import sys
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

cards = re.findall(r'card-cover card-cover--\d+', content)
titles = re.findall(r'<div class="cover-title">(.*?)</div>', content, re.DOTALL)
nums = re.findall(r'<div class="cover-num">(.*?)</div>', content, re.DOTALL)

output = []
for i, (c, t, n) in enumerate(zip(cards, titles, nums)):
    output.append(f'{i+1}. {c} | num={n.strip()} | title={t.strip()}')

sys.stdout.buffer.write('\n'.join(output).encode('utf-8'))
sys.stdout.buffer.write(b'\n')
