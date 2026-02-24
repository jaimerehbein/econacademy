import os
import re

TARGET_DIR = "/Users/machd/Desktop/licecon/web-portal/public/program"

def inject_marker(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "<!-- GLOSARIO -->" in content:
        return False
        
    # Buscar el footer o el final del documento
    if "<!-- FOOTER -->" in content:
        new_content = content.replace("<!-- FOOTER -->", "<!-- GLOSARIO -->\n<!-- FOOTER -->")
    else:
        # Intentar insertar antes de los últimos tags de cierre div
        match = re.search(r'(\s*</div>\s*</div>\s*)$', content, re.DOTALL)
        if match:
            new_content = content[:match.start()] + "\n<!-- GLOSARIO -->\n" + match.group(1)
        else:
            new_content = content + "\n<!-- GLOSARIO -->\n"
            
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    return True

def main():
    files = [f for f in os.listdir(TARGET_DIR) if f.endswith('.md')]
    count = 0
    for f in files:
        if inject_marker(os.path.join(TARGET_DIR, f)):
            print(f"Inyectado marcador en {f}")
            count += 1
    print(f"Total marcadores inyectados: {count}")

if __name__ == "__main__":
    main()
