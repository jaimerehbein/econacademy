import os, re
TARGET = '/Users/machd/Desktop/licecon/web-portal/public/program'
pending = []
for f in sorted(os.listdir(TARGET)):
    if not f.endswith('.md'): continue
    txt = open(os.path.join(TARGET, f)).read()
    if 'GLOSARIO v9.5' not in txt and '<!-- GLOSARIO -->' in txt:
        m = re.search(r'<h[12][^>]*>(.*?)</h[12]>', txt)
        title = m.group(1).strip() if m else f
        pending.append((f, title))
print(f'Total pending: {len(pending)}')
for fn, title in pending:
    print(f'{fn}: {title[:70]}')
