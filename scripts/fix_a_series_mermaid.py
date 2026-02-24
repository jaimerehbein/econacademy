import os
import glob
import re

def fix_mermaid_in_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # Regex to find ```mermaid and replace it with <pre class="mermaid bg-transparent flex justify-center">
    # and the closing ``` with </pre>
    
    # We look for exactly ```mermaid followed by newlines and content, and ending with ```
    # Note: re.sub with DOTALL matches across newlines
    
    pattern1 = r'```mermaid\s*\n(.*?)\n\s*```'
    replacement1 = r'<pre class="mermaid bg-transparent flex justify-center">\n\1\n</pre>'
    
    new_content = re.sub(pattern1, replacement1, content, flags=re.DOTALL)
    
    # Check if there's any xychart-beta that needs fixing
    pattern2 = r'```mermaid\nxychart-beta(.*?)\n```'
    replacement2 = r'<pre class="mermaid bg-transparent flex justify-center">\nxychart-beta\1\n</pre>'
    new_content = re.sub(pattern2, replacement2, new_content, flags=re.DOTALL)
    
    if new_content != content:
        with open(filepath, 'w') as f:
            f.write(new_content)
        print(f"Fixed mermaid in {os.path.basename(filepath)}")
        return True
    return False

if __name__ == "__main__":
    files = glob.glob("/Users/machd/Desktop/licecon/web-portal/public/program/a*.md")
    count = 0
    for file in files:
        if fix_mermaid_in_file(file):
            count += 1
    print(f"Fixed {count} files.")
