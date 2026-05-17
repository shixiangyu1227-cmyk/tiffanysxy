import sys, re
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

m = list(re.finditer(r'card-cover card-cover--02', content))
for match in m:
    snippet = content[match.start()+600:match.start()+1200]
    sys.stdout.buffer.write(snippet.encode('utf-8'))
    sys.stdout.buffer.write(b'\n---\n')
