"""
batch_enrich_maestria.py
Enriches M1-M10 (Maestría en Ciencias Económicas) with full academic content.
Uses NotebookLM web research + query pipeline.
Output: m{N}_extended.md → processed by senior_ux_refactor.py into m{N}.md
"""
import asyncio
import os
import json
import subprocess
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# M modules with full academic context for better research queries
MAESTRIA_SUBJECTS = [
    ("M1",  "Fundamentos de la Economía",
             "macroeconomía microeconomía principios economía universidad maestría"),
    ("M2",  "Investigación en Ciencias Sociales",
             "metodología investigación cuantitativa cualitativa ciencias sociales"),
    ("M3",  "Herramientas del investigador",
             "econometría estadística software R Stata Python investigación económica"),
    ("M4",  "Economía de la empresa",
             "teoría de la empresa organización industrial estrategia empresarial"),
    ("M5",  "Economía conductual",
             "behavioral economics economía del comportamiento sesgos cognitivos Kahneman Thaler"),
    ("M6",  "Economía financiera",
             "finanzas teoría de carteras CAPM valoración activos mercados financieros maestría"),
    ("M7",  "Economía del comercio internacional",
             "comercio internacional ventaja comparativa modelos Heckscher-Ohlin política comercial"),
    ("M8",  "Economía industrial",
             "organización industrial competencia imperfecta oligopolio regulación antimonopolio"),
    ("M9",  "Instrumentos y mercados financieros",
             "derivados financieros opciones futuros swaps mercados de capitales"),
    ("M10", "Innovación e iniciativa emprendedora",
             "innovación emprendimiento ecosistema startup economía innovación Schumpeter"),
]


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


async def process_subject(session, code, name, keywords):
    print(f"\n{'='*57}")
    print(f"=== {code} — {name} ===")
    print(f"{'='*57}\n")

    try:
        # 1. Deep Research
        print("1. Lanzando Fast Research (web académico)...")
        query = (
            f"Maestría en Ciencias Económicas: temario completo y contenido académico de "
            f"'{name}'. {keywords}. Nivel posgrado universitario, en español."
        )
        res = await session.call_tool("research_start", arguments={
            "query": query,
            "source": "web",
            "mode": "fast",
            "title": f"MCE: {code} - {name}"
        })
        data = json.loads(res.content[0].text)
        notebook_id = data.get("notebook_id")
        task_id     = data.get("task_id")
        if not notebook_id or not task_id:
            print("[-] Sin IDs válidos."); return False
        print(f"  Notebook: {notebook_id} | Task: {task_id}")

        # 2. Poll
        print("\n2. Esperando investigación...")
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

        # 4. Generate full academic guide
        print("\n4. Generando Guía Académica completa...")
        prompt = f"""Eres un profesor experto de la Maestría en Ciencias Económicas.
Escribe una GUÍA DE ESTUDIO ACADÉMICA COMPLETA para el módulo "{name}" (código {code}).

ESTRUCTURA OBLIGATORIA:
# {code}: {name}
## [Tema 1 del módulo con número]
### [Subtema 1.1]
[Contenido denso: definiciones, teorías, autores, ecuaciones si aplica]
### [Subtema 1.2]
[...]
## [Tema 2 del módulo]
[Continua...]
## Puntos Clave
[5 puntos clave conclusivos]

REQUISITOS:
- Nivel de posgrado (maestría), rigor académico alto
- Mínimo 8 temas principales (##) con sus subtemas (### y ####)
- Cada tema: mínimo 3 párrafos de 100+ palabras con contenido sustancial
- Incluye autores clave, teorías formales, modelos, aplicaciones prácticas
- Cita modelos matemáticos o estadísticos donde corresponda
- Menciona debates académicos actuales y bibliografía relevante
- Idioma: español académico
- Formato: Markdown puro, sin bloques de código json
- Mínimo 4,000 palabras de contenido real

SI EL CONTENIDO ES SUPERFICIAL O MENOR A 2,000 PALABRAS, SERÁ RECHAZADO."""

        qres = await session.call_tool("notebook_query", arguments={
            "notebook_id": notebook_id,
            "query": prompt,
            "timeout": 420.0
        })
        guide = clean_content(qres.content[0].text)

        if not guide or len(guide.strip()) < 500:
            print(f"[!] Contenido insuficiente para {code}")
            return False

        # 5. Save _extended.md
        program_dir = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            'public', 'program'
        )
        ext_path = os.path.join(program_dir, f'{code.lower()}_extended.md')
        with open(ext_path, 'w', encoding='utf-8') as f:
            f.write(guide)
        print(f"  Guardado: {os.path.basename(ext_path)} ({len(guide):,} chars)")

        # 6. Apply Zero-Noise v9 formatter
        print("\n5. Aplicando Zero-Noise v9...")
        script = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'senior_ux_refactor.py')
        r = subprocess.run(
            ['python3', script, f'{code.lower()}_extended.md'],
            capture_output=True, text=True,
            cwd=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        )
        if r.returncode == 0:
            print(f"  {r.stdout.strip()}")
        else:
            print(f"  [!] v9 error: {r.stderr[:100]}")

        print(f"\n[✔] {code} completado ({len(guide):,} chars)")
        return True

    except Exception as e:
        print(f"\n[!] Error en {code}: {e}")
        return False


async def run_batch():
    server_params = StdioServerParameters(
        command="notebooklm-mcp",
        args=["--query-timeout", "300"],
        env=None
    )

    print(f"\n{'='*57}")
    print(f"=== MAESTRÍA EN CIENCIAS ECONÓMICAS — {len(MAESTRIA_SUBJECTS)} módulos ===")
    print(f"{'='*57}\n")

    results = {}
    for code, name, keywords in MAESTRIA_SUBJECTS:
        try:
            async with stdio_client(server_params) as (read, write):
                async with ClientSession(read, write) as session:
                    await session.initialize()
                    ok = await process_subject(session, code, name, keywords)
                    results[code] = '✔' if ok else '✗'
        except Exception as e:
            print(f"[!] Error de sesión para {code}: {e}")
            results[code] = '✗'
        await asyncio.sleep(5)

    print(f"\n{'='*57}")
    print("=== RESUMEN FINAL ===")
    done = sum(1 for v in results.values() if v == '✔')
    for code, status in results.items():
        print(f"  {status} {code}")
    print(f"\n{done}/{len(results)} módulos completados")
    print(f"{'='*57}")


if __name__ == "__main__":
    asyncio.run(run_batch())
