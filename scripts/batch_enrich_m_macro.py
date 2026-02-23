import asyncio
import os
import sys
import json
import subprocess
import subprocess
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

MACRO_SUBJECTS = [
    # ("MAC1", "La ciencia de la macroeconomía", 
    #  "macroeconomía Mankiw 8va edición capítulo 1 ciencia económica modelos macroeconómicos"),
    # ("MAC2", "Los datos macroeconómicos", 
    #  "datos macroeconómicos PIB inflación desempleo Mankiw capítulo 2 medición económica"),
    ("MAC3", "La renta nacional: de dónde viene y adónde va", 
     "renta nacional distribución Mankiw capítulo 3 factores de producción función de producción demanda bienes y servicios"),
    # ("MAC4", "El sistema monetario: qué es y cómo funciona", 
    #  "sistema monetario dinero banco central oferta monetaria Mankiw capítulo 4 creación de dinero reservas"),
    # ("MAC5", "La inflación: sus causas, sus efectos y sus costes sociales", 
    #  "inflación teoría cuantitativa del dinero señoraje efecto Fisher costes sociales Mankiw capítulo 5 hiperinflación"),
    # ("MAC6", "La economía abierta", 
    #  "economía abierta flujos internacionales capitales bienes tipos de cambio Mankiw capítulo 6 paridad poder adquisitivo"),
    # ("MAC7", "El paro", 
    #  "desempleo paro natural friccional estructural rigidez salarial Mankiw capítulo 7 búsqueda empleo salarios de eficiencia"),
    # ("MAC8", "El crecimiento económico I: la acumulación de capital y el crecimiento de la población", 
    #  "crecimiento económico modelo de Solow acumulación capital estado estacionario regla de oro crecimiento poblacional Mankiw capítulo 8"),
    # ("MAC9", "El crecimiento económico II: la tecnología, el análisis empírico y la política económica", 
    #  "crecimiento económico modelo de Solow progreso tecnológico empírico política crecimiento endógeno Mankiw capítulo 9"),
    # ("MAC10", "Introducción a las fluctuaciones económicas y la Demanda Agregada", 
    #  "fluctuaciones económicas ciclo económico corto plazo demanda agregada oferta agregada políticas de estabilización Mankiw capítulo 10"),
]

def clean_content(raw):
    guide = raw
    try:
        import json
        if raw.strip().startswith('{'):
            data = json.loads(raw)
            guide = data.get("answer", raw)
    except Exception:
        pass
    for prefix in ["```markdown\\n", "```markdown", "```\\n", "```"]:
        if guide.startswith(prefix):
            guide = guide[len(prefix):]
    for suffix in ["```\\n", "```"]:
        if guide.endswith(suffix):
            guide = guide[:-len(suffix)]
    return guide.strip()

async def process_subject(session, code, name, keywords):
    print(f"\\n{'='*57}")
    print(f"=== {code} — {name} ===")
    print(f"{'='*57}\\n")
    
    # 1. Fast Research
    print("1. Lanzando Fast Research (web académico)...")
    res = await session.call_tool("research_start", arguments={
        "query": f"Mankiw Macroeconomía 8va edición: temario y contenido de '{name}'. {keywords} universidad master",
        "source": "web",
        "mode": "fast"
    })
    
    notebook_id = None
    task_id = None
    
    try:
        data = json.loads(res.content[0].text)
        notebook_id = data.get("notebook_id")
        task_id = data.get("task_id")
    except Exception:
        pass
                
    if not notebook_id or not task_id:
        print("[!] Error: No se pudo iniciar el research.", res.content)
        return False
        
    print(f"  Notebook: {notebook_id} | Task: {task_id}")
    
    # 2. Wait
    print("\\n2. Esperando investigación...")
    await session.call_tool("research_status", arguments={
        "notebook_id": notebook_id,
        "task_id": task_id,
        "max_wait": 300,
        "poll_interval": 10
    })
    print("  Research OK")
    
    # 3. Import
    print("\\n3. Importando fuentes...")
    await session.call_tool("research_import", arguments={
        "notebook_id": notebook_id,
        "task_id": task_id
    })
    
    # 4. Generate Guide
    print("\\n4. Generando Guía Académica completa...")
    
    prompt = f"""Eres un profesor experto del Master en Macroeconomía, especializado en la obra de N. Gregory Mankiw (8va edición).
Escribe una GUÍA DE ESTUDIO ACADÉMICA COMPLETA para el módulo "{name}" (código {code}).

INSTRUCCIONES ESTRICTAS:
1. BASADO EN MANKIW: El contenido debe reflejar fielmente los conceptos, modelos y estructura del capítulo "{name}" del libro Macroeconomía de Mankiw.
2. EXTENSIÓN: Obligatorio un mínimo de 4000 palabras de contenido denso. Desarrolla a fondo las fórmulas, gráficos teóricos, derivaciones matemáticas y explicaciones conceptuales avanzadas.
3. ESTRUCTURA: Usa Markdown con encabezados (##, ###), viñetas, y bloques matemáticos LaTeX ($ para inline, $$ para bloques).
4. TONO: Académico de posgrado.
5. NO uses etiquetas HTML complejas, solo Markdown estándar. No incluyas `<div class="card">` ni nada parecido, será procesado por otro script luego.

DESARROLLA LOS SIGUIENTES TEMAS que corresponden a este módulo en la obra de Mankiw:
- Conceptos fundamentales, definiciones precisas y variables clave.
- Modelos matemáticos paso a paso (ej. Modelo IS-LM, Solow, según corresponda al módulo).
- Implicaciones de las políticas macroeconómicas.
- Casos prácticos y evidencia empírica discutida en el texto de Mankiw.
"""

    qres = await session.call_tool("notebook_query", arguments={
        "notebook_id": notebook_id,
        "query": prompt,
        "timeout": 420.0
    })
    
    guide = clean_content(qres.content[0].text)
    
    out_path = f"/Users/machd/Desktop/licecon/web-portal/public/program/{code.lower()}_extended.md"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(guide)
        
    print(f"\\n  Guardado: {os.path.basename(out_path)} ({len(guide):,} chars)")
    
    # 5. Apply ZeroNoise
    print("\\n5. Aplicando Zero-Noise v9...")
    subprocess.run(["python3", "scripts/senior_ux_refactor.py", os.path.basename(out_path)], cwd="/Users/machd/Desktop/licecon/web-portal")
    
    print(f"\\n[✔] {code} completado ({len(guide):,} chars)")
    return True

async def run_batch():
    server_params = StdioServerParameters(
        command="notebooklm-mcp",
        args=["--query-timeout", "420"],
        env=None
    )
    
    print(f"\\n{'='*57}")
    print(f"=== MASTER EN MACROECONOMÍA — {len(MACRO_SUBJECTS)} módulos ===")
    print(f"{'='*57}\\n")
    
    results = {}
    
    for code, name, keywords in MACRO_SUBJECTS:
        try:
            async with stdio_client(server_params) as (read, write):
                async with ClientSession(read, write) as session:
                    await session.initialize()
                    ok = await process_subject(session, code, name, keywords)
                    results[code] = '✔' if ok else '✗'
        except Exception as e:
            print(f"[!] Error de sesión para {code}: {e}")
            results[code] = '✗'
            
        # Cooldown temporal
        await asyncio.sleep(5)
        
    print(f"\\n\\n{'='*57}")
    print("=== RESUMEN FINAL ===")
    for c, r in results.items():
        print(f"  {r} {c}")
    print(f"\\n{len([r for r in results.values() if r == '✔'])}/{len(MACRO_SUBJECTS)} módulos completados")
    print(f"{'='*57}")

if __name__ == "__main__":
    asyncio.run(run_batch())
