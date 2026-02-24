import os
import re
import json
import time
import urllib.request
import urllib.error
import sys

# Configuración de APIs
MANUS_API_KEY = "sk-PkiBpff8Awdb6gKGYsqcfP8raHdifCEWYGOBKjEJLDIOiWNaPIbF7uOoj87Hn93HigCIKSw1igVPrcvqJPP7Nv19kTS0"
MANUS_CREATE_URL = "https://api.manus.ai/v1/tasks"
MANUS_POLL_URL = "https://api.manus.ai/v1/tasks/"

# Modelos y carpetas
TARGET_DIR = "/Users/machd/Desktop/licecon/web-portal/public/program"

# v9.5: Lista vacía para forzar el re-procesamiento de TODOS los módulos con el nuevo diseño
already_fixed = []

GLOSSARY_TEMPLATE = """
<!-- GLOSARIO v9.5 -->
<section id="glosario" class="mt-24 mb-16 relative">
    <div class="flex items-center gap-4 mb-10">
        <div class="w-1.5 h-8 bg-{color}-500 rounded-full shadow-[0_0_15px_rgba(var(--color-rgb),0.5)]"></div>
        <h2 class="text-2xl font-black text-white tracking-tight uppercase italic">Glosario Técnico</h2>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-6 relative z-10">
{items}
    </div>
</section>
"""

ITEM_TEMPLATE = """
        <div class="group p-6 rounded-2xl bg-slate-900/40 backdrop-blur-sm border border-white/5 hover:border-{color}-500/30 transition-all duration-500 hover:shadow-2xl hover:shadow-{color}-500/5">
            <h3 class="text-sm font-black text-{color}-400 mb-2 uppercase tracking-widest flex items-center gap-2">
                <span class="w-1.5 h-1.5 rounded-full bg-{color}-500 animate-pulse"></span>
                {term}
            </h3>
            <p class="text-slate-400 text-sm leading-relaxed font-medium">
                {definition}
            </p>
        </div>
"""

def log(msg):
    print(msg)
    sys.stdout.flush()

def generate_content_with_manus(prompt):
    headers = {
        "API_KEY": MANUS_API_KEY,
        "Content-Type": "application/json"
    }
    
    # 1. Crear Tarea
    data = {"prompt": prompt}
    try:
        req = urllib.request.Request(MANUS_CREATE_URL, data=json.dumps(data).encode(), headers=headers)
        with urllib.request.urlopen(req) as response:
            res = json.loads(response.read().decode())
            task_id = res.get("task_id")
            if not task_id:
                log("Error: No se obtuvo task_id")
                return None
            log(f"Tarea creada en Manus: {task_id}")
    except Exception as e:
        log(f"Error creando tarea: {e}")
        return None

    # 2. Polling
    poll_url = MANUS_POLL_URL + task_id
    for i in range(40): 
        time.sleep(15)
        log(f"  Polling Manus ({task_id}) - Intento {i+1}...")
        try:
            req = urllib.request.Request(poll_url, headers=headers)
            with urllib.request.urlopen(req) as response:
                res = json.loads(response.read().decode())
                status = res.get("status")
                if status == "completed":
                    output_list = res.get("output", [])
                    for item in reversed(output_list):
                        if item.get("role") == "assistant" and (item.get("type") == "message" or item.get("type") == "text"):
                            content = item.get("content")
                            if isinstance(content, list):
                                for part in content:
                                    if part.get("type") == "output_text":
                                        text = part.get("text")
                                        if "{" in text and "}" in text:
                                            log(f"  ✅ Contenido extraído de {task_id}.")
                                            return text
                            elif isinstance(content, dict):
                                text = content.get("text")
                                if text: return text
                elif status == "error":
                    log(f"  ❌ Tarea {task_id} reportó error.")
                    return None
        except Exception as e:
            log(f" Error en polling ({task_id}): {e}")
            break
    return None

def extract_color(content):
    match = re.search(r'bg-(\w+)-500', content)
    return match.group(1) if match else "blue"

def clean_json_response(text):
    if not text: return None
    text = re.sub(r'```json\s*', '', text)
    text = re.sub(r'```\s*', '', text)
    try:
        return json.loads(text.strip())
    except Exception as e:
        match = re.search(r'({.*})', text, re.DOTALL)
        if match:
            try: return json.loads(match.group(1))
            except: pass
    return None

def process_file(filepath):
    filename = os.path.basename(filepath)
    if filename in already_fixed:
        return False

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Si ya tiene v9.5, saltar
    if "<!-- GLOSARIO v9.5 -->" in content:
        return False

    if "<!-- GLOSARIO -->" not in content:
        return False

    color = extract_color(content)
    
    prompt = f"""
Actúa como un experto en economía de nivel Master. Analiza el siguiente contenido y genera un JSON con exactamente 10 términos clave y sus definiciones académicas rigurosas.
REGLA DE ORO: NO uses herramientas de búsqueda ni navegación. Procesa SOLO el texto proporcionado.
Formato: {{"terms": [{{"term": "Nombre", "definition": "Definición técnica"}}]}}
ENTREGA SOLO EL JSON.

CONTENIDO:
{content[:15000]}
"""

    log(f"Iniciando procesamiento de {filename}...")
    raw_response = generate_content_with_manus(prompt)
    data = clean_json_response(raw_response)
    
    if not data or "terms" not in data:
        log(f"  Falló la obtención de JSON para {filename}")
        return False

    items_html = ""
    for item in data["terms"]:
        items_html += ITEM_TEMPLATE.format(
            color=color,
            term=item["term"],
            definition=item["definition"]
        )

    new_glossary = GLOSSARY_TEMPLATE.format(color=color, items=items_html)

    parts = content.split("<!-- GLOSARIO -->")
    if len(parts) < 2: 
        # Si no tiene el marcador normal pero sí una versión anterior, intentar limpiar
        parts = re.split(r'<!-- GLOSARIO v\d\.\d -->', content)
        if len(parts) < 2: return False
    
    main_part = parts[0]
    remainder = parts[1]
    
    # Limpiar el glosario anterior si existe antes de buscar el footer
    remainder = re.sub(r'<section id="glosario".*?</section>', '', remainder, flags=re.DOTALL)
    
    if "<!-- FOOTER -->" in remainder:
        footer_parts = remainder.split("<!-- FOOTER -->")
        footer_content = "<!-- FOOTER -->" + footer_parts[1]
    else:
        split_match = re.search(r'(\s*</div>\s*</div>\s*)$', remainder, re.DOTALL)
        footer_content = split_match.group(1) if split_match else ""

    final_content = main_part + "<!-- GLOSARIO -->\n" + new_glossary + "\n" + footer_content
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(final_content)
    
    log(f"  ✨ {filename} actualizado a v9.5.")
    return True

def main():
    files = [f for f in sorted(os.listdir(TARGET_DIR)) if f.endswith('.md')]
    # PRIORIDAD: Módulos críticos primero
    files.sort(key=lambda x: (
        0 if 'mic' in x else 
        1 if 'ep' in x else 
        2 if 'mac' in x else 
        3 if 'eb' in x else 4, 
        x
    ))
    
    count = 0
    for f in files:
        if process_file(os.path.join(TARGET_DIR, f)):
            count += 1
            # Pausa para no saturar API
            time.sleep(2)
    
    log(f"Finalizado. Total archivos actualizados a v9.5: {count}")

if __name__ == "__main__":
    main()
