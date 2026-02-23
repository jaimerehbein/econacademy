"""
Senior UX Content Architect v9 — ZERO-NOISE + DARK MODE + ROTATING COLORS
- Section numbers hidden in HTML comments <!-- x.x -->
- NO Markdown # symbols — replaced by contextual emoji icons
- Dark mode UI (dark backgrounds, light text)
- 8-color rotating palette per H2 section (stimulating study)
- Premium floating cards
- Pedagogical "Puntos Clave" per main section
- Anti-noise: strips *, _, inline artifacts, hidden citations
"""
import os, glob, re, sys

# ─── helpers ─────────────────────────────────────────────────────────────────

def strip_noise(text):
    # 0. Strip repetitive noisy fragments (NotebookLM/MASTER SERIES hallucinations)
    fragments = [
        r'(?i)MIC\s+MASTER\s+SERIES',
        r'(?i)ECONOMICS\s+MASTER\s+SERIES',
        r'(?i)MAC\s+MASTER\s+SERIES',
        r'(?i)TOPE\s+DE\s+GAMA',
        r'(?i)DARK\s+MODE',
        r'(?i)ZERO-NOISE\s+UX',
        r'(?i)MIC\d+',
        r'(?i)MAC\d+',
        r'(?i)Teoría\s+del\s+Consumidor\s+y\s+Demanda\s+Individual',
        r'(?i)Microeconomía\s+Avanzada',
        r'(?i)La\s+ciencia\s+de\s+la\s+macroeconomía',
        r'(?i)Guía\s+de\s+estudio\s+académica.*?(?=:|$|\n)',
        r'(?i)\(Módulo\s+.*?\)',
        r'(?i)A10MASTER\s+v\d+\.\d+',
        r'<!--\s*(HERO|FOOTER)\s*-->',
        r'(?i)TE\s+Tech\s+Economics\s+Institute\s+Zero-Noise\s+Architecture\s+v\d+',
        r'(?i)Glosario\s+Recursos',
        r'(?i)A\s+continuación\s+presento.*?$'
    ]
    for frag in fragments:
        text = re.sub(frag, '', text)
    
    # 1. Punctuation Clean: Remove dangling colons, empty parens, and clusters
    text = re.sub(r'\(.*?\)', lambda m: '' if not re.search(r'\w', m.group(0)) else m.group(0), text)
    text = re.sub(r':\s*$', '', text)
    text = re.sub(r':\s*$', '', text) # Double pass for nested
    text = re.sub(r',\s*,', ',', text)
    text = re.sub(r',\s*\.', '.', text) 
    text = re.sub(r'\.\s*\.', '.', text)
    text = re.sub(r'\.\s*:', '.', text)
    text = re.sub(r'\s{2,}', ' ', text) # Normalise spaces
    math_blocks = []
    
    def isolate_math(match):
        math_blocks.append(match.group(0))
        return f"@@MATHBLOCK{len(math_blocks)-1}@@"
        
    # Extract $$...$$ first, then $...$
    text = re.sub(r'\$\$.*?\$\$', isolate_math, text, flags=re.DOTALL)
    text = re.sub(r'\$(?!\s).*?(?<!\s)\$', isolate_math, text)

    text = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*([^*]+)\*',     r'<em>\1</em>', text)
    text = re.sub(r'_([^_]+)_',       r'<em>\1</em>', text)
    text = re.sub(r'(?<!\w)\*(?!\w)', '', text)
    
    # Citations [1], [74] → invisible span, preserved in source
    # We use a more aggressive match to catch [19], [20] or [12, 13]
    text = re.sub(r'\[(\d+(?:,\s*\d+)*)\]',
                  r'<span class="hidden" data-ref="\1" aria-hidden="true"></span>', text)
                  
    # 2. Artifact Removal: Remove any leftover asterisks, underscores, and visible multi-level section numbers
    text = text.replace('*', '').replace('_', '')
    text = re.sub(r'^\s*\d+(?:\.\d+)+\.?\s+', '', text)
    
    # 3. Punctuation Clean: Remove clusters like ", , ." or ".:"
    text = re.sub(r',\s*,', ',', text)
    text = re.sub(r'\.\s*\.', '.', text)
    text = re.sub(r'\.\s*:', '.', text)
    text = re.sub(r'\s{2,}', ' ', text) # Normalise spaces
    
    # 4. Sentence Repair: Replace all newlines with spaces to join fragmented lines within the same block
    text = text.replace('\n', ' ')
    
    # 5. Block Start Clean: Remove leading dots/symbols often left by syllabus fragments
    text = re.sub(r'^[\s·•*-]+', '', text)

    # 6. Deduplicate repeating HTML tags (common in recursive builds)
    text = re.sub(r'(<a.*?>.*?</a>\s*)\1+', r'\1', text)
    text = re.sub(r'(<span.*?>.*?</span>\s*)\1+', r'\1', text)

    # Restore math blocks
    for i, mb in enumerate(math_blocks):
        text = text.replace(f"@@MATHBLOCK{i}@@", mb)
        
    return text.strip()

def clean_title(raw_title):
    # 3. Hidden Metadata: Remove leading asterisks and numbers from titles
    clean_t = re.sub(r'^[\*\_]+', '', raw_title.strip())
    title = re.sub(r'^\d+(?:\.\d+)*\.?\s*', '', clean_t).strip()
    title = re.sub(r'(\s*\[\d+(?:,\s*\d+)*\])+\s*$', '', title).strip()
    return title

def extract_number(raw_title):
    clean_t = re.sub(r'^[\*\_]+', '', raw_title.strip())
    m = re.match(r'^(\d+(?:\.\d+)*\.?)', clean_t)
    return m.group(1) if m else ''

# ─── icon mapping ─────────────────────────────────────────────────────────────

ICON_MAP = [
    (['mercado', 'precio', 'oferta', 'demanda', 'competencia', 'microeconomía'],           '📈'),
    (['macroeconomía', 'pib', 'inflación', 'desempleo', 'ciclo económico', 'crecimiento'],'🏦'),
    (['comercio', 'exportación', 'importación', 'global', 'internacional', 'balanza'],     '🌐'),
    (['empresa', 'negocio', 'administración', 'organización', 'gestión', 'dirección'],     '🏢'),
    (['estrategia', 'planificación', 'objetivos', 'misión', 'visión', 'plan'],             '🎯'),
    (['recursos humanos', 'personal', 'trabajador', 'reclutamiento', 'empleo', 'nómina'], '👥'),
    (['marketing', 'publicidad', 'marca', 'cliente', 'segmento', 'producto', 'venta'],    '📣'),
    (['producción', 'operación', 'proceso', 'inventario', 'cadena', 'logística'],         '⚙️'),
    (['liderazgo', 'motivación', 'equipo', 'cultura', 'comunicación organizacional'],     '🤝'),
    (['finanzas', 'financiero', 'inversión', 'capital', 'crédito', 'préstamo', 'deuda'],  '💰'),
    (['contabilidad', 'balance', 'activo', 'pasivo', 'patrimonio', 'estado financiero'],  '📒'),
    (['presupuesto', 'gasto', 'ingreso', 'egreso', 'costo', 'rentabilidad'],              '💹'),
    (['bolsa', 'acción', 'bono', 'título', 'fondo', 'portafolio'],                        '📊'),
    (['derecho', 'ley', 'legal', 'norma', 'obligación', 'contrato', 'régimen'],           '⚖️'),
    (['tributar', 'fiscal', 'impuesto', 'tributo', 'hacienda', 'sat', 'contribuyente'],   '🏛️'),
    (['delito', 'sanción', 'multa', 'infracción', 'penal', 'judicial', 'recurso'],       '🔒'),
    (['sistema', 'tecnología', 'digital', 'software', 'dato', 'información', 'red'],     '💻'),
    (['estadística', 'probabilidad', 'muestra', 'variable', 'regresión', 'modelo'],      '🔢'),
    (['investigación', 'metodología', 'hipótesis', 'análisis', 'estudio', 'teoría'],     '🔬'),
    (['historia', 'evolución', 'origen', 'antecedente', 'tendencia', 'corriente'],       '📜'),
    (['ética', 'responsabilidad', 'sostenible', 'social', 'bienestar', 'equidad'],       '🌱'),
    (['concepto', 'definición', 'fundamento', 'principio', 'clasificación', 'tipo'],     '📖'),
]

def topic_icon(title):
    t = title.lower()
    for keywords, icon in ICON_MAP:
        if any(kw in t for kw in keywords):
            return icon
    return '📌'

# ─── color palette (rotating per H2 section) ─────────────────────────────────
# Each tuple: (gradient_from, gradient_to, bar_bg, badge_bg+border, badge_text,
#              card_bg+border-left, pk_from, pk_border, pk_accent)

SECTION_COLORS = [
    ('from-indigo-300', 'to-violet-400',   'bg-indigo-500', 'bg-indigo-500/15 border-indigo-500/30',  'text-indigo-300', 'bg-indigo-500/8 border-l-indigo-400',   'from-indigo-950/90 to-slate-900/90', 'border-indigo-500/25', 'text-indigo-400'),
    ('from-cyan-300',   'to-blue-400',     'bg-cyan-500',   'bg-cyan-500/15 border-cyan-500/30',      'text-cyan-300',   'bg-cyan-500/8 border-l-cyan-400',       'from-cyan-950/90 to-slate-900/90',   'border-cyan-500/25',   'text-cyan-400'),
    ('from-emerald-300','to-teal-400',     'bg-emerald-500','bg-emerald-500/15 border-emerald-500/30','text-emerald-300','bg-emerald-500/8 border-l-emerald-400', 'from-emerald-950/90 to-slate-900/90','border-emerald-500/25','text-emerald-400'),
    ('from-amber-300',  'to-orange-400',   'bg-amber-500',  'bg-amber-500/15 border-amber-500/30',    'text-amber-300',  'bg-amber-500/8 border-l-amber-400',     'from-amber-950/90 to-slate-900/90',  'border-amber-500/25',  'text-amber-400'),
    ('from-rose-300',   'to-pink-400',     'bg-rose-500',   'bg-rose-500/15 border-rose-500/30',      'text-rose-300',   'bg-rose-500/8 border-l-rose-400',       'from-rose-950/90 to-slate-900/90',   'border-rose-500/25',   'text-rose-400'),
    ('from-fuchsia-300','to-purple-400',   'bg-fuchsia-500','bg-fuchsia-500/15 border-fuchsia-500/30','text-fuchsia-300','bg-fuchsia-500/8 border-l-fuchsia-400', 'from-fuchsia-950/90 to-slate-900/90','border-fuchsia-500/25','text-fuchsia-400'),
    ('from-sky-300',    'to-blue-400',     'bg-sky-500',    'bg-sky-500/15 border-sky-500/30',        'text-sky-300',    'bg-sky-500/8 border-l-sky-400',         'from-sky-950/90 to-slate-900/90',    'border-sky-500/25',    'text-sky-400'),
    ('from-lime-300',   'to-green-400',    'bg-lime-500',   'bg-lime-500/15 border-lime-500/30',      'text-lime-300',   'bg-lime-500/8 border-l-lime-400',       'from-lime-950/90 to-slate-900/90',   'border-lime-500/25',   'text-lime-400'),
]

def get_color(idx):
    return SECTION_COLORS[idx % len(SECTION_COLORS)]

# ─── block parser ─────────────────────────────────────────────────────────────

def parse_extended(content):
    # 1. Binary Scrubbing: Identify and remove PNG chunks or abnormally long non-space strings
    lines = []
    for line in content.split('\n'):
        if re.search(r'(IHDR|IDAT|pHYs|PLTE|\x89PNG|sRGB)', line):
            continue
        if any(len(word) > 80 for word in line.split()):
            continue
        lines.append(line)
    content = '\n'.join(lines)

    content = re.sub(r'</?(?:div|section|header|footer|p|aside|span|ul|li|h[1-6]|details|summary|strong|em|article)[^>]*>', '', content)
    content = re.sub(r'\n(#{1,4}\s)', r'\n\n\1', content)
    content = re.sub(r'([^\n])\n(#{1,4}\s)', r'\1\n\n\2', content)

    raw_blocks = [b.strip() for b in re.split(r'\n{2,}', content) if b.strip()]
    blocks = []

    for block in raw_blocks:
        lines = block.split('\n')
        first = lines[0].strip()
        rest  = ' '.join(l.strip() for l in lines[1:] if l.strip())

        hm = re.match(r'^(#{1,4})\s+(.*)', first)
        if hm:
            hashes, raw_title = hm.groups()
            level  = len(hashes)
            number = extract_number(raw_title)
            title  = clean_title(raw_title)
            body   = strip_noise(rest) if rest else ''
            blocks.append({'type': 'heading', 'level': level, 'number': number,
                           'title': title, 'body': body, 'items': []})
            continue

        if re.search(r'^\s*\d+\.\s+\S', block, re.MULTILINE):
            intro_lines, steps = [], []
            for line in lines:
                ms = re.match(r'^\s*\*{0,2}(\d+)\.\*{0,2}\s+(.*)', line) or \
                     re.match(r'^\s*(\d+)\.\s+(.*)', line)
                if ms:
                    steps.append((ms.group(1), strip_noise(ms.group(2))))
                elif line.strip():
                    intro_lines.append(strip_noise(line.strip()))
            if steps:
                blocks.append({'type': 'stepper', 'body': ' '.join(intro_lines),
                               'items': steps, 'title': '', 'number': '', 'level': 0})
                continue

        if any(l.strip().startswith(('* ', '- ')) for l in lines):
            intro_lines, items = [], []
            for line in lines:
                l = line.strip()
                if l.startswith(('* ', '- ')): items.append(strip_noise(l[2:]))
                elif l: intro_lines.append(strip_noise(l))
            blocks.append({'type': 'list', 'body': ' '.join(intro_lines),
                           'items': items, 'title': '', 'number': '', 'level': 0})
            continue

        if '$$' in block:
            blocks.append({'type': 'formula', 'body': block.strip(),
                           'title': '', 'number': '', 'items': [], 'level': 0})
            continue

        if block.strip() in ('---', '***', '___'):
            blocks.append({'type': 'separator', 'body': '',
                           'title': '', 'number': '', 'items': [], 'level': 0})
            continue

        if block.strip():
            blocks.append({'type': 'text', 'body': strip_noise(block),
                           'title': '', 'number': '', 'items': [], 'level': 0})

    # 4. Sentence Repair: Merge consecutive text blocks if they are fragmented
    merged_blocks = []
    for b in blocks:
        if merged_blocks and merged_blocks[-1]['type'] == 'text' and b['type'] == 'text':
            # If the previous text block does not end with punctuation, merge it
            if not re.search(r'[.:?!>"]\s*$', merged_blocks[-1]['body']):
                merged_blocks[-1]['body'] += " " + b['body']
                continue
        merged_blocks.append(b)

    return merged_blocks

# ─── renderers ────────────────────────────────────────────────────────────────

# ─── renderers ────────────────────────────────────────────────────────────────

def render_hero(b):
    return f'''
<header class="mb-24">
    <div class="flex items-center gap-4 mb-8">
        <div class="w-8 h-0.5 bg-indigo-500 rounded-full"></div>
        <span class="text-indigo-400 font-black text-[10px] uppercase tracking-[0.4em]">Economics Master Series</span>
    </div>
    <h1 class="text-5xl md:text-7xl font-black text-white tracking-tighter leading-none mb-8">
        {b.get('title', 'ECON')}
    </h1>
    <div class="flex flex-wrap gap-3">
        <span class="bg-indigo-500/15 text-indigo-300 border border-indigo-500/25 px-4 py-1 rounded-full text-[10px] font-black uppercase tracking-[0.3em]">Zero-Noise UX</span>
        <span class="bg-white/5 text-slate-400 border border-white/10 px-4 py-1 rounded-full text-[10px] font-black uppercase tracking-[0.3em]">v9.0 · Dark Mode</span>
    </div>
</header>'''

def render_key_points(points):
    if not points: return ""
    cleaned_points = []
    for p in points:
        cp = strip_noise(p)
        if cp: cleaned_points.append(cp)
    
    if not cleaned_points: return ""
    
    li_items = "\n".join([f'<li class="flex items-start gap-3 text-slate-200 text-sm leading-relaxed"><span class="text-indigo-400 flex-shrink-0 mt-0.5 font-black">✦</span><span>{p}</span></li>' for p in cleaned_points])
    return f'''
<div class="bg-gradient-to-br from-indigo-950/90 to-slate-900/90 border border-indigo-500/25 p-6 md:p-10 rounded-2xl md:rounded-[2rem] my-8 md:my-14 shadow-xl relative overflow-hidden">
    <div class="absolute top-0 right-0 w-32 md:w-40 h-32 md:h-40 bg-white/5 -mr-16 md:-mr-20 -mt-16 md:-mt-20 rounded-full pointer-events-none"></div>
    <div class="relative z-10">
        <h5 class="text-indigo-400 text-[9px] md:text-[10px] uppercase tracking-[0.4em] font-black mb-6 flex items-center gap-3">
            <span class="w-6 h-px inline-block opacity-60"></span>
            Puntos Clave
        </h5>
        <ul class="space-y-4">
{li_items}
        </ul>
    </div>
</div>'''

def render_formula(b):
    cleaned_body = strip_noise(b['body'])
    if not cleaned_body: return ""
    return f'''
<div class="bg-white/5 border border-white/10 p-4 md:p-8 my-8 rounded-2xl text-center overflow-x-auto">
    {cleaned_body}
</div>'''

# ─── assembler ────────────────────────────────────────────────────────────────

def assemble(blocks):
    html_parts = []
    section_id = 0

    for b in blocks:
        if b['type'] == 'hero':
            html_parts.append(render_hero(b))
        
        elif b['type'] == 'separator':
            html_parts.append('<div class="my-16 border-t border-white/10"></div>')

        elif b['type'] == 'heading':
            title = strip_noise(b['title'])
            if not title: continue
            
            if b['level'] <= 1:
                html_parts.append(f'''
<div class="flex items-center gap-3 md:gap-4 mt-12 md:mt-20 mb-6">
    <span class="text-3xl md:text-4xl drop-shadow-lg">🏦</span>
    <h2 class="text-2xl md:text-4xl font-black tracking-tight leading-tight bg-gradient-to-r from-indigo-300 to-violet-400 bg-clip-text text-transparent">{title}</h2>
</div>''')
            elif b['level'] == 2:
                section_id += 1
                
                body_p = ""
                if b['body']:
                    cleaned_p = strip_noise(b['body'])
                    if cleaned_p:
                        body_p = f'<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">{cleaned_p}</p>'
                
                html_parts.append(f'''
<section class="mb-16 last:mb-0">
<!-- section: {section_id}. -->
<div class="flex items-center gap-4 md:gap-5 mt-10 md:mt-16 mb-6">
    <span class="text-2xl md:text-3xl drop-shadow-md">📖</span>
    <div>
        <h2 class="text-xl md:text-3xl font-black tracking-tight bg-gradient-to-r from-indigo-300 to-violet-400 bg-clip-text text-transparent">{title}</h2>
        <div class="w-10 md:w-14 h-1 bg-indigo-500 rounded-full mt-2 opacity-80"></div>
    </div>
</div>
{body_p}''')
                
                # Check for list items (stepper)
                if b.get('items'):
                    steps = []
                    for i, item in enumerate(b['items']):
                        cleaned_item = strip_noise(item)
                        if cleaned_item:
                            steps.append(f'''
<div class="flex items-start gap-5 p-5 bg-indigo-500/10 rounded-2xl my-3 border bg-indigo-500/20 hover:bg-indigo-500/15 transition-all">
    <!-- step:{i+1} -->
    <div class="bg-indigo-500 text-white w-9 h-9 rounded-full flex items-center justify-center font-black flex-shrink-0 text-sm shadow-md">{i+1}</div>
    <div class="text-slate-200 text-base leading-snug pt-1">{cleaned_item}</div>
</div>''')
                    html_parts.append("\n".join(steps))
                
                html_parts.append('</section>')

            elif b['level'] >= 3:
                html_parts.append(f'''
<div class="flex items-center gap-4 mt-10 mb-4">
    <span class="text-lg bg-indigo-500/15 border-indigo-500/30 border w-9 h-9 rounded-xl flex items-center justify-center flex-shrink-0 shadow-sm">📌</span>
    <h3 class="text-xl font-bold text-indigo-300 tracking-tight">{title}</h3>
</div>''')
                if b['body']:
                    cleaned_p = strip_noise(b['body'])
                    if cleaned_p:
                        html_parts.append(f'<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">{cleaned_p}</p>')

        elif b['type'] == 'text':
            cleaned_p = strip_noise(b['body'])
            if cleaned_p:
                html_parts.append(f'<p class="text-slate-300 text-base md:text-lg leading-relaxed my-4">{cleaned_p}</p>')

        elif b['type'] == 'stepper':
            steps = []
            for n, t in b['items']:
                steps.append(f'''
<div class="flex items-start gap-5 p-5 bg-indigo-500/10 rounded-2xl my-3 border bg-indigo-500/20 hover:bg-indigo-500/15 transition-all">
    <!-- step:{n} -->
    <div class="bg-indigo-500 text-white w-9 h-9 rounded-full flex items-center justify-center font-black flex-shrink-0 text-sm shadow-md">{n}</div>
    <div class="text-slate-200 text-base leading-snug pt-1">{t}</div>
</div>''')
            html_parts.append("\n".join(steps))

        elif b['type'] == 'formula':
            html_parts.append(render_formula(b))

    return "\n".join(html_parts)

# ─── template ─────────────────────────────────────────────────────────────────

def build_template(name, body):
    return f'''<div class="max-w-4xl mx-auto px-4 py-14 md:px-12 font-sans">

<!-- HERO -->
<header class="mb-24">
    <div class="flex items-center gap-4 mb-8">
        <div class="w-8 h-0.5 bg-indigo-500 rounded-full"></div>
        <span class="text-indigo-400 font-black text-[10px] uppercase tracking-[0.4em]">Economics Master Series</span>
    </div>
    <h1 class="text-5xl md:text-7xl font-black text-white tracking-tighter leading-none mb-8">
        {name}
    </h1>
    <div class="flex flex-wrap gap-3">
        <span class="bg-indigo-500/15 text-indigo-300 border border-indigo-500/25 px-4 py-1 rounded-full text-[10px] font-black uppercase tracking-[0.3em]">Zero-Noise UX</span>
        <span class="bg-white/5 text-slate-400 border border-white/10 px-4 py-1 rounded-full text-[10px] font-black uppercase tracking-[0.3em]">v9.0 · Dark Mode</span>
    </div>
</header>

{body}

<!-- FOOTER -->
<footer class="mt-28 pt-10 border-t border-white/10">
    <div class="flex flex-col md:flex-row justify-between items-center gap-6">
        <div class="flex items-center gap-4">
            <div class="w-9 h-9 bg-indigo-600 rounded-xl flex items-center justify-center text-white font-black text-xs shadow-md">TE</div>
            <div>
                <p class="font-black text-white text-sm">Tech Economics Institute</p>
                <p class="text-slate-500 text-[10px] uppercase tracking-[0.3em]">Zero-Noise Architecture v9</p>
            </div>
        </div>
        <div class="flex gap-8 text-[10px] font-black text-slate-600 uppercase tracking-widest">
            <a href="#" class="hover:text-indigo-400 transition-colors">Glosario</a>
            <a href="#" class="hover:text-indigo-400 transition-colors">Recursos</a>
        </div>
    </div>
</footer>

</div>'''

# ─── entry point ──────────────────────────────────────────────────────────────

def process(source_path, output_path):
    with open(source_path, 'r', encoding='utf-8') as f:
        raw = f.read()

    blocks = parse_extended(raw)
    body   = assemble(blocks)
    name   = os.path.basename(output_path).replace('.md', '').upper()
    result = build_template(name, body)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(result)

    print(f'Zero-Noise v9 → {os.path.basename(output_path)} ✓')


if __name__ == '__main__':
    target_file = sys.argv[1] if len(sys.argv) > 1 else 'a1_extended.md'
    program_dir = '/Users/machd/Desktop/licecon/web-portal/public/program/'
    src = os.path.join(program_dir, target_file)
    if not os.path.exists(src):
        print(f'Error: {target_file} not found.'); sys.exit(1)
    out = os.path.join(program_dir, target_file.replace('_extended', ''))
    process(src, out)
