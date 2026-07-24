import argparse
import hashlib
import json
import re
import sys
from collections import defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path
from urllib.parse import unquote


VAULT_DIR = Path(__file__).resolve().parent.parent
IGNORED_DIRS = {".git", ".obsidian", ".venv", "__pycache__"}
WIKILINK_RE = re.compile(r"(!?)\[\[([^\]]+)\]\]")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*#*\s*$")
BLOCK_ID_RE = re.compile(r"(?:^|\s)\^([A-Za-z0-9-]+)\s*$")
MARKER_RE = re.compile(r"\b(TODO|FIXME|MISSING)\b", re.IGNORECASE)
NUMBERED_NOTE_RE = re.compile(r"^(\d{2})(?:\s|$)")
URI_RE = re.compile(r"^[A-Za-z][A-Za-z0-9+.-]*:")


@dataclass(frozen=True)
class Issue:
    kind: str
    path: str
    line: int
    message: str


@dataclass
class Note:
    path: Path
    text: str
    scan_lines: list[str]
    headings: dict[str, list[tuple[str, int]]]
    block_ids: set[str]


def relative(path: Path) -> str:
    return path.relative_to(VAULT_DIR).as_posix()


def normalize_heading(value: str) -> str:
    value = unquote(value).strip().casefold()
    value = re.sub(r"[`*_~]", "", value)
    value = re.sub(r"[^\w]+", " ", value)
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def lines_without_code(text: str) -> list[str]:
    result = []
    fence = None
    for line in text.splitlines():
        fence_match = re.match(r"^\s*(`{3,}|~{3,})", line)
        if fence_match:
            marker = fence_match.group(1)[0]
            fence = None if fence == marker else marker
            result.append("")
            continue
        if fence:
            result.append("")
            continue
        line = re.sub(r"<!--.*?-->", "", line)
        line = re.sub(r"`[^`]*`", "", line)
        result.append(line)
    return result


def markdown_link_targets(line: str):
    position = 0
    while position < len(line):
        opening = line.find("[", position)
        if opening < 0:
            return
        if opening + 1 < len(line) and line[opening + 1] == "[":
            position = opening + 2
            continue
        label_end = line.find("](", opening + 1)
        if label_end < 0:
            return
        target_start = label_end + 2
        depth = 1
        cursor = target_start
        while cursor < len(line) and depth:
            if line[cursor] == "\\":
                cursor += 2
                continue
            if line[cursor] == "(":
                depth += 1
            elif line[cursor] == ")":
                depth -= 1
            cursor += 1
        if depth:
            yield None
            return
        yield line[target_start:cursor - 1]
        position = cursor


def load_notes() -> list[Note]:
    notes = []
    for path in sorted(VAULT_DIR.rglob("*.md")):
        if any(part in IGNORED_DIRS for part in path.parts):
            continue
        text = path.read_text(encoding="utf-8-sig")
        scan_lines = lines_without_code(text)
        headings = defaultdict(list)
        block_ids = set()
        for line_number, line in enumerate(scan_lines, start=1):
            heading = HEADING_RE.match(line)
            if heading:
                title = heading.group(2).strip()
                headings[normalize_heading(title)].append((title, line_number))
            block = BLOCK_ID_RE.search(line)
            if block:
                block_ids.add(block.group(1).casefold())
        notes.append(Note(path, text, scan_lines, dict(headings), block_ids))
    return notes


def split_target(target: str) -> tuple[str, str]:
    target = target.strip()
    if target.startswith("<") and ">" in target:
        target = target[1:target.index(">")]
    elif re.search(r"\s+[\"']", target):
        target = re.split(r"\s+[\"']", target, maxsplit=1)[0]
    target = unquote(target)
    if "#" in target:
        return tuple(target.split("#", 1))
    return target, ""


def resolve_standard_target(
    source: Path,
    file_part: str,
    files_by_name: dict[str, list[Path]],
) -> tuple[Path | None, bool]:
    if not file_part:
        return source, False
    normalized_part = file_part.replace("\\", "/")
    if not normalized_part.startswith("/"):
        candidate = (source.parent / Path(normalized_part)).resolve()
        if candidate.exists():
            return candidate, False
    vault_candidate = (VAULT_DIR / Path(normalized_part.lstrip("/"))).resolve()
    if vault_candidate.exists():
        return vault_candidate, True
    name = Path(file_part).name.casefold()
    global_matches = files_by_name.get(name, [])
    if len(global_matches) == 1:
        return global_matches[0], True
    return None, False


def resolve_wikilink(
    source: Path,
    file_part: str,
    notes_by_stem: dict[str, list[Note]],
    notes_by_path: dict[str, Note],
) -> Note | None:
    if not file_part:
        return notes_by_path.get(str(source.resolve()).casefold())
    normalized = unquote(file_part).replace("\\", "/").removesuffix(".md")
    if "/" in normalized:
        suffix = f"/{normalized.casefold()}.md"
        matches = [note for key, note in notes_by_path.items() if key.replace("\\", "/").endswith(suffix)]
        return matches[0] if len(matches) == 1 else None
    matches = notes_by_stem.get(normalized.casefold(), [])
    return matches[0] if len(matches) == 1 else None


def validate_fragment(target: Note, fragment: str) -> bool:
    if not fragment:
        return True
    if fragment.startswith("^"):
        return fragment[1:].casefold() in target.block_ids
    return normalize_heading(fragment) in target.headings


def audit_links(notes: list[Note], include_portability: bool = False) -> list[Issue]:
    issues = []
    notes_by_path = {str(note.path.resolve()).casefold(): note for note in notes}
    notes_by_stem = defaultdict(list)
    for note in notes:
        notes_by_stem[note.path.stem.casefold()].append(note)

    files_by_name = defaultdict(list)
    for path in VAULT_DIR.rglob("*"):
        if path.is_file() and not any(part in IGNORED_DIRS for part in path.parts):
            files_by_name[path.name.casefold()].append(path.resolve())

    for note in notes:
        for line_number, line in enumerate(note.scan_lines, start=1):
            for target_text in markdown_link_targets(line):
                if target_text is None:
                    issues.append(Issue("malformed-link", relative(note.path), line_number, "Markdown-Link ist nicht geschlossen"))
                    continue
                file_part, fragment = split_target(target_text)
                if URI_RE.match(file_part) or file_part.startswith(("//", "mailto:")):
                    continue
                target_path, used_global_fallback = resolve_standard_target(note.path, file_part, files_by_name)
                if target_path is None:
                    issues.append(Issue("broken-link", relative(note.path), line_number, f"Ziel nicht gefunden: {target_text}"))
                    continue
                if used_global_fallback and include_portability:
                    issues.append(Issue("nonportable-link", relative(note.path), line_number, f"Nur über den global eindeutigen Dateinamen auflösbar: {target_text}"))
                target_note = notes_by_path.get(str(target_path.resolve()).casefold())
                if fragment and target_note and not validate_fragment(target_note, fragment):
                    issues.append(Issue("broken-anchor", relative(note.path), line_number, f"Anker nicht gefunden: {target_text}"))

            for match in WIKILINK_RE.finditer(line):
                raw_target = match.group(2).split("|", 1)[0].strip()
                file_part, fragment = split_target(raw_target)
                if match.group(1) == "!" and Path(file_part).suffix.lower() not in {"", ".md"}:
                    target_path, _ = resolve_standard_target(note.path, file_part, files_by_name)
                    if target_path is None:
                        issues.append(Issue("broken-embed", relative(note.path), line_number, f"Einbettung nicht gefunden: {raw_target}"))
                    continue
                target_note = resolve_wikilink(note.path, file_part, notes_by_stem, notes_by_path)
                if target_note is None:
                    issues.append(Issue("broken-wikilink", relative(note.path), line_number, f"Notiz nicht eindeutig gefunden: {raw_target}"))
                elif fragment and not validate_fragment(target_note, fragment):
                    issues.append(Issue("broken-anchor", relative(note.path), line_number, f"Anker nicht gefunden: {raw_target}"))
    return issues


def meaningful_text(note: Note) -> str:
    text = re.sub(r"\A---\s*\n.*?\n---\s*\n", "", note.text, flags=re.DOTALL)
    text = "\n".join(note.scan_lines) if text == note.text else text
    text = re.sub(r"[#>*_~|\[\]()-]", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def audit_structure(notes: list[Note]) -> list[Issue]:
    issues = []
    hashes = defaultdict(list)
    numbered_by_folder = defaultdict(lambda: defaultdict(list))

    for note in notes:
        path = relative(note.path)
        content = meaningful_text(note)
        if not content:
            issues.append(Issue("empty-note", path, 1, "Notiz enthält keinen Inhalt"))
        elif len(content) < 40:
            issues.append(Issue("short-note", path, 1, f"Sehr kurze Notiz ({len(content)} Zeichen Inhalt)"))

        normalized_content = re.sub(r"\s+", " ", note.text).strip().casefold()
        if len(content) >= 100:
            hashes[hashlib.sha256(normalized_content.encode("utf-8")).hexdigest()].append(note.path)

        for normalized, occurrences in note.headings.items():
            if len(occurrences) > 1:
                lines = ", ".join(str(line) for _, line in occurrences)
                issues.append(Issue("duplicate-heading", path, occurrences[1][1], f"Überschrift '{occurrences[0][0]}' mehrfach in Zeilen {lines}"))

        for line_number, line in enumerate(note.scan_lines, start=1):
            if MARKER_RE.search(line):
                issues.append(Issue("open-marker", path, line_number, line.strip()))

        number_match = NUMBERED_NOTE_RE.match(note.path.stem)
        if number_match:
            numbered_by_folder[note.path.parent][number_match.group(1)].append(note.path)

        fence_counts = {marker: len(re.findall(rf"^\s*{re.escape(marker)}", note.text, re.MULTILINE)) for marker in ("```", "~~~")}
        for marker, count in fence_counts.items():
            if count % 2:
                issues.append(Issue("unclosed-fence", path, 1, f"Ungerade Anzahl von {marker}-Codebegrenzungen: {count}"))
        if len(re.findall(r"^\s*\$\$\s*$", note.text, re.MULTILINE)) % 2:
            issues.append(Issue("unclosed-math", path, 1, "Ungerade Anzahl eigenständiger $$-Begrenzungen"))

    for matching_paths in hashes.values():
        if len(matching_paths) > 1:
            duplicates = ", ".join(relative(path) for path in matching_paths)
            for path in matching_paths[1:]:
                issues.append(Issue("duplicate-note", relative(path), 1, f"Inhalt identisch mit: {duplicates}"))

    for folder, notes_by_number in numbered_by_folder.items():
        if len(notes_by_number) < 3:
            continue
        for number, paths in notes_by_number.items():
            if len(paths) > 1:
                names = ", ".join(path.name for path in paths)
                issues.append(Issue("duplicate-number", relative(paths[1]), 1, f"Nummer {number} im Ordner mehrfach vergeben: {names}"))
    return issues


def print_text(issues: list[Issue], note_count: int) -> None:
    grouped = defaultdict(list)
    for issue in issues:
        grouped[issue.kind].append(issue)
    print(f"Geprüfte Markdown-Dateien: {note_count}")
    print(f"Befunde: {len(issues)}")
    for kind in sorted(grouped):
        print(f"\n[{kind}] {len(grouped[kind])}")
        for issue in grouped[kind]:
            print(f"- {issue.path}:{issue.line} - {issue.message}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Prüft einen Obsidian-Vault, ohne Dateien zu verändern.")
    parser.add_argument("--json", action="store_true", help="Befunde als JSON ausgeben")
    parser.add_argument("--portability", action="store_true", help="Nur in Obsidian auflösbare Kurzlinks zusätzlich melden")
    parser.add_argument("--strict", action="store_true", help="Bei Befunden mit Exit-Code 1 enden")
    args = parser.parse_args()

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    notes = load_notes()
    issues = sorted(audit_links(notes, args.portability) + audit_structure(notes), key=lambda item: (item.kind, item.path, item.line))
    if args.json:
        print(json.dumps({"notes": len(notes), "issues": [asdict(issue) for issue in issues]}, ensure_ascii=False, indent=2))
    else:
        print_text(issues, len(notes))
    if args.strict and issues:
        raise SystemExit(1)


if __name__ == "__main__":
    main()