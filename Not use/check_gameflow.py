import sys, re
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# First card-cover--03 is GameFlow
m = list(re.finditer(r'card-cover card-cover--03', content))[0]
snippet = content[m.start():m.start()+1000]
sys.stdout.buffer.write(snippet.encode('utf-8'))
