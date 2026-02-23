import fs from 'fs';
import path from 'path';

// Using native fetch if Node version >= 18, otherwise we'd need node-fetch.
// However, newer Node versions have `fetch` natively available globally.

const dataPath = path.join(process.cwd(), 'src', 'data.json');
const programPath = path.join(process.cwd(), 'public', 'program');

async function getWikipediaExtract(title) {
    try {
        // We use the Wikipedia REST API to get the summary
        const encodeTitle = encodeURIComponent(title);
        const url = `https://es.wikipedia.org/api/rest_v1/page/summary/${encodeTitle}`;
        const response = await fetch(url);

        if (response.ok) {
            const data = await response.json();
            if (data.type !== 'disambiguation' && data.extract) {
                return data.extract;
            }
        }
        return null;
    } catch (error) {
        console.error(`  [!] Error fetching Wikipedia for ${title}:`, error.message);
        return null;
    }
}

async function processSubjects() {
    console.log("=== Iniciando Enriquecimiento de Contenido con Wikipedia ===");

    // 1. Read master curriculum list
    const rawData = fs.readFileSync(dataPath, 'utf8');
    const curriculum = JSON.parse(rawData);
    const subjects = curriculum.asignaturas;

    let successCount = 0;

    for (const subject of subjects) {
        const fileCode = subject.codigo.toLowerCase();
        const markdownFilePath = path.join(programPath, `${fileCode}.md`);

        if (!fs.existsSync(markdownFilePath)) {
            console.log(`[SKIP] File not found for ${subject.nombre} (${fileCode}.md)`);
            continue;
        }

        console.log(`\nProcesando: ${subject.codigo} - ${subject.nombre}...`);

        // 2. Query Wikipedia
        const extract = await getWikipediaExtract(subject.nombre);

        if (extract) {
            console.log(`  [+] Extracto encontrado (${extract.substring(0, 50)}...)`);

            // 3. Formatear la cita
            const wikiBlock = `\n\n> [!NOTE]\n> **Contexto Enciclopédico (Wikipedia)**\n> ${extract}\n\n`;

            // 4. Inyectar en el Markdown
            let mdContent = fs.readFileSync(markdownFilePath, 'utf8');

            // Check if already injected
            if (mdContent.includes("Contexto Enciclopédico (Wikipedia)")) {
                console.log(`  [SKIP] Ya cuenta con el contexto enciclopédico.`);
                continue;
            }

            // Insert it after the Title / first paragraph or a specific marker
            // If the file starts with `# `, we try to inject it right after the first `## ` or at the end of the overview.

            // Simple injection logic: put it right before the first `## ` section, or append if no `##` exists.
            const splitMatch = mdContent.indexOf('\n## ');

            if (splitMatch !== -1) {
                mdContent = mdContent.slice(0, splitMatch) + wikiBlock + mdContent.slice(splitMatch);
            } else {
                mdContent += wikiBlock;
            }

            fs.writeFileSync(markdownFilePath, mdContent, 'utf8');
            console.log(`  [✔] Inyectado en ${fileCode}.md`);
            successCount++;
        } else {
            console.log(`  [-] No se encontró extracto directo en Wikipedia.`);
        }
    }

    console.log(`\n=== Proceso Completado ===`);
    console.log(`Subjects enriquecidos exitosamente: ${successCount}/${subjects.length}`);
}

processSubjects();
