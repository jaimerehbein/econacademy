import json
import os

filepath = '/Users/machd/Desktop/licecon/web-portal/public/program/a10_master.md'

with open(filepath, 'r', encoding='utf-8') as f:
    raw_content = f.read()

try:
    data = json.loads(raw_content)
    if "answer" in data:
        markdown_content = data["answer"]
        
        # Clean up markdown code blocks if present in the answer
        if markdown_content.startswith("```markdown\n"):
            markdown_content = markdown_content[12:]
        elif markdown_content.startswith("```markdown"):
            markdown_content = markdown_content[11:]
        elif markdown_content.startswith("```\n"):
            markdown_content = markdown_content[4:]
        elif markdown_content.startswith("```"):
            markdown_content = markdown_content[3:]
            
        if markdown_content.endswith("```\n"):
            markdown_content = markdown_content[:-4]
        elif markdown_content.endswith("```"):
            markdown_content = markdown_content[:-3]
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        print("Extracted and saved pure markdown.")
    else:
        print("No 'answer' key in JSON.")
except Exception as e:
    print(f"Error parseando JSON: {e}")
