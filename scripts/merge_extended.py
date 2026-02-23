import os
import re
import glob

def merge_extended_contents():
    program_dir = os.path.join(os.getcwd(), 'public', 'program')
    extended_files = glob.glob(os.path.join(program_dir, '*_extended.md'))
    
    print(f"Encontrados {len(extended_files)} archivos *_extended.md para fusionar.")
    
    merged_count = 0
    
    for ext_file in extended_files:
        basename = os.path.basename(ext_file)
        base_name_no_ext = basename.replace('_extended.md', '')
        target_file = os.path.join(program_dir, f"{base_name_no_ext}.md")
        
        if not os.path.exists(target_file):
            print(f"Advertencia: Archivo destino {base_name_no_ext}.md no encontrado.")
            continue
            
        with open(target_file, 'r', encoding='utf-8') as tf:
            target_content = tf.read()
            
        if "Desarrollo Integral del Temario" in target_content:
            print(f"El archivo {base_name_no_ext}.md ya tiene el contenido extendido fusionado. Saltando.")
            continue
            
        with open(ext_file, 'r', encoding='utf-8') as ef:
            extended_content = ef.read()
            
        # Clean up the extended content: remove top level title if present
        lines = extended_content.splitlines()
        if lines and lines[0].startswith('# '):
            lines = lines[1:]
        elif lines and len(lines) > 1 and lines[0] == '' and lines[1].startswith('# '):
           lines = lines[2:]
        elif lines and len(lines) > 2 and "Guía de Estudio" in extended_content[:150]:
           # Try to strip first # title
           new_lines = []
           found_first = False
           for line in lines:
               if line.startswith('# ') and not found_first:
                   found_first = True
                   continue
               new_lines.append(line)
           lines = new_lines
           
        extended_content_clean = "\n".join(lines).strip()
        
        # Determine the primary color to use for prose
        primary_color = "indigo" # default
        color_match = re.search(r'prose prose-([a-z]+)', target_content)
        if color_match:
            primary_color = color_match.group(1)
        else:
            color_match = re.search(r'border-l-8 border-([a-z]+)', target_content)
            if color_match:
                primary_color = color_match.group(1)
                
        # Build the HTML wrapper for the extended content
        html_section = """
    <section class="mb-10 p-8 bg-slate-900/60 rounded-3xl border border-white/10 shadow-xl relative overflow-hidden">
        <div class="absolute inset-0 bg-gradient-to-br from-COLOR-500/5 to-transparent pointer-events-none"></div>
        <h2 class="text-3xl font-extrabold text-white mb-8 flex items-center border-b border-white/10 pb-4 relative z-10">
            <span class="bg-COLOR-600 text-white w-10 h-10 rounded-xl flex items-center justify-center mr-4 text-lg shadow-lg shadow-COLOR-500/30">📚</span>
            Tema Master: Desarrollo Integral del Temario
        </h2>
        <div class="prose prose-invert prose-COLOR max-w-none relative z-10 
                    prose-headings:text-COLOR-100 prose-headings:font-bold 
                    prose-h2:border-b prose-h2:border-white/10 prose-h2:pb-2 prose-h2:mt-10
                    prose-h3:text-white
                    prose-a:text-COLOR-400 hover:prose-a:text-COLOR-300
                    prose-strong:text-white
                    prose-blockquote:border-l-COLOR-500 prose-blockquote:bg-COLOR-900/20 prose-blockquote:py-1 prose-blockquote:px-4 prose-blockquote:rounded-r-lg">
EXTENDED_CONTENT
        </div>
    </section>

"""
        html_section = html_section.replace("COLOR", primary_color)
        html_section = html_section.replace("EXTENDED_CONTENT", extended_content_clean)
        
        # Inject right before the <footer>
        footer_idx = target_content.find("<footer")
        
        if footer_idx != -1:
            new_target_content = target_content[:footer_idx] + html_section + target_content[footer_idx:]
            
            with open(target_file, 'w', encoding='utf-8') as tf:
                tf.write(new_target_content)
            print(f"[+] Fusionado exitosamente en {base_name_no_ext}.md con tema {primary_color}")
            merged_count += 1
        else:
            print(f"[-] No se encontró <footer> en {base_name_no_ext}.md. Abortando fusión para este archivo.")

    print(f"\n==========================================")
    print(f"Fusión completada. {merged_count} archivos actualizados.")
    print(f"==========================================")

if __name__ == "__main__":
    merge_extended_contents()
