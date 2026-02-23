import os
import glob
import re

program_dir = os.path.join(os.getcwd(), 'public', 'program')
md_files = glob.glob(os.path.join(program_dir, 'a*.md'))

for md_file in md_files:
    if '_extended' in md_file: continue
    
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We want to remove leading spaces from any line that is part of the HTML
    # An easy heuristic: if a line starts with spaces, and we are not inside a markdown list/code block
    # Honestly, we can just replace 4-space indents at the start of a line with nothing.
    # To be safe and preserve markdown lists, let's only do it for lines inside the top HTML shell,
    # OR just un-indent lines that start with spaces followed by '<', or spaces followed by normal text
    # Let's just strip leading whitespace from all lines EXCEPT those that look like markdown lists (- , * , 1. )
    
    lines = content.split('\n')
    new_lines = []
    in_code_block = False
    
    for line in lines:
        stripped = line.lstrip()
        # If line is a markdown list or quote, keep original
        if stripped.startswith('- ') or stripped.startswith('* ') or re.match(r'^\d+\.', stripped) or stripped.startswith('> '):
            new_lines.append(line)
        # If it's a code block marker
        elif stripped.startswith('```'):
            in_code_block = not in_code_block
            new_lines.append(line)
        elif in_code_block:
            new_lines.append(line)
        else:
            # It's an HTML line or regular text. Strip leading whitespace.
            new_lines.append(stripped)
            
    with open(md_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(new_lines))
        
print(f"Fixed {len(md_files)} files.")
