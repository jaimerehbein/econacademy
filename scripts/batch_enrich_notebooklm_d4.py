import asyncio
import os
import json
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

def extract_syllabus(subject_code, malla_path):
    if not subject_code.startswith('A'):
        return ""
    try:
        num = int(subject_code[1:])
        asignatura_str = f"Asignatura {num}."
        next_asignatura_str = f"Asignatura {num+1}."
        
        with open(malla_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        start_idx = content.find(asignatura_str)
        if start_idx == -1:
            return ""
            
        end_idx = content.find(next_asignatura_str, start_idx)
        if end_idx == -1:
            end_idx = len(content)
            
        return content[start_idx:end_idx].strip()
    except Exception as e:
        print(f"Error parseando malla: {e}")
        return ""

async def process_subject(session, subject_code, subject_name):
    print(f"\n=======================================================")
    print(f"=== Procesando: {subject_code} - {subject_name} ===")
    print(f"=======================================================\n")
    
    try:
        # 1. Start Deep Research
        print("1. Lanzando Deep Research (Búsqueda Académica Avanzada)...")
        research_query = f"University level curriculum, academic papers, and detailed theories regarding '{subject_name}' in Spanish. Focus on foundational principles, modern theories, and applications."
        
        research_start_res = await session.call_tool("research_start", arguments={
            "query": research_query,
            "source": "web",
            "mode": "fast", 
            "title": f"Licecon: {subject_code} - {subject_name}"
        })
        
        response_text = research_start_res.content[0].text
        
        try:
            data = json.loads(response_text)
            notebook_id = data.get("notebook_id")
            task_id = data.get("task_id")
        except json.JSONDecodeError:
            print("[-] No se pudo parsear el JSON de la respuesta de research_start.")
            return False

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
        print("Research completado!")
        
        # 3. Import Sources
        print("\n3. Importando fuentes descubiertas a la libreta...")
        await session.call_tool("research_import", arguments={
            "notebook_id": notebook_id,
            "task_id": task_id
        })
        print("Fuentes Importadas.")
        
        # 3.5 ADD SYLLABUS AS A SOURCE
        print("Añadiendo Temario Oficial como fuente a la libreta...")
        malla_path = os.path.join(os.path.dirname(os.getcwd()), 'malla.md')
        syllabus = extract_syllabus(subject_code, malla_path)
        
        if syllabus:
            await session.call_tool("notebook_add_text", arguments={
                "notebook_id": notebook_id,
                "text": syllabus,
                "title": f"Temario Oficial de {subject_name}"
            })
            print("Temario añadido como fuente exitosamente.")
        else:
            print("No se encontró temario específico.")
            
        # 4. Generate the Study Guide
        print("\n4. Generando Guía de Estudio (Synthesis) con temario...")
        
        prompt = f"""Escribe una 'Guía de Estudio' académica sobre {subject_name}. 
Básate estrictamente en las fuentes de esta libreta.
ATENCIÓN CRÍTICA: Entre las fuentes se encuentra el "Temario Oficial de {subject_name}".
Es OBLIGATORIO que tu respuesta contenga ABSOLUTAMENTE TODOS los títulos y subtítulos exactos de ese Temario Oficial, desarrollando contenido para cada uno de ellos, sin omitir ni resumir niveles. No puedes dejar ningún punto (ej. 1.1.1, 1.1.2) por fuera.

Formato requerido:
- Usa Markdown puro sin encapsular en bloques de código json.
- Título principal con #.
- Usa ## para los temas principales (ej. 31.1) y ### o #### para todos los subtemas exactos del temario.
- Desarrolla explicaciones sustanciales bajo cada uno de los sub-epígrafes.
- Al final, incluye un resumen de 3 puntos clave.
SI OMITES ALGÚN SUBTEMA DEL TEMARIO, LA RESPUESTA SERÁ RECHAZADA."""

        query_res = await session.call_tool("notebook_query", arguments={
            "notebook_id": notebook_id,
            "query": prompt,
            "timeout": 360.0 # Increased timeout for large generations
        })
        
        raw_content = query_res.content[0].text
        
        # NotebookLM query either returns a JSON string, or just the raw markdown depending on the model backend
        guide_content = raw_content
        try:
            # Try to parse it as JSON first
            if raw_content.strip().startswith('{'):
                query_data = json.loads(raw_content)
                guide_content = query_data.get("answer", raw_content)
        except json.JSONDecodeError:
            # If it fails to parse, it's likely just the raw markdown string already!
            guide_content = raw_content
        
        # Clean up any potential markdown code blocks if the AI returned it wrapped in ```markdown
        if guide_content.startswith("```markdown\n"):
            guide_content = guide_content[12:]
        elif guide_content.startswith("```markdown"):
             guide_content = guide_content[11:]
        elif guide_content.startswith("```\n"):
            guide_content = guide_content[4:]
        elif guide_content.startswith("```"):
            guide_content = guide_content[3:]
            
        if guide_content.endswith("```\n"):
            guide_content = guide_content[:-4]
        elif guide_content.endswith("```"):
            guide_content = guide_content[:-3]
            
        if not guide_content or len(guide_content.strip()) < 100:
            print(f"\n[!] Advertencia: La guía generada para {subject_code} parece estar vacía o es demasiado corta.")
            print(f"--- RAW CONTENT RECIBIDO ---")
            print(raw_content)
            print(f"----------------------------")
            return False
            
        # 5. Save to File
        output_path = os.path.join(os.getcwd(), 'public', 'program', f'{subject_code.lower()}_extended.md')
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(guide_content.strip())
        
        print(f"\n[✔] Asignatura {subject_code} procesada exitosamente. Guardado en {output_path}")
        return True

    except Exception as e:
        print(f"\n[!] Error crítico procesando {subject_code}: {e}")
        return False

async def run_batch():
    # Read the data.json
    data_path = os.path.join(os.getcwd(), 'src', 'data.json')
    with open(data_path, 'r', encoding='utf-8') as f:
        curriculum = json.load(f)
        
    subjects = curriculum.get('asignaturas', [])
    
    # Processing A31 through A40 for the next batch
    target_codes = ["A31", "A32", "A33", "A34", "A35", "A36", "A37", "A38", "A39", "A40"]
    subjects_to_process = [s for s in subjects if s['codigo'] in target_codes]
    
    if not subjects_to_process:
        print("No se encontraron las asignaturas objetivo.")
        return

    server_params = StdioServerParameters(
        command="notebooklm-mcp",
        args=["--query-timeout", "300"],
        env=None
    )
    
    print(f"=== Iniciando Procesamiento por Lotes ({len(subjects_to_process)} asignaturas) ===\n")
    
    for subject in subjects_to_process:
        print(f"\n[+] Iniciando sesión para {subject['codigo']}...")
        try:
            async with stdio_client(server_params) as (read, write):
                async with ClientSession(read, write) as session:
                    await session.initialize()
                    success = await process_subject(session, subject['codigo'], subject['nombre'])
                    if not success:
                        print(f"[-] Fallo reportado para {subject['codigo']}.")
        except Exception as e:
            print(f"[!] Error de conexión/sesión para {subject['codigo']}: {e}")
            
        # Small delay between subjects to avoid hammering the API
        await asyncio.sleep(5)
                
    print("\n=== Procesamiento por Lotes Finalizado ===")

if __name__ == "__main__":
    asyncio.run(run_batch())
