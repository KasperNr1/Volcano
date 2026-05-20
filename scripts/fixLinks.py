import os
import re
import shutil
from pathlib import Path
from urllib.parse import unquote, quote

# Paths
SCRIPTS_DIR = Path(__file__).parent.resolve()
VAULT_DIR = SCRIPTS_DIR.parent

# Dictionaries to locate any file by its globally unique name
md_files = {}
attachment_files = {}
IMG_EXTS = {'.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp', '.pdf'}

# 1. Inventory the vault
for p in VAULT_DIR.rglob('*'):
    if not p.is_file() or '.obsidian' in p.parts or p.parent == SCRIPTS_DIR:
        continue
        
    if p.suffix.lower() == '.md':
        md_files[p.name] = p
    elif p.suffix.lower() in IMG_EXTS:
        attachment_files[p.name] = p

# Regex to match standard Markdown links: [text](target) or ![alt](target)
link_pattern = re.compile(r'(!?)\[([^\]]*)\]\(([^)]+)\)')
moved_images = set()

# 2. Process all markdown files
for md_path in md_files.values():
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()

    def replace_link(match):
        is_image = match.group(1) == '!'
        alt_text = match.group(2)
        target = match.group(3)
        
        # Ignore external links
        if target.startswith(('http://', 'https://', 'obsidian://')):
            return match.group(0)
            
        # Separate heading from filename
        if '#' in target:
            file_part, heading = target.split('#', 1)
            heading = '#' + heading
        else:
            file_part = target
            heading = ''
            
        file_name = Path(unquote(file_part)).name
        if not file_name:
            return match.group(0)

        # Handle Images
        if is_image and file_name in attachment_files:
            if file_name not in moved_images:
                # First mention: move the physical file
                current_img_path = attachment_files[file_name]
                new_attachments_dir = md_path.parent / 'attachments'
                new_img_path = new_attachments_dir / file_name
                
                new_attachments_dir.mkdir(exist_ok=True)
                if current_img_path.exists() and current_img_path != new_img_path:
                    shutil.move(str(current_img_path), str(new_img_path))
                
                attachment_files[file_name] = new_img_path
                moved_images.add(file_name)
            
            # Update link with relative path to wherever the image now lives
            final_img_path = attachment_files[file_name]
            rel_path = os.path.relpath(final_img_path, md_path.parent)
            safe_rel_path = quote(Path(rel_path).as_posix(), safe='/')
            
            return f"![{alt_text}]({safe_rel_path})"
            
        # Handle Note Links
        elif not is_image and file_name.endswith('.md'):
            if file_name in md_files:
                # Enforce pathless unique filename + heading
                safe_file_name = quote(file_name)
                return f"[{alt_text}]({safe_file_name}{heading})"
        
        return match.group(0)

    # Apply replacements
    new_content = link_pattern.sub(replace_link, content)
    
    # Save if changes were made
    if new_content != content:
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

print("Finished processing vault links and moving attachments!")