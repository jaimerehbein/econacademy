import re

filepath = '/Users/machd/Desktop/licecon/web-portal/public/program/a10_master.md'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the title and subtitle from the markdown as we'll put it in the HTML header
content = re.sub(r'# A10_master.md: Tratado Avanzado de Microeconomía\n### Asignatura 10: Microeconomía Superior\n\*\*Autoridad Académica:\*\*.*\n\*\*Fuente Base:\*\*.*\n\n---\n', '', content)

# Wrap the rest of the content in the premium HTML structure
html_wrapper = f"""<div class="max-w-4xl mx-auto p-8 bg-transparent shadow-2xl rounded-3xl border border-white/10 my-10 font-sans text-slate-200">
    <header class="mb-12 border-l-8 border-cyan-500 pl-6 py-4 bg-cyan-500/10 rounded-r-xl">
        <h1 class="text-4xl font-extrabold text-white tracking-tight">A10: Microeconomía Superior (MASTER)</h1>
        <p class="text-lg text-cyan-300 font-medium mt-2">Tratado Avanzado basado en Mankiw y Textos Complementarios de Alto Nivel</p>
    </header>

    <div class="prose prose-cyan max-w-none prose-invert">
{content}
    </div>

    <footer class="mt-12 pt-8 border-t border-white/10 text-center text-slate-500 text-sm">
        &copy; 2026 Tech Institute | Licenciatura en Economía | Generado por Agente Académico O-3 basado en Libro Master
    </footer>
</div>"""

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html_wrapper)
print("Wrapped A10 Master with premium HTML layout.")
