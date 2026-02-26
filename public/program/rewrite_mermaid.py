import re

with open('/Users/machd/Desktop/licecon/web-portal/public/program/map1.md', 'r') as f:
    content = f.read()

# Replace all classDefs
content = re.sub(r' +classDef [a-zA-Z0-9]+ fill:.*?color:.*?\n', '', content)

# Remove all :::class references
content = re.sub(r' :::[a-zA-Z0-9]+\n', '\n', content)

# Remove generic double quotes from nodes
content = re.sub(r'A\(\(\"(.*?)\"\)\)', r'A((\1))', content)

with open('/Users/machd/Desktop/licecon/web-portal/public/program/map1.md', 'w') as f:
    f.write(content)
