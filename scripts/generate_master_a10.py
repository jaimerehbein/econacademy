import asyncio
import os
import sys
from PyPDF2 import PdfReader
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def generate_master_a10():
    notebook_id = "39635117-afc1-49fa-85c9-d18aefdd3f63"
    pdf_path = "/Users/machd/Desktop/licecon/Microeconomía.pdf"
    
    # 1. Extract text from the PDF since NotebookLM MCP doesn't take local file uploads directly yet
    print(f"Buscando PDF en: {pdf_path}")
    if not os.path.exists(pdf_path):
        print("El archivo PDF no existe.")
        return
        
    print("Extrayendo texto del PDF (esto puede tomar un minuto)...")
    reader = PdfReader(pdf_path)
    full_text = ""
    for page in reader.pages:
        text = page.extract_text()
        if text:
            full_text += text + "\n"
            
    # We might need to split it if it's too massive, but let's try the whole text first.
    # NotebookLM handles very large contexts.
    text_length = len(full_text)
    print(f"Texto extraído: {text_length} caracteres.")
    
    server_params = StdioServerParameters(
        command="notebooklm-mcp",
        args=["--query-timeout", "600"],
        env=None
    )
    
    print("\nIniciando sesión MCP pCon NotebookLM...")
    try:
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                
                # 2. Add as text source
                print("Añadiendo el contenido del libro como fuente a la libreta A10...")
                add_res = await session.call_tool("notebook_add_text", arguments={
                    "notebook_id": notebook_id,
                    "text": full_text,
                    "title": "Libro Master de Microeconomía (PDF)"
                })
                print("Libro añadido como fuente exitosamente.")
                
                # 3. Generate Master Content
                print("\nGenerando Documento Master para A10 basado EXCLUSIVAMENTE en el temario y el nuevo libro...")
                
                prompt = """Eres el Catedrático Principal de Economía. El usuario ha subido un nuevo libro completo de Microeconomía que servirá como la "biblia" para esta asignatura.
                
Genera un 'Documento MASTER' (A10_master.md) que desarrolle en extrema profundidad teórica y matemática CADA PUNTO Y SUBPUNTO del Temario Oficial de la Asignatura 10 (Microeconomía) usando PRINCIPALMENTE el nuevo "Libro Master de Microeconomía" como fuente de consulta.

Requisitos de generación:
1. DEBES cubrir t-o-d-o-s los temas del Temario Oficial.
2. Formato Markdown puro, adecuado para un tema oscuro premium.
3. Este es el documento "Tope de Gama", así que no escatimes en detalles, gráficos ASCII si puedes, o desarrollo exhaustivo con bloques de KaTeX para las fórmulas de demanda, costos marginales, monopolio, etc.
4. Extensión esperada: Mínimo 4000-5000 palabras. Desarrolla como si fuera un capítulo de libro definitivo.
5. No inventes, extrae los conceptos avanzados, ejemplos y ecuaciones estructurales DIRECTAMENTE de la fuente recién subida.
"""

                print("Consultando a NotebookLM (Esperando generación densa, puede tardar varios minutos)...")
                query_res = await session.call_tool("notebook_query", arguments={
                    "notebook_id": notebook_id,
                    "query": prompt,
                    "timeout": 600.0
                })
                
                raw_content = query_res.content[0].text
                
                # Limpiar Markdown
                guide_content = raw_content
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
                    
                output_path = "/Users/machd/Desktop/licecon/web-portal/public/program/a10_master.md"
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(guide_content.strip())
                
                print(f"\n[✔] Master para A10 procesado exitosamente. Guardado en {output_path}")

    except Exception as e:
        print(f"\n[!] Error crítico: {e}")

if __name__ == "__main__":
    asyncio.run(generate_master_a10())
