"""
batch_enrich_thin_modules.py
Targeted enrichment for modules flagged as THIN by the audit:
A6, A20, A23, A24, A25, A29, A31, A34, A35, A38, A39, A40
"""
import asyncio
import os
import json
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# ── Modules to enrich ────────────────────────────────────────────────────────
THIN_MODULES = [
    "A6", "A20", "A23", "A24", "A25",
    "A29", "A31", "A34", "A35", "A38", "A39", "A40"
]

# ── Helpers ───────────────────────────────────────────────────────────────────

def extract_syllabus(subject_code, malla_path):
    if not subject_code.startswith('A'):
        return ""
    try:
        num = int(subject_code[1:])
        start_str = f"Asignatura {num}."
        end_str   = f"Asignatura {num+1}."
        with open(malla_path, 'r', encoding='utf-8') as f:
            content = f.read()
        start_idx = content.find(start_str)
        if start_idx == -1:
            return ""
        end_idx = content.find(end_str, start_idx)
        if end_idx == -1:
            end_idx = len(content)
        return content[start_idx:end_idx].strip()
    except Exception as e:
        print(f"Error parseando malla: {e}")
        return ""

def clean_content(raw):
    guide = raw
    try:
        if raw.strip().startswith('{'):
            data = json.loads(raw)
            guide = data.get("answer", raw)
    except json.JSONDecodeError:
        pass
    for prefix in ["```markdown\n", "```markdown", "```\n", "```"]:
        if guide.startswith(prefix):
            guide = guide[len(prefix):]
    for suffix in ["```\n", "```"]:
        if guide.endswith(suffix):
            guide = guide[:-len(suffix)]
    return guide.strip()

# ── Per-subject processor ─────────────────────────────────────────────────────

async def process_subject(session, subject_code, subject_name, malla_path):
    print(f"\n{'='*55}")
    print(f"=== {subject_code} — {subject_name} ===")
    print(f"{'='*55}\n")

    try:
        # 1. Deep Research
        print("1. Lanzando Fast Research...")
        res = await session.call_tool("research_start", arguments={
            "query": f"Universidad: temario completo, teorías y conceptos de '{subject_name}' en español. Fundamentos académicos, aplicaciones prácticas y autores relevantes.",
            "source": "web",
            "mode": "fast",
            "title": f"Licecon Enrich: {subject_code} - {subject_name}"
        })
        data = json.loads(res.content[0].text)
        notebook_id = data.get("notebook_id")
        task_id     = data.get("task_id")
        if not notebook_id or not task_id:
            print("[-] Sin IDs válidos."); return False
        print(f"  Notebook: {notebook_id} | Task: {task_id}")

        # 2. Poll
        print("\n2. Esperando resultados...")
        await session.call_tool("research_status", arguments={
            "notebook_id": notebook_id,
            "task_id": task_id,
            "poll_interval": 10,
            "max_wait": 180
        })
        print("  Research OK")

        # 3. Import sources
        print("\n3. Importando fuentes...")
        await session.call_tool("research_import", arguments={
            "notebook_id": notebook_id,
            "task_id": task_id
        })

        # 3.5 Add syllabus
        syllabus = extract_syllabus(subject_code, malla_path)
        if syllabus:
            await session.call_tool("notebook_add_text", arguments={
                "notebook_id": notebook_id,
                "text": syllabus,
                "title": f"Temario Oficial — {subject_name}"
            })
            print("  Temario oficial añadido ✓")
        else:
            print("  [!] No se encontró temario para este código")

        # 4. Generate expanded study guide
        print("\n4. Generando Guía de Estudio expandida...")
        prompt = f"""Escribe una GUÍA DE ESTUDIO ACADÉMICA COMPLETA sobre {subject_name}.

INSTRUCCIONES CRÍTICAS:
- Sigue ESTRICTAMENTE el Temario Oficial de {subject_name} incluido en las fuentes.
- Desarrolla TODOS los títulos y subtítulos del temario (niveles 1, 2, 3 y 4), sin omitir ninguno.
- Para cada sub-epígrafe, escribe al menos 2 párrafos explicativos sustanciales.
- Incluye definiciones formales, teorías relevantes, ejemplos prácticos y autores clave.
- Usa lenguaje académico en español.

FORMATO MARKDOWN PURO:
- # para el título principal
- ## para temas principales (ej. 6.1. Título)
- ### para subtemas (ej. 6.1.1. Subtítulo)
- #### para sub-subtemas
- Párrafos normales para el contenido
- Listas con - para enumeraciones

SI OMITES ALGÚN SUBTEMA DEL TEMARIO, LA RESPUESTA SERÁ RECHAZADA.
Mínimo 3,000 palabras de contenido real."""

        qres = await session.call_tool("notebook_query", arguments={
            "notebook_id": notebook_id,
            "query": prompt,
            "timeout": 360.0
        })
        guide = clean_content(qres.content[0].text)

        if not guide or len(guide.strip()) < 200:
            print(f"[!] Contenido insuficiente para {subject_code}")
            return False

        # 5. Save
        out_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            'public', 'program', f'{subject_code.lower()}_extended.md'
        )
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(guide)

        print(f"\n[✔] {subject_code} guardado → {os.path.basename(out_path)} ({len(guide):,} chars)")
        return True

    except Exception as e:
        print(f"\n[!] Error en {subject_code}: {e}")
        return False

# ── Main batch runner ─────────────────────────────────────────────────────────

async def run_batch():
    data_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        'src', 'data.json'
    )
    with open(data_path, 'r', encoding='utf-8') as f:
        curriculum = json.load(f)

    subjects = curriculum.get('asignaturas', [])
    to_process = [s for s in subjects if s['codigo'] in THIN_MODULES]

    if not to_process:
        print("No se encontraron las asignaturas objetivo.")
        return

    malla_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
        'malla.md'
    )

    server_params = StdioServerParameters(
        command="notebooklm-mcp",
        args=["--query-timeout", "300"],
        env=None
    )

    print(f"\n{'='*55}")
    print(f"=== THIN MODULES ENRICHMENT — {len(to_process)} asignaturas ===")
    print(f"Módulos: {', '.join(THIN_MODULES)}")
    print(f"{'='*55}\n")

    results = {}
    for subject in to_process:
        try:
            async with stdio_client(server_params) as (read, write):
                async with ClientSession(read, write) as session:
                    await session.initialize()
                    ok = await process_subject(session, subject['codigo'], subject['nombre'], malla_path)
                    results[subject['codigo']] = '✔' if ok else '✗'
        except Exception as e:
            print(f"[!] Error de sesión para {subject['codigo']}: {e}")
            results[subject['codigo']] = '✗'

        await asyncio.sleep(5)

    print(f"\n{'='*55}")
    print("=== RESUMEN FINAL ===")
    for code, status in results.items():
        print(f"  {status} {code}")
    print(f"{'='*55}")

if __name__ == "__main__":
    asyncio.run(run_batch())
