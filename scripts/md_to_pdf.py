import os
import re
import shutil
import subprocess
import tempfile
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PyPDF2 import PdfReader, PdfWriter


# ─── Vault detection ─────────────────────────────────────────────────────────

def find_vault_root(files):
    path = os.path.commonpath(files)
    if os.path.isfile(path):
        path = os.path.dirname(path)
    current = path
    while True:
        if os.path.isdir(os.path.join(current, '.obsidian')):
            return current
        parent = os.path.dirname(current)
        if parent == current:
            return path  # fallback: common ancestor
        current = parent


# ─── Image map ───────────────────────────────────────────────────────────────

def build_image_map(vault_root):
    image_map = {}
    for root, _, files in os.walk(vault_root):
        if os.path.basename(root) == 'attachments':
            for f in files:
                image_map[f] = os.path.join(root, f)
    return image_map


# ─── Preprocessing ───────────────────────────────────────────────────────────

def preprocess_callouts(content):
    lines = content.split('\n')
    result = []
    i = 0
    while i < len(lines):
        m = re.match(r'^> \[!(\w+)\][+\-]?[ \t]*(.*)', lines[i])
        if m:
            callout_type = m.group(1).upper()
            title = m.group(2).strip() or callout_type
            body_lines = []
            i += 1
            while i < len(lines) and lines[i].startswith('>'):
                line = lines[i][1:]
                if line.startswith(' '):
                    line = line[1:]
                body_lines.append(line)
                i += 1
            result.append(f'> **[{callout_type}] {title}**')
            result.append('>')
            for bl in body_lines:
                result.append(f'> {bl}')
            result.append('')
        else:
            result.append(lines[i])
            i += 1
    return '\n'.join(result)


def preprocess_images(content, image_map, skip_svgs=False):
    def replace_wikilink(m):
        inner = m.group(1).strip()
        filename = inner.split('|')[0].strip()
        path = image_map.get(filename, filename)
        if skip_svgs and path.lower().endswith('.svg'):
            return f'*[SVG: {filename}]*'
        return f'![]({path})'

    content = re.sub(r'!\[\[([^\]]+)\]\]', replace_wikilink, content)

    def replace_std(m):
        alt = m.group(1).split('|')[0].strip()
        path = m.group(2).strip()
        basename = os.path.basename(path)
        if basename in image_map:
            path = image_map[basename]
        if skip_svgs and path.lower().endswith('.svg'):
            return f'*[SVG: {alt or basename}]*'
        return f'![{alt}]({path})'

    content = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', replace_std, content)
    return content


def preprocess_math(content):
    # Ensure blank line before a standalone $$ line so pandoc recognises it as display math
    content = re.sub(r'(?<=[^\n])\n(\$\$[ \t]*\n)', r'\n\n\1', content)
    # Ensure blank line after a standalone $$ line
    content = re.sub(r'(\n\$\$[ \t]*)\n(?=[^\n$])', r'\1\n\n', content)
    # MathJax allows \begin{array}{} (empty column spec); LaTeX does not
    content = content.replace('\\begin{array}{}', '\\begin{array}{l}')
    return content


def preprocess(content, image_map, skip_svgs=False):
    content = preprocess_callouts(content)
    content = preprocess_math(content)
    content = preprocess_images(content, image_map, skip_svgs=skip_svgs)
    return content


# ─── Conversion ──────────────────────────────────────────────────────────────

def md_to_pdf(md_path, output_pdf, image_map, skip_svgs=False):
    with open(md_path, encoding='utf-8') as f:
        content = f.read()

    content = preprocess(content, image_map, skip_svgs=skip_svgs)

    with tempfile.NamedTemporaryFile(mode='w', suffix='.md', delete=False, encoding='utf-8') as tmp:
        tmp.write(content)
        tmp_path = tmp.name

    try:
        result = subprocess.run(
            [
                'pandoc', tmp_path,
                '-o', output_pdf,
                '--pdf-engine=xelatex',
                # Only treat $...$ and $$...$$ as math; \(...\) may be literal text
                '--from=markdown-tex_math_single_backslash',
                '-V', 'geometry:margin=2cm',
                '-V', 'colorlinks=true',
                '-V', 'linkcolor=blue',
            ],
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            raise subprocess.CalledProcessError(result.returncode, 'pandoc', stderr=result.stderr)
    finally:
        os.unlink(tmp_path)


def merge_pdfs(pdf_paths, output_path):
    writer = PdfWriter()
    for path in pdf_paths:
        reader = PdfReader(path)
        for page in reader.pages:
            writer.add_page(page)
    with open(output_path, 'wb') as f:
        writer.write(f)


# ─── GUI ─────────────────────────────────────────────────────────────────────

def check_dependencies():
    missing = []
    if shutil.which('pandoc') is None:
        missing.append('pandoc        →  brew install pandoc')
    if shutil.which('xelatex') is None:
        missing.append('xelatex       →  brew install --cask mactex-no-gui')
    if missing:
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("Missing dependencies", "Install the following:\n\n" + '\n'.join(missing))
        root.destroy()
        return False
    return shutil.which('rsvg-convert') is not None  # True = SVGs supported, False = skip them


def pick_files():
    root = tk.Tk()
    root.withdraw()
    files = filedialog.askopenfilenames(
        title="Select Markdown files to export",
        filetypes=[("Markdown", "*.md"), ("All files", "*.*")],
    )
    root.destroy()
    return list(files)


class OrderWindow:
    def __init__(self, files):
        self.files = list(files)
        self.result = None
        self._drag_idx = None

        self.root = tk.Tk()
        self.root.title("Order files")
        self.root.geometry("520x400")
        self.root.resizable(True, True)

        tk.Label(self.root, text="Drag to reorder:", anchor='w').pack(fill=tk.X, padx=12, pady=(12, 4))

        frame = tk.Frame(self.root)
        frame.pack(fill=tk.BOTH, expand=True, padx=12)

        sb = tk.Scrollbar(frame)
        sb.pack(side=tk.RIGHT, fill=tk.Y)

        self.lb = tk.Listbox(
            frame,
            yscrollcommand=sb.set,
            selectmode=tk.SINGLE,
            font=('Helvetica', 13),
            activestyle='none',
            selectbackground='#4a90d9',
            selectforeground='white',
        )
        self.lb.pack(fill=tk.BOTH, expand=True)
        sb.config(command=self.lb.yview)

        for f in self.files:
            self.lb.insert(tk.END, os.path.basename(f))

        self.lb.bind('<Button-1>', self._click)
        self.lb.bind('<B1-Motion>', self._drag)
        self.lb.bind('<ButtonRelease-1>', self._release)

        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)
        tk.Button(btn_frame, text="Confirm", command=self._confirm, width=12).pack(side=tk.LEFT, padx=6)
        tk.Button(btn_frame, text="Cancel", command=self._cancel, width=12).pack(side=tk.LEFT, padx=6)

        self.root.mainloop()

    def _click(self, e):
        self._drag_idx = self.lb.nearest(e.y)
        self.lb.selection_clear(0, tk.END)
        self.lb.selection_set(self._drag_idx)

    def _drag(self, e):
        if self._drag_idx is None:
            return
        target = self.lb.nearest(e.y)
        if target == self._drag_idx:
            return
        text = self.lb.get(self._drag_idx)
        path = self.files[self._drag_idx]
        self.lb.delete(self._drag_idx)
        self.files.pop(self._drag_idx)
        self.lb.insert(target, text)
        self.files.insert(target, path)
        self._drag_idx = target
        self.lb.selection_clear(0, tk.END)
        self.lb.selection_set(target)

    def _release(self, e):
        self._drag_idx = None

    def _confirm(self):
        self.result = self.files
        self.root.destroy()

    def _cancel(self):
        self.result = None
        self.root.destroy()


class ProgressWindow:
    def __init__(self, total):
        self.root = tk.Tk()
        self.root.title("Exporting...")
        self.root.geometry("440x90")
        self.root.resizable(False, False)
        self.label = tk.Label(self.root, text="Starting...", anchor='w')
        self.label.pack(fill=tk.X, padx=12, pady=(12, 4))
        self.bar = ttk.Progressbar(self.root, maximum=total, length=400)
        self.bar.pack(padx=12)

    def update(self, step, msg):
        self.label.config(text=msg)
        self.bar['value'] = step
        self.root.update()

    def close(self):
        self.root.destroy()


# ─── Main ────────────────────────────────────────────────────────────────────

def main():
    has_rsvg = check_dependencies()
    if has_rsvg is False:
        return  # hard dependency missing
    skip_svgs = not has_rsvg

    files = pick_files()
    if not files:
        return

    order_win = OrderWindow(files)
    ordered = order_win.result
    if not ordered:
        return

    root = tk.Tk()
    root.withdraw()
    output_path = filedialog.asksaveasfilename(
        title="Save merged PDF",
        defaultextension=".pdf",
        filetypes=[("PDF", "*.pdf")],
    )
    root.destroy()
    if not output_path:
        return

    vault_root = find_vault_root(ordered)
    image_map = build_image_map(vault_root)

    if skip_svgs:
        root2 = tk.Tk()
        root2.withdraw()
        messagebox.showwarning(
            "SVG images will be skipped",
            "rsvg-convert not found — SVG images will be replaced with placeholders.\n\n"
            "To enable SVGs:  brew install librsvg",
        )
        root2.destroy()

    progress = ProgressWindow(len(ordered))
    errors = []

    with tempfile.TemporaryDirectory() as tmpdir:
        pdf_paths = []
        for i, md_path in enumerate(ordered):
            name = os.path.basename(md_path)
            progress.update(i, f"Converting {i + 1}/{len(ordered)}: {name}")
            out = os.path.join(tmpdir, f'{i:04d}.pdf')
            try:
                md_to_pdf(md_path, out, image_map, skip_svgs=skip_svgs)
                pdf_paths.append(out)
            except subprocess.CalledProcessError as e:
                errors.append(f"{name}:\n  {e.stderr.strip()}")

        if pdf_paths:
            progress.update(len(ordered), "Merging PDFs...")
            merge_pdfs(pdf_paths, output_path)

    progress.close()

    if errors:
        messagebox.showwarning(
            "Completed with errors",
            f"Saved to:\n{output_path}\n\nFailed files:\n\n" + '\n'.join(errors),
        )
    else:
        messagebox.showinfo("Done", f"Saved to:\n{output_path}")


if __name__ == '__main__':
    main()
