import json
import sys
import os

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

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python format_mic.py <input_json_path> <mod_id> <mod_title>")
        sys.exit(1)
        
    input_path = sys.argv[1]
    mod_id = sys.argv[2]
    mod_title = sys.argv[3]
    
    with open(input_path, 'r', encoding='utf-8') as f:
        # The tool output might just be the direct JSON string, or not quite standard python dict output
        text = f.read()
        
    try:
        # Usually it writes single quotes if it's strictly a python dict string, 
        # or valid JSON. Let's safely extract the "answer" field.
        # simple parsing just in case ast.literal_eval or json.loads fails
        # Let's try json.loads first, but fix single quotes to double quotes if it's python repr.
        text = text.strip()
        # Just use ast.literal_eval as it evaluates python dict representation safely
        import ast
        data = ast.literal_eval(text)
        guide_content = data.get("answer", "")
    except Exception as e:
        print(f"Failed to parse dict. Error: {e}")
        # fallback string search
        idx = text.find("'answer': '")
        if idx == -1:
            idx = text.find('"answer":"')
            if idx != -1:
                # simple extract
                import re
                match = re.search(r'"answer"\s*:\s*"(.*?)"\s*,\s*"conversation_id"', text, re.DOTALL)
                if match:
                    guide_content = match.group(1).encode('utf-8').decode('unicode_escape')
                else:
                    guide_content = text
            else:
                guide_content = text
        else:
            # We are pretty sure AST eval will work for python dicts
            pass

    # Limpiar Markdown wrapper
    if guide_content.startswith("```markdown\\n"):
        guide_content = guide_content[13:]
    elif guide_content.startswith("```markdown\\n"):
         guide_content = guide_content[12:]
    elif guide_content.startswith("```\\n"):
        guide_content = guide_content[4:]
    elif guide_content.startswith("```"):
        guide_content = guide_content[3:]
        
    if guide_content.endswith("```\\n"):
        guide_content = guide_content[:-4]
    elif guide_content.endswith("```"):
        guide_content = guide_content[:-3]

    final_html = format_master_content(guide_content, mod_title, mod_id)
    
    output_dir = "/Users/machd/Desktop/licecon/web-portal/public/program"
    os.makedirs(output_dir, exist_ok=True)
    out_path = os.path.join(output_dir, f"{mod_id}.md")
    
    with open(out_path, 'w', encoding='utf-8') as out:
        out.write(final_html)
    
    print(f"Successfully generated {out_path}")
