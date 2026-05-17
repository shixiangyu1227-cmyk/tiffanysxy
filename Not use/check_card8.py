import sys, re
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all card-cover--03 occurrences
matches = list(re.finditer(r'card-cover card-cover--03', content))
sys.stdout.buffer.write(f'Found {len(matches)} card-cover--03\n'.encode())
for i, match in enumerate(matches):
    snippet = content[match.start():match.start()+600]
    sys.stdout.buffer.write(f'\n--- Instance {i+1} ---\n'.encode())
    sys.stdout.buffer.write(snippet.encode('utf-8'))
