import asyncio
import os
import json
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

import argparse

async def run_notebooklm_pipeline(subject_code, subject_name):
    server_params = StdioServerParameters(
        command="notebooklm-mcp",
        args=[],
        env=None
    )
    
    print(f"=== Iniciando Pipeline de NotebookLM para: {subject_code} - {subject_name} ===\n")
    
    try:
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                
                # 1. Start Deep Research to find sources
                print("1. Lanzando Deep Research (Búsqueda Académica Avanzada)...")
                research_query = f"University level curriculum, academic papers, and detailed theories regarding '{subject_name}' in Spanish. Focus on foundational principles, modern theories, and applications."
                
                research_start_res = await session.call_tool("research_start", arguments={
                    "query": research_query,
                    "source": "web",
                    "mode": "fast",
                    "title": f"Licecon: {subject_name}"
                })
                
                print("Research Start Response:", research_start_res)
                
                # Extract notebook_id and task_id
                response_text = research_start_res.content[0].text
                
                try:
                    data = json.loads(response_text)
                    notebook_id = data.get("notebook_id")
                    task_id = data.get("task_id")
                except json.JSONDecodeError:
                    print("[-] No se pudo parsear el JSON de la respuesta.")
                    return

                if not notebook_id or not task_id:
                     print("[-] Faltan IDs en la respuesta JSON.")
                     return

                print(f"  [+] Notebook ID: {notebook_id}")
                print(f"  [+] Task ID: {task_id}")
                
                # 2. Poll Research Status
                print("\n2. Esperando a que termine el Deep Research...")
                status_res = await session.call_tool("research_status", arguments={
                    "notebook_id": notebook_id,
                    "task_id": task_id,
                    "poll_interval": 10,
                    "max_wait": 180
                })
                print("Research completado!\n")
                
                # 3. Import Sources
                print("3. Importando fuentes descubiertas a la libreta...")
                import_res = await session.call_tool("research_import", arguments={
                    "notebook_id": notebook_id,
                    "task_id": task_id
                })
                print("Fuentes Importadas.")
                
                # 4. Generate the Study Guide
                print("\n4. Generando Guía de Estudio (Synthesis)...")
                prompt = f"""Escribe una 'Guía de Estudio' exhaustiva, de nivel universitario, sobre {subject_name}. 
Básate estrictamente en las fuentes académicas que acabamos de investigar e importar a esta libreta.
Formato requerido:
- Usa Markdown puro.
- Título principal con #
- Incluye secciones como 'Principios Fundamentales', 'Principales Teorías', 'Aplicaciones Modernas', etc.
- Sé extremadamente profesional, objetivo y académico. Evita lenguaje de marketing.
- Usa listas numeradas y viñetas para desglosar conceptos complejos.
- Al final, incluye un resumen de 3 puntos clave."""

                query_res = await session.call_tool("notebook_query", arguments={
                    "notebook_id": notebook_id,
                    "query": prompt,
                    "timeout": 180.0
                })
                
                raw_content = query_res.content[0].text
                try:
                    query_data = json.loads(raw_content)
                    guide_content = query_data.get("answer", raw_content)
                except json.JSONDecodeError:
                    guide_content = raw_content
                
                print("\n=== GUÍA GENERADA ===\n")
                print(guide_content[:500] + "...\n[CONTINÚA]")
                
                # 5. Save to File
                output_path = os.path.join(os.getcwd(), 'public', 'program', f'{subject_code.lower()}_extended.md')
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(guide_content)
                
                print(f"\n[✔] Exitoso. Contenido guardado en {output_path}")

    except Exception as e:
        print(f"\n[!] Error crítico en el pipeline: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Enriquecimiento de asignaturas con NotebookLM')
    parser.add_argument('--code', type=str, default='A1', help='Código de la asignatura (ej: A1)')
    parser.add_argument('--name', type=str, default='Administración de empresas', help='Nombre de la asignatura')
    args = parser.parse_args()
    
    asyncio.run(run_notebooklm_pipeline(args.code, args.name))

