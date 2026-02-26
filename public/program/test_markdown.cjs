const fs = require('fs');
const text = fs.readFileSync('/Users/machd/Desktop/licecon/web-portal/public/program/map1.md', 'utf-8');
console.log("File loaded, length:", text.length);
const mermaidMatches = text.match(/<pre class="mermaid.*?">(.*?)<\/pre>/gs);
if (mermaidMatches) {
    console.log("Found", mermaidMatches.length, "mermaid blocks.");
    console.log(mermaidMatches[0].substring(0, 500));
} else {
    console.log("No mermaid blocks found!");
}
