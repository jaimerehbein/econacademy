import os
import re
import glob

# Defines the replacements mapping from light theme classes to our Top-Tier dark theme classes
# Using regex groups to capture the color name dynamically
replacements = [
    (r'\bbg-(slate|gray|zinc|neutral|stone)-50\b', r'bg-\1-800/40'),
    (r'\bbg-white\b', r'bg-transparent'),
    # e.g., bg-cyan-50 -> bg-cyan-500/10
    (r'\bbg-([a-z]+)-50\b', r'bg-\1-500/10'),
    (r'\bbg-([a-z]+)-100\b', r'bg-\1-500/10'),
    
    # Text colors
    (r'\btext-(slate|gray|zinc|neutral|stone)-800\b', r'text-slate-200'),
    (r'\btext-(slate|gray|zinc|neutral|stone)-900\b', r'text-white'),
    (r'\btext-(slate|gray|zinc|neutral|stone)-950\b', r'text-white'),
    (r'\btext-(slate|gray|zinc|neutral|stone)-400\b', r'text-slate-400'), # Keep as is, or soften
    (r'\btext-gray-400\b', r'text-slate-500'),
    (r'\btext-black\b', r'text-white'),

    # Colorful Text
    (r'\btext-([a-z]+)-800\b', r'text-\1-300'),
    (r'\btext-([a-z]+)-900\b', r'text-\1-300'),
    (r'\btext-([a-z]+)-950\b', r'text-\1-300'),
    
    # Borders
    (r'\bborder-(slate|gray|zinc|neutral|stone)-100\b', r'border-white/10'),
    (r'\bborder-(slate|gray|zinc|neutral|stone)-200\b', r'border-white/10'),
    (r'\bborder-(slate|gray|zinc|neutral|stone)-300\b', r'border-white/10'),
    (r'\bborder-([a-z]+)-200\b', r'border-\1-500/30'),
    (r'\bborder-([a-z]+)-300\b', r'border-\1-500/30'),

    # Prose background adjustments
    (r'\bbg-slate-900\b', r'bg-slate-900/50'), # soften dark backgrounds inside prose
]

def patch_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    for pattern, replacement in replacements:
        content = re.sub(pattern, replacement, content)

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Patched: {os.path.basename(filepath)}")

def main():
    directory = '/Users/machd/Desktop/licecon/web-portal/public/program'
    md_files = glob.glob(os.path.join(directory, '*.md'))
    for filepath in md_files:
        patch_file(filepath)
    print(f"Finished patching {len(md_files)} markdown files.")

if __name__ == "__main__":
    main()
