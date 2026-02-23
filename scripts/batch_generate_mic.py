import asyncio
import os
import sys
import re
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# We will use the existing notebook ID used for Microeconomics, assuming it already has the PDF loaded.
# It was used in generate_master_a10.py
NOTEBOOK_ID = "39635117-afc1-49fa-85c9-d18aefdd3f63"

MODULES = [
    {
        "id": "mic1",
        "title": "Teoría del Consumidor y Demanda Individual",
        "topics": "Preferencias, restricción presupuestaria, curva de indiferencia, función de utilidad, tipos de axiomas, derivación de la curva de demanda individual, variaciones en cantidad y demanda."
    },
    {
        "id": "mic2",
        "title": "Elección Intertemporal e Incertidumbre",
        "topics": "Preferencias intemporales, relación marginal de preferencia temporal, tipo de interés, valor descontado, elección bajo incertidumbre, riesgo, valor esperado, utilidad esperada, aversión al riesgo, prima de riesgo."
    },
    {
        "id": "mic3",
        "title": "Teoría de Juegos Estáticos y Dinámicos",
        "topics": "Juegos estáticos en forma normal, juegos dinámicos en forma extensiva, estrategias, inducción hacia atrás, equilibrio de Nash perfecto en sub-juegos, racionalidad secuencial, duopolio de Stackelberg."
    },
    {
        "id": "mic4",
        "title": "Monopolio, Bienestar y Poder de Mercado",
        "topics": "Concepto de monopolio, bienestar y valoración, excedente del consumidor y productor, poder de mercado, ineficiencia asignativa, fallos de mercado, pérdida irrecuperable de eficiencia."
    },
    {
        "id": "mic5",
        "title": "Competencia Monopolística y Diferenciación de Producto",
        "topics": "Características del mercado de competencia monopolística, libre entrada y salida, equilibrio a corto y largo plazo, exceso de capacidad, diferenciación de producto, comparación con competencia perfecta."
    },
    {
        "id": "mic6",
        "title": "Modelos de Oligopolio",
        "topics": "Características del oligopolio, interdependencia estratégica, oligopolio diferenciado y concentrado, barreras de ingreso, colusión, cárteles, Cournot, Stackelberg."
    },
    {
        "id": "mic7",
        "title": "El Sector Público y la Regulación",
        "topics": "La intervención pública en oligopolios y mercados concentrados, regulación antimonopolio, políticas de competencia, empresas públicas frente a empresas privadas en oligopolio, barreras tecnológicas e innovación regulada."
    },
    {
        "id": "mic8",
        "title": "Externalidades y Bienes Públicos",
        "topics": "La existencia de bienes públicos puros (no rivales, no excluyentes), free riders, externalidades positivas y negativas, costes sociales vs privados, impuestos pigouvianos, teorema de Coase, política medioambiental."
    },
    {
        "id": "mic9",
        "title": "Información Asimétrica",
        "topics": "Información asimétrica en mercados, selección adversa, riesgo moral, señalización, cribado, teoría de la información asimétrica y sus efectos en precios y equilibrios."
    },
    {
        "id": "mic10",
        "title": "Equilibrio General y Eficiencia",
        "topics": "La economía abierta y el equilibrio competitivo, eficiencia de Pareto, precios máximos y mínimos, efecto de impuestos indirectos, síntesis de tipología de fallos y diseño de mercados."
    }
]

def format_master_content(content, title, code):
    # Premium HTML wrapper
    html_wrapper = f"""<div class="max-w-4xl mx-auto px-4 py-14 md:px-12 font-sans text-slate-200">

<!-- HERO -->
<header class="mb-24 relative">
    <div class="absolute inset-0 bg-gradient-to-r from-blue-500/10 to-indigo-500/10 blur-3xl -z-10 rounded-[3rem]"></div>
    <div class="flex items-center gap-4 mb-8">
        <div class="w-8 h-0.5 bg-blue-500 rounded-full"></div>
        <span class="text-blue-400 font-black text-[10px] uppercase tracking-[0.4em]">MIC MASTER SERIES</span>
    </div>
    <h1 class="text-5xl md:text-7xl font-black text-white tracking-tighter leading-none mb-8">
        {code.upper()}
    </h1>
    <h2 class="text-3xl md:text-4xl font-bold bg-gradient-to-r from-slate-200 to-slate-400 bg-clip-text text-transparent mb-8">
        {title}
    </h2>
    <div class="flex flex-wrap gap-3">
        <span class="bg-blue-500/15 text-blue-300 border border-blue-500/25 px-4 py-1 rounded-full text-[10px] font-black uppercase tracking-[0.3em]">Microeconomía Avanzada</span>
        <span class="bg-white/5 text-slate-400 border border-white/10 px-4 py-1 rounded-full text-[10px] font-black uppercase tracking-[0.3em]">Tope de Gama</span>
    </div>
</header>

<div class="prose prose-invert max-w-none 
    prose-headings:font-black prose-headings:tracking-tight 
    prose-h2:text-3xl prose-h2:bg-gradient-to-r prose-h2:from-blue-300 prose-h2:to-indigo-400 prose-h2:bg-clip-text prose-h2:text-transparent prose-h2:mt-16 prose-h2:mb-8 
    prose-h3:text-2xl prose-h3:text-slate-200 prose-h3:mt-12 prose-h3:mb-6
    prose-p:text-slate-300 prose-p:text-lg prose-p:leading-relaxed prose-p:mb-6
    prose-ul:text-slate-300 prose-ul:text-lg prose-ul:space-y-3 prose-li:marker:text-blue-500
    prose-strong:text-blue-300 prose-strong:font-bold
    prose-a:text-blue-400 prose-a:no-underline hover:prose-a:text-blue-300 hover:prose-a:underline
    prose-blockquote:border-l-4 prose-blockquote:border-blue-500 prose-blockquote:bg-blue-500/5 prose-blockquote:py-2 prose-blockquote:px-6 prose-blockquote:rounded-r-2xl prose-blockquote:text-slate-300 prose-blockquote:not-italic
    prose-code:text-indigo-300 prose-code:bg-indigo-500/10 prose-code:px-2 prose-code:py-0.5 prose-code:rounded-md prose-code:before:content-none prose-code:after:content-none font-mono">
{content}
</div>

<footer class="mt-24 pt-8 border-t border-white/10 text-center text-slate-500 text-sm font-medium">
    &copy; 2026 Tech Institute | Master en Microeconomía | Generación O-3
</footer>
</div>"""
    return html_wrapper

async def batch_generate_mic():
    server_params = StdioServerParameters(
        command="notebooklm-mcp",
        args=["--query-timeout", "600"],
        env=None
    )
    
    output_dir = "/Users/machd/Desktop/licecon/web-portal/public/program"
    os.makedirs(output_dir, exist_ok=True)
    
    print("\nIniciando sesión MCP con NotebookLM...")
    try:
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                
                for mod in MODULES:
                    mod_id = mod["id"]
                    mod_title = mod["title"]
                    mod_topics = mod["topics"]
                    
                    output_path = os.path.join(output_dir, f"{mod_id}.md")
                    
                    if os.path.exists(output_path):
                        print(f"[-] Saltando {mod_id.upper()} porque ya existe el archivo.")
                        continue
                        
                    print(f"\nGenerando Documento MASTER para {mod_id.upper()}: {mod_title}...")
                    
                    prompt = f"""Eres el Catedrático Principal de Economía. El usuario tiene un libro de nivel postgrado/master de Microeconomía subido a esta libreta.

Debes generar el Módulo Master '{mod_title}' de la asignatura Master en Microeconomía.
Cubre EXHAUSTIVAMENTE los siguientes subtemas, basándote en el contenido matemático y analítico del libro o fuentes subidas:
Temas a cubrir: {mod_topics}

Requisitos de la generación:
1. Explica los fundamentos teóricos con rigor académico (nivel Maestría de Economía). Transmite intuición económica.
2. Formato Markdown puro, usando jerarquía de títulos (##, ###).
3. Usa bloques KaTeX `$$ ... $$` o `$ ... $` para presentar fórmulas, funciones de demanda, restricciones presupuestarias y condiciones de equilibrio. Asegúrate de escapar caracteres especiales si es necesario, y NO USES subguiones que puedan romper el parsing Markdown. (Trata de estructurar las matemáticas claramente).
4. Longitud de al menos 1500 a 2500 palabras (profundiza al máximo en demostraciones y conceptos avanzados).
5. Incluye una sección final "Aplicaciones avanzadas - Perspectiva Master" que sintetiza modelos o ejemplos prácticos.
No incluyas el titulo principal del modulo usando h1 (#) en tu respuesta, arranca directamente con los H2 (##).
"""
                    print(f"Consultando a NotebookLM para {mod_id} (puede tardar un par de minutos)...")
                    query_res = await session.call_tool("notebook_query", arguments={
                        "notebook_id": NOTEBOOK_ID,
                        "query": prompt,
                        "timeout": 600.0
                    })
                    
                    raw_content = query_res.content[0].text
                    
                    # Limpiar Markdown wrapper
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
                    
                    final_html = format_master_content(guide_content, mod_title, mod_id)
                    
                    with open(output_path, 'w', encoding='utf-8') as f:
                        f.write(final_html)
                    
                    print(f"[✔] Generado {mod_id.upper()} exitosamente.")
                    
                    # Sleep to avoid rate limits
                    print("Esperando 10 segundos antes del siguiente módulo...")
                    await asyncio.sleep(10)
                    
    except Exception as e:
        print(f"\n[!] Error: {e}")

if __name__ == "__main__":
    asyncio.run(batch_generate_mic())
