import asyncio
import os
import json
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def process_subject(session, subject_code, subject_name):
    print(f"\n=======================================================")
    print(f"=== Procesando REPARACION: {subject_code} - {subject_name} ===")
    print(f"=======================================================\n")
    
    try:
        # 1. Start Deep Research
        print("1. Lanzando Deep Research (Búsqueda Académica Avanzada)...")
        research_query = f"University level curriculum, academic papers, and detailed theories regarding '{subject_name}' in Spanish. Focus on foundational principles, modern theories, and applications."
        
        research_start_res = await session.call_tool("research_start", arguments={
            "query": research_query,
            "source": "web",
            "mode": "fast", 
            "title": f"Licecon REPAIR: {subject_code} - {subject_name}"
        })
        
        response_text = research_start_res.content[0].text
        data = json.loads(response_text)
        notebook_id = data.get("notebook_id")
        task_id = data.get("task_id")

        if not notebook_id or not task_id:
             print("[-] Faltan IDs en la respuesta JSON.")
             return False

        print(f"  [+] Notebook ID: {notebook_id}")
        print(f"  [+] Task ID: {task_id}")
        
        # 2. Poll Research Status
        print("\n2. Esperando a que termine el Deep Research...")
        await session.call_tool("research_status", arguments={
            "notebook_id": notebook_id,
            "task_id": task_id,
            "poll_interval": 10,
            "max_wait": 180
        })
        
        # 3. Import Sources
        print("\n3. Importando fuentes descubiertas a la libreta...")
        await session.call_tool("research_import", arguments={
            "notebook_id": notebook_id,
            "task_id": task_id
        })
        
        # 4. Generate the Study Guide
        print("\n4. Generando Guía de Estudio (Synthesis)...")
        prompt = f"""Escribe una 'Guía de Estudio' exhaustiva, de nivel universitario, sobre {subject_name}. 
Básate estrictamente en las fuentes académicas que acabamos de investigar e importar a esta libreta.
Markdown puro, profesional, académico, con resumen al final."""

        query_res = await session.call_tool("notebook_query", arguments={
            "notebook_id": notebook_id,
            "query": prompt,
            "timeout": 180.0
        })
        
        raw_content = query_res.content[0].text
        guide_content = raw_content
        try:
            if raw_content.strip().startswith('{'):
                query_data = json.loads(raw_content)
                guide_content = query_data.get("answer", raw_content)
        except:
            pass
        
        # Simple cleanup
        if "```" in guide_content:
            lines = guide_content.split("\n")
            cleaned = []
            in_block = False
            for line in lines:
                if line.startswith("```"):
                    in_block = not in_block
                    continue
                cleaned.append(line)
            guide_content = "\n".join(cleaned)

        # 5. Save to File
        output_path = os.path.join(os.getcwd(), 'public', 'program', f'{subject_code.lower()}_extended.md')
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(guide_content.strip())
        
        print(f"\n[✔] Asignatura {subject_code} REPARADA. Guardado en {output_path}")
        return True

    except Exception as e:
        print(f"\n[!] Error crítico REPARANDO {subject_code}: {e}")
        return False

async def run_repair():
    subjects_to_repair = [
        {"codigo": "A3", "nombre": "Introducción a la economía"},
        {"codigo": "A4", "nombre": "Introducción al derecho"}
    ]

    server_params = StdioServerParameters(
        command="notebooklm-mcp",
        args=["--query-timeout", "300"],
        env=None
    )
    
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            for subject in subjects_to_repair:
                await process_subject(session, subject['codigo'], subject['nombre'])
                await asyncio.sleep(5)

if __name__ == "__main__":
    asyncio.run(run_repair())
