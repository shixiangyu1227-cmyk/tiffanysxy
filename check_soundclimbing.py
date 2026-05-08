import sys, re
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Second card-cover--03 is SoundClimbing
m = list(re.finditer(r'card-cover card-cover--03', content))[1]
snippet = content[m.start():m.start()+1000]
sys.stdout.buffer.write(snippet.encode('utf-8'))
