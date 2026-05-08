import re, sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()
original = content

new_svg = """        <svg class="mwc-scene" viewBox="0 0 480 280" preserveAspectRatio="xMidYMid slice"
             xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
          <defs>
            <linearGradient id="mwc-depth" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0%"   stop-color="#c5cdb2" stop-opacity="0"/>
              <stop offset="48%"  stop-color="#c5cdb2" stop-opacity="0"/>
              <stop offset="78%"  stop-color="#bfc8a8" stop-opacity="0.10"/>
              <stop offset="100%" stop-color="#b8c2a0" stop-opacity="0.26"/>
            </linearGradient>
          </defs>

          <!-- ① Sage green base — clean, light, minimal depth -->
          <rect width="480" height="280" fill="#c5cdb2"/>
          <ellipse cx="240" cy="72"  rx="300" ry="175" fill="#bfc9aa" opacity="0.52"/>
          <ellipse cx="110" cy="195" rx="196" ry="138" fill="#b8c2a2" opacity="0.38"/>
          <ellipse cx="385" cy="208" rx="218" ry="148" fill="#c0cab0" opacity="0.36"/>

          <!-- ② Upper sparse blossom hints — barely-there, y=38-132, ff-sm filter -->
          <g class="hf-detail" filter="url(#ff-sm)" opacity="0.50">
            <ellipse cx="84"  cy="44"  rx="9"  ry="7"  fill="#d0c2d8"/>
            <ellipse cx="198" cy="38"  rx="8"  ry="6"  fill="#d8c8ca"/>
            <ellipse cx="318" cy="46"  rx="10" ry="7"  fill="#ccc0d6"/>
            <ellipse cx="432" cy="40"  rx="8"  ry="6"  fill="#d4c4cc"/>
            <ellipse cx="50"  cy="74"  rx="11" ry="8"  fill="#c8bcd4"/>
            <ellipse cx="162" cy="68"  rx="9"  ry="7"  fill="#d6c8c4"/>
            <ellipse cx="276" cy="76"  rx="10" ry="8"  fill="#c4b8d0"/>
            <ellipse cx="390" cy="70"  rx="9"  ry="7"  fill="#d2c2ce"/>
            <ellipse cx="472" cy="74"  rx="8"  ry="6"  fill="#ccbcd8"/>
            <ellipse cx="24"  cy="102" rx="12" ry="9"  fill="#c0b2cc"/>
            <ellipse cx="122" cy="110" rx="10" ry="8"  fill="#d4bcc4"/>
            <ellipse cx="240" cy="104" rx="11" ry="8"  fill="#c6bad2"/>
            <ellipse cx="354" cy="112" rx="10" ry="7"  fill="#d0bece"/>
            <ellipse cx="462" cy="106" rx="9"  ry="7"  fill="#ccc0d4"/>
            <ellipse cx="72"  cy="124" rx="11" ry="8"  fill="#c2b4ce"/>
            <ellipse cx="188" cy="130" rx="10" ry="8"  fill="#d6c2c4"/>
            <ellipse cx="304" cy="126" rx="11" ry="8"  fill="#c4b8d2"/>
            <ellipse cx="418" cy="132" rx="10" ry="7"  fill="#cebccc"/>
          </g>

          <!-- ③ Mid blooms — sparse at top, growing denser downward, hf-mid + ff-mid -->
          <g class="hf-mid" filter="url(#ff-mid)" opacity="0.74">
            <ellipse cx="50"  cy="100" rx="14" ry="11" fill="#d4b8cc"/>
            <ellipse cx="140" cy="94"  rx="16" ry="12" fill="#baaece"/>
            <ellipse cx="280" cy="90"  rx="15" ry="11" fill="#d0b8c4"/>
            <ellipse cx="420" cy="98"  rx="16" ry="12" fill="#c4b4d4"/>
            <ellipse cx="24"  cy="130" rx="19" ry="14" fill="#c2b0d0"/>
            <ellipse cx="116" cy="136" rx="17" ry="13" fill="#d6b4be"/>
            <ellipse cx="214" cy="128" rx="18" ry="14" fill="#bcb0d2"/>
            <ellipse cx="312" cy="137" rx="17" ry="13" fill="#cebeda"/>
            <ellipse cx="410" cy="130" rx="19" ry="14" fill="#d2b2bc"/>
            <ellipse cx="470" cy="135" rx="14" ry="11" fill="#c4bcd4"/>
            <ellipse cx="50"  cy="160" rx="20" ry="16" fill="#c0b0ce"/>
            <ellipse cx="140" cy="166" rx="19" ry="15" fill="#d8b8c2"/>
            <ellipse cx="230" cy="158" rx="21" ry="16" fill="#baaed0"/>
            <ellipse cx="320" cy="167" rx="20" ry="15" fill="#ccbcda"/>
            <ellipse cx="410" cy="160" rx="21" ry="16" fill="#d4b2bc"/>
            <ellipse cx="470" cy="165" rx="17" ry="13" fill="#c2bcd6"/>
            <ellipse cx="18"  cy="188" rx="22" ry="17" fill="#c2b0cc"/>
            <ellipse cx="106" cy="194" rx="21" ry="16" fill="#d4b6c0"/>
            <ellipse cx="196" cy="186" rx="23" ry="18" fill="#bcb0d0"/>
            <ellipse cx="286" cy="195" rx="22" ry="17" fill="#ccbede"/>
            <ellipse cx="376" cy="188" rx="23" ry="18" fill="#d0b0b8"/>
            <ellipse cx="458" cy="193" rx="19" ry="15" fill="#c4bcd6"/>
            <ellipse cx="56"  cy="214" rx="24" ry="19" fill="#c4b6d2"/>
            <ellipse cx="148" cy="220" rx="23" ry="18" fill="#d6b8c4"/>
            <ellipse cx="240" cy="212" rx="25" ry="20" fill="#baaed2"/>
            <ellipse cx="330" cy="221" rx="24" ry="19" fill="#cebcd6"/>
            <ellipse cx="416" cy="214" rx="25" ry="20" fill="#d4b2be"/>
            <ellipse cx="474" cy="219" rx="19" ry="15" fill="#c2bcd8"/>
            <ellipse cx="20"  cy="242" rx="26" ry="20" fill="#c0b4d0"/>
            <ellipse cx="114" cy="248" rx="25" ry="19" fill="#d8b8c2"/>
            <ellipse cx="208" cy="241" rx="27" ry="21" fill="#bab0d2"/>
            <ellipse cx="302" cy="249" rx="26" ry="20" fill="#cebad8"/>
            <ellipse cx="396" cy="242" rx="27" ry="21" fill="#d2b0bc"/>
            <ellipse cx="468" cy="247" rx="21" ry="16" fill="#c4bcd6"/>
          </g>

          <!-- ④ Dense blurry lower layer — ff-fg heavy blur, growing toward bottom -->
          <g class="hf-fg" filter="url(#ff-fg)" opacity="0.56">
            <ellipse cx="64"  cy="192" rx="44" ry="34" fill="#c0aece"/>
            <ellipse cx="200" cy="198" rx="46" ry="36" fill="#d4b8c0"/>
            <ellipse cx="336" cy="191" rx="44" ry="34" fill="#b8aed4"/>
            <ellipse cx="462" cy="196" rx="38" ry="30" fill="#ccb0be"/>
            <ellipse cx="0"   cy="193" rx="34" ry="27" fill="#d0bcd6"/>
            <ellipse cx="96"  cy="225" rx="50" ry="40" fill="#c8b4d0"/>
            <ellipse cx="228" cy="231" rx="52" ry="42" fill="#d2b0bc"/>
            <ellipse cx="360" cy="224" rx="50" ry="40" fill="#bcb2d6"/>
            <ellipse cx="472" cy="229" rx="40" ry="32" fill="#ccb8d8"/>
            <ellipse cx="14"  cy="226" rx="38" ry="30" fill="#d8c4c0"/>
            <ellipse cx="52"  cy="258" rx="56" ry="44" fill="#c4b4d4"/>
            <ellipse cx="184" cy="264" rx="58" ry="46" fill="#d8bcc8"/>
            <ellipse cx="316" cy="257" rx="56" ry="44" fill="#b8b0d2"/>
            <ellipse cx="448" cy="262" rx="50" ry="40" fill="#ceb8d8"/>
            <ellipse cx="480" cy="258" rx="36" ry="29" fill="#d2b0bc"/>
            <ellipse cx="80"  cy="278" rx="64" ry="50" fill="#c2b2d4"/>
            <ellipse cx="216" cy="284" rx="66" ry="52" fill="#d4c0c8"/>
            <ellipse cx="352" cy="277" rx="62" ry="49" fill="#baaed0"/>
            <ellipse cx="476" cy="281" rx="52" ry="42" fill="#ccb4c2"/>
            <ellipse cx="0"   cy="280" rx="44" ry="35" fill="#d0bcd8"/>
          </g>

          <!-- ⑤ Depth gradient overlay — transparent top, subtle sage wash at bottom -->
          <rect width="480" height="280" fill="url(#mwc-depth)" pointer-events="none"/>
        </svg>"""

# Replace the entire mwc-scene SVG block
pattern = re.compile(
    r'        <svg class="mwc-scene".*?        </svg>',
    re.S
)
result = pattern.sub(new_svg, content, count=1)
if result != content:
    content = result
    sys.stdout.buffer.write(b'  OK: mwc-scene SVG replaced\n')
else:
    sys.stdout.buffer.write(b'  MISS: pattern not found\n')

changed = content != original
sys.stdout.buffer.write(f'Changed: {changed}\n'.encode())
if changed:
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    sys.stdout.buffer.write(b'Saved.\n')
