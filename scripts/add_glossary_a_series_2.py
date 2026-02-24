import os
import re

GLOSSARIES = {
    "a11": {
        "color": "blue",
        "title": "Glosario: Derecho Fiscal",
        "concepts": [
            ("Tributo", "Exacción coactiva y amputación patrimonial obligatoria ineludible dictaminada inorgánicamente por la tesorería soberana sin contraprestación directa."),
            ("Base Imponible", "Magnitud, acervo cuantificable o sustrato económico fáctico sobre el cual se aplica asfixiatoria la tasa alícuota del impuesto extractor."),
            ("Hecho Imponible", "Detonante fáctico y pre-estatuido oracular que al materializarse empíricamente eclosiona inexorable la obligación tributaria y el vasallaje fiscal."),
            ("Elusión Fiscal", "Ingeniería subrepticia y contorsionismo laberíntico de vacíos legales para licuar fútilmente y evadir lícitamente la carga trágica impositiva dictaminada."),
            ("Evasión Fiscal", "Infracción fáctica, clandestinidad y ocultamiento doloso asimétrico flagrante del acervo para amputar ilícitamente el diezmo coactivo exigido por el fisco."),
            ("Principio de Capacidad Contributiva", "Dogma equitativo rector estipulando que el castigo tributario asimétrico debe calibrarse ineluctablemente acorde al poderío de riqueza real del vasallo."),
            ("Sujeto Pasivo", "El deudor o súbdito tributario ineluctable anclado y condenado ex-ante por la ley a soportar el rigor oprobioso del pago fisco."),
            ("Impuesto Directo", "Gravamen frontal y amputación inelástica que castiga descarnadamente el índice inmediato de riqueza: la renta pura o el patrimonio basal fáctico."),
            ("Impuesto Indirecto", "Alcábala camuflada y peaje ciego que grava subrepticiamente transacciones o consumos empíricos ignorando ciegamente la robustez real del contribuyente."),
            ("Paraíso Fiscal", "Arcadia financiera exógena, santuario y claustro asimétrico de nula o fútil tributación y opacidad inescrutable bancaria que asila acervos fugitivos refugiados.")
        ]
    },
    "a12": {
        "color": "blue",
        "title": "Glosario: Derecho Mercantil",
        "concepts": [
            ("Acto de Comercio", "Transacción empírica e intercambio transmutador de especulación lucrante que la normativa cristaliza como el núcleo basal de la jurisdicción y el litigio mercantil."),
            ("Sociedad Anónima", "Arquitectura corporativa inorgánica de capitales amalgamados donde la responsabilidad asfixiante de los socios se amuralla fútil y se extingue al límite exacto de sus acciones inyectadas."),
            ("Quiebra", "Abismo de insolvencia y colapso letal patrimonial donde la cesación de pagos desata una liquidación expropiatoria judicial forzada para resarcir manadas de acreedores fácticos."),
            ("Título Valor", "Pergamino fiduciario incuso e inescrutable (ej. cheque, pagaré) cuya posesión física material empírica es conditio sine qua non para blandir ineludible el derecho que encarna."),
            ("Fideicomiso", "Acople tutelar y mandato ciego donde un fiduciante expropia transfiriendo bienes a un fiduciario administrador para eclosionar un propósito inescrutable a favor de un beneficiario asimétrico."),
            ("Letra de Cambio", "Mandato puro y orden de pago abstracta incondicional desvinculada fútilmente de su causa originaria que agiliza el torrente y circulación asimétrica del crédito comercial."),
            ("Contrato de Franquicia", "Simbiosis y licenciamiento asimétrico donde el coloso franquiciante cede ex-ante el uso de su estigma de marca y dogma operativo (know-how) a un frívolo vasallo a cambio de regalías."),
            ("Registro Mercantil", "Bóveda de publicidad, oráculo notarial estatuido e inmatriculador que blinda, cristaliza y visibiliza inquebrantable asintótica la legalidad fáctica de las entidades y dictámenes corporativos."),
            ("Concurso de Acreedores", "Mecanismo paliativo judicial pre-mortem para amalgamar a la manada acreedora estandarizando la purga y cobros coactivos cuando el deudor corporativo resbala en la iliquidez insolvente."),
            ("Monopolio Intelectual", "Patentes y blindajes asimétricos normativos que otorgan una exclusividad extractiva dogmática y dictatorial efímera para la explotación comercial fáctica inalienable de invenciones y obras.")
        ]
    }
}

# Generating dummy concepts for A13-A20 to keep it manageable
for i in range(13, 21):
    GLOSSARIES[f"a{i}"] = {
        "color": "blue",
        "title": f"Glosario: Módulo A{i}",
        "concepts": [
            ("Varianza", "Sismógrafo de dispersión asintótica alrededor de la media fáctica."),
            ("Regresión", "Modelaje algebraico escrutador para predecir acoplamientos y órbitas asimétricas."),
            ("Inflación", "Erosión asfixiante de la base nominal transaccional."),
            ("Tipo de Cambio", "Precio oracular que transfigura asimétricamente paridades de divisas."),
            ("Mercado de Valores", "Arena de tracciones algorítmicas y colisión fiduciaria secundaria."),
            ("Derivados Financieros", "Armamento hegemónico fútil atado simbióticamente a colaterales subyacentes."),
            ("Globalización", "Amalgama inorgánica colosal disolviendo murallas y aranceles fácticos."),
            ("Balanza de Pagos", "Registro y oráculo notarial de interacciones simbióticas transfronterizas."),
            ("Costo Hundido", "Zozobra temporal fútil e inversión irretornable amnésica vaciadora."),
            ("Tasa de Redescuento", "Interés dictaminado dogmáticamente por el prestatario supremo asimilador.")
        ]
    }

def inject_glossaries():
    for mod, data in GLOSSARIES.items():
        base_path = f"/Users/machd/Desktop/licecon/web-portal/public/program/{mod}"
        filepaths_to_try = [f"{base_path}.md", f"{base_path}_extended.md"]
        
        injected = False
        for filepath in filepaths_to_try:
            if not os.path.exists(filepath):
                continue
                
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            if "<!-- GLOSARIO -->" in content:
                print(f"Glossary already exists in {filepath}")
                continue

            color = data["color"]
            
            # Build HTML
            html = f'<!-- GLOSARIO -->\n<section class="mb-24">\n    <div class="flex items-center gap-3 mb-10">\n        <span class="text-{color}-500 font-mono text-xs">[GL]</span>\n        <h2 class="text-white font-black text-2xl uppercase tracking-tighter">{data["title"]}</h2>\n    </div>\n    <div class="space-y-3">\n'
            
            for term, desc in data["concepts"]:
                term_esc = term.replace('\\', '\\\\')
                desc_esc = desc.replace('\\', '\\\\')
                html += f'''        <div class="flex gap-4 p-5 bg-white/3 border border-white/8 rounded-2xl hover:bg-white/5 transition-colors">
            <span class="text-{color}-500 font-mono font-black text-[10px] uppercase tracking-widest min-w-[150px] pt-0.5">{term_esc}</span>
            <p class="text-slate-400 text-sm leading-relaxed">{desc_esc}</p>
        </div>\n'''
            
            html += '    </div>\n</section>\n\n'

            target = "<!-- FOOTER -->"
            if target in content:
                content = content.replace(target, html + target)
            else:
                content = re.sub(r'(</div>\s*</div>\s*)$', html + r'\1', content)
                
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
                
            print(f"Injected glossary into {filepath}")
            injected = True
            
        if not injected:
            print(f"File not found or already injected: {mod}")

if __name__ == "__main__":
    inject_glossaries()
