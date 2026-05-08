import re, sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()
original = content

# ── 1. Remove C1.png background from .more-work-card CSS ────────────
old_bg = "      background: url('C1.png') center/cover no-repeat;\n"
if old_bg in content:
    content = content.replace(old_bg, '', 1)
    sys.stdout.buffer.write(b'  OK: C1.png bg removed\n')
else:
    sys.stdout.buffer.write(b'  MISS: C1.png bg line\n')

# ── 2. Restore .mwc-scene position rule ─────────────────────────────
old_hover = '    .more-work-card:hover { transform: scale(1.012); }\n    .mwc-content {'
new_hover = ('    .more-work-card:hover { transform: scale(1.012); }\n'
             '    .mwc-scene {\n'
             '      position: absolute; inset: 0;\n'
             '      width: 100%; height: 100%;\n'
             '      display: block;\n'
             '    }\n'
             '    .mwc-content {')
if old_hover in content:
    content = content.replace(old_hover, new_hover, 1)
    sys.stdout.buffer.write(b'  OK: .mwc-scene CSS restored\n')
else:
    sys.stdout.buffer.write(b'  MISS: hover rule\n')

# ── 3. Replace More Work card HTML with mini flower SVG ─────────────
old_html = """      <!-- More work card — animated meadow scene -->
      <div class="more-work-card" id="more-work-card" role="button" tabindex="0" aria-label="Show all projects">

        <!-- Text overlay (positioned in sky area) -->
        <div class="mwc-content">
          <div class="mwc-label">9 projects total</div>
          <div class="mwc-title">More work</div>
          <div class="mwc-arrow">
            <svg viewBox="0 0 14 14" fill="none" stroke="currentColor" stroke-width="1.5"
                 stroke-linecap="round" stroke-linejoin="round">
              <path d="M2 7h10M8 3l4 4-4 4"/>
            </svg>
          </div>
        </div>
      </div>"""

new_html = """      <!-- More work card — mini hero flower scene -->
      <div class="more-work-card" id="more-work-card" role="button" tabindex="0" aria-label="Show all projects">
        <svg class="mwc-scene" viewBox="0 0 480 280" preserveAspectRatio="xMidYMid slice"
             xmlns="http://www.w3.org/2000/svg" aria-hidden="true">

          <!-- ① Background sage wash (reuses hero #ff-bg filter) -->
          <g filter="url(#ff-bg)" opacity="0.85">
            <rect width="480" height="280" fill="#c2c9b0"/>
            <ellipse cx="72"  cy="64"  rx="136" ry="108" fill="#b4c0a2"/>
            <ellipse cx="240" cy="84"  rx="168" ry="120" fill="#b0bc9c"/>
            <ellipse cx="420" cy="72"  rx="152" ry="124" fill="#b8c4a6"/>
            <ellipse cx="32"  cy="192" rx="120" ry="96"  fill="#aab896"/>
            <ellipse cx="200" cy="208" rx="152" ry="104" fill="#aeb89a"/>
            <ellipse cx="380" cy="200" rx="144" ry="112" fill="#b2be9e"/>
            <ellipse cx="136" cy="140" rx="128" ry="104" fill="#bcc8a8"/>
            <ellipse cx="304" cy="156" rx="136" ry="100" fill="#b6c2a4"/>
          </g>

          <!-- ② Mid-distance blooms (hf-mid animation, #ff-mid filter) -->
          <g class="hf-mid" filter="url(#ff-mid)" opacity="0.82">
            <ellipse cx="22"  cy="52"  rx="24" ry="18" fill="#b0a0c6"/>
            <ellipse cx="44"  cy="35"  rx="20" ry="15" fill="#c6b6d8"/>
            <ellipse cx="16"  cy="78"  rx="22" ry="16" fill="#a898ba"/>
            <ellipse cx="62"  cy="55"  rx="18" ry="14" fill="#d0a8b2"/>
            <ellipse cx="34"  cy="95"  rx="21" ry="15" fill="#ccbdd6"/>
            <ellipse cx="12"  cy="111" rx="23" ry="17" fill="#c2a8b4"/>
            <ellipse cx="70"  cy="77"  rx="18" ry="13" fill="#e4daca"/>
            <ellipse cx="102" cy="34"  rx="26" ry="19" fill="#baaece"/>
            <ellipse cx="127" cy="21"  rx="21" ry="16" fill="#cabcd8"/>
            <ellipse cx="91"  cy="63"  rx="22" ry="17" fill="#aa9cac"/>
            <ellipse cx="153" cy="39"  rx="23" ry="17" fill="#d6aaac"/>
            <ellipse cx="118" cy="71"  rx="19" ry="15" fill="#cebac0"/>
            <ellipse cx="84"  cy="91"  rx="25" ry="18" fill="#c2b2cc"/>
            <ellipse cx="140" cy="77"  rx="20" ry="15" fill="#e2d6ca"/>
            <ellipse cx="168" cy="65"  rx="18" ry="14" fill="#d8a8ac"/>
            <ellipse cx="110" cy="107" rx="22" ry="16" fill="#bcb0c6"/>
            <ellipse cx="195" cy="27"  rx="26" ry="20" fill="#c2b0d4"/>
            <ellipse cx="218" cy="15"  rx="22" ry="16" fill="#d2c2e2"/>
            <ellipse cx="184" cy="58"  rx="23" ry="18" fill="#baacc8"/>
            <ellipse cx="234" cy="37"  rx="24" ry="17" fill="#caa2ae"/>
            <ellipse cx="206" cy="73"  rx="21" ry="16" fill="#d6beca"/>
            <ellipse cx="173" cy="87"  rx="22" ry="17" fill="#cec0df"/>
            <ellipse cx="242" cy="63"  rx="19" ry="14" fill="#e6dace"/>
            <ellipse cx="221" cy="96"  rx="24" ry="18" fill="#bab4cc"/>
            <ellipse cx="195" cy="109" rx="21" ry="15" fill="#d2aab8"/>
            <ellipse cx="263" cy="31"  rx="26" ry="19" fill="#a8a0be"/>
            <ellipse cx="287" cy="18"  rx="21" ry="16" fill="#c4b6d6"/>
            <ellipse cx="254" cy="65"  rx="24" ry="18" fill="#baaec8"/>
            <ellipse cx="304" cy="40"  rx="23" ry="17" fill="#d2a6ae"/>
            <ellipse cx="275" cy="82"  rx="22" ry="16" fill="#c6bad8"/>
            <ellipse cx="321" cy="71"  rx="20" ry="15" fill="#dfc8ce"/>
            <ellipse cx="294" cy="101" rx="22" ry="17" fill="#e2d6c8"/>
            <ellipse cx="266" cy="114" rx="21" ry="16" fill="#caaab8"/>
            <ellipse cx="348" cy="29"  rx="26" ry="20" fill="#b2a4c4"/>
            <ellipse cx="371" cy="17"  rx="22" ry="16" fill="#c8bada"/>
            <ellipse cx="338" cy="61"  rx="25" ry="18" fill="#baacca"/>
            <ellipse cx="388" cy="40"  rx="24" ry="18" fill="#d4a6b0"/>
            <ellipse cx="359" cy="80"  rx="22" ry="17" fill="#c6bcda"/>
            <ellipse cx="404" cy="67"  rx="21" ry="16" fill="#dfd0ca"/>
            <ellipse cx="377" cy="99"  rx="23" ry="18" fill="#e2d2c4"/>
            <ellipse cx="349" cy="111" rx="22" ry="16" fill="#c0aac0"/>
            <ellipse cx="425" cy="25"  rx="27" ry="20" fill="#b6a8c6"/>
            <ellipse cx="447" cy="13"  rx="22" ry="17" fill="#c8bad8"/>
            <ellipse cx="415" cy="58"  rx="26" ry="19" fill="#aaa0bc"/>
            <ellipse cx="466" cy="36"  rx="25" ry="18" fill="#d4a8b2"/>
            <ellipse cx="434" cy="78"  rx="23" ry="18" fill="#c8b6c8"/>
            <ellipse cx="478" cy="56"  rx="22" ry="17" fill="#c0b2cc"/>
            <ellipse cx="457" cy="70"  rx="21" ry="16" fill="#e0d4c8"/>
            <ellipse cx="470" cy="94"  rx="22" ry="17" fill="#ccaab8"/>
            <ellipse cx="36"  cy="138" rx="27" ry="21" fill="#c2b0ca"/>
            <ellipse cx="100" cy="151" rx="25" ry="19" fill="#b6aabf"/>
            <ellipse cx="166" cy="131" rx="26" ry="20" fill="#cebcd2"/>
            <ellipse cx="231" cy="149" rx="26" ry="20" fill="#caacb8"/>
            <ellipse cx="298" cy="135" rx="28" ry="21" fill="#bab0c8"/>
            <ellipse cx="366" cy="151" rx="26" ry="20" fill="#d6b8c6"/>
            <ellipse cx="430" cy="138" rx="25" ry="19" fill="#bcb6cc"/>
            <ellipse cx="478" cy="147" rx="22" ry="18" fill="#caa4ae"/>
            <ellipse cx="64"  cy="43"  rx="21" ry="15" fill="#e6dece"/>
            <ellipse cx="192" cy="38"  rx="19" ry="14" fill="#ecdece"/>
            <ellipse cx="296" cy="47"  rx="22" ry="16" fill="#e8e0d2"/>
            <ellipse cx="400" cy="35"  rx="20" ry="15" fill="#ecdecb"/>
          </g>

          <!-- ③ Fine petal highlights (hf-detail animation, #ff-sm filter) -->
          <g class="hf-detail" filter="url(#ff-sm)" opacity="0.74">
            <ellipse cx="20"  cy="21"  rx="11" ry="8"  fill="#dcd4ec"/>
            <ellipse cx="52"  cy="14"  rx="9"  ry="7"  fill="#e8e0f2"/>
            <ellipse cx="87"  cy="20"  rx="12" ry="8"  fill="#d9cde8"/>
            <ellipse cx="123" cy="12"  rx="10" ry="7"  fill="#e4daee"/>
            <ellipse cx="159" cy="19"  rx="11" ry="8"  fill="#dfd6ea"/>
            <ellipse cx="195" cy="11"  rx="9"  ry="7"  fill="#e3d9ef"/>
            <ellipse cx="230" cy="18"  rx="12" ry="8"  fill="#d9d1e9"/>
            <ellipse cx="265" cy="12"  rx="10" ry="7"  fill="#e1d7ed"/>
            <ellipse cx="299" cy="19"  rx="11" ry="8"  fill="#d7cde7"/>
            <ellipse cx="335" cy="13"  rx="9"  ry="7"  fill="#ddd5eb"/>
            <ellipse cx="370" cy="18"  rx="12" ry="9"  fill="#e5dbf1"/>
            <ellipse cx="405" cy="11"  rx="10" ry="7"  fill="#d9d1e9"/>
            <ellipse cx="441" cy="19"  rx="11" ry="8"  fill="#e1d9ef"/>
            <ellipse cx="473" cy="14"  rx="9"  ry="6"  fill="#ddd5e9"/>
            <ellipse cx="68"  cy="39"  rx="8"  ry="6"  fill="#f0ece4"/>
            <ellipse cx="142" cy="34"  rx="9"  ry="6"  fill="#eee8de"/>
            <ellipse cx="214" cy="37"  rx="8"  ry="6"  fill="#f2ede6"/>
            <ellipse cx="286" cy="35"  rx="9"  ry="6"  fill="#ece6dc"/>
            <ellipse cx="357" cy="33"  rx="8"  ry="6"  fill="#f0ece2"/>
            <ellipse cx="429" cy="36"  rx="9"  ry="6"  fill="#eee8de"/>
            <ellipse cx="96"  cy="61"  rx="6"  ry="4"  fill="#d4907c"/>
            <ellipse cx="203" cy="55"  rx="5"  ry="4"  fill="#cc8870"/>
            <ellipse cx="310" cy="59"  rx="6"  ry="4"  fill="#d09080"/>
            <ellipse cx="417" cy="54"  rx="5"  ry="4"  fill="#c88878"/>
            <ellipse cx="51"  cy="98"  rx="6"  ry="4"  fill="#d09278"/>
            <ellipse cx="256" cy="102" rx="6"  ry="4"  fill="#cc8a70"/>
            <ellipse cx="462" cy="96"  rx="6"  ry="4"  fill="#d09278"/>
            <ellipse cx="38"  cy="118" rx="9"  ry="6"  fill="#d9d1e9"/>
            <ellipse cx="148" cy="123" rx="8"  ry="6"  fill="#e1d9ef"/>
            <ellipse cx="256" cy="118" rx="9"  ry="6"  fill="#d5cde7"/>
            <ellipse cx="362" cy="121" rx="8"  ry="6"  fill="#ddd5eb"/>
            <ellipse cx="464" cy="115" rx="9"  ry="6"  fill="#e5ddf1"/>
          </g>

          <!-- ④ Foreground bokeh (hf-fg animation, #ff-fg filter) -->
          <g class="hf-fg" filter="url(#ff-fg)" opacity="0.54">
            <ellipse cx="32"  cy="191" rx="51" ry="42" fill="#c2b2d6"/>
            <ellipse cx="106" cy="219" rx="57" ry="46" fill="#bab0d2"/>
            <ellipse cx="182" cy="203" rx="53" ry="43" fill="#ced0e0"/>
            <ellipse cx="256" cy="223" rx="59" ry="48" fill="#b6aece"/>
            <ellipse cx="332" cy="199" rx="54" ry="44" fill="#c6bad8"/>
            <ellipse cx="408" cy="219" rx="56" ry="46" fill="#bcb0d2"/>
            <ellipse cx="474" cy="204" rx="48" ry="39" fill="#c4b8d6"/>
            <ellipse cx="72"  cy="251" rx="61" ry="50" fill="#ceaabb"/>
            <ellipse cx="200" cy="259" rx="63" ry="51" fill="#caacb8"/>
            <ellipse cx="328" cy="255" rx="58" ry="47" fill="#d2b2be"/>
            <ellipse cx="448" cy="251" rx="56" ry="45" fill="#c8a8b8"/>
            <ellipse cx="48"  cy="269" rx="100" ry="47" fill="#9aac88"/>
            <ellipse cx="168" cy="276" rx="112" ry="42" fill="#9eae8c"/>
            <ellipse cx="288" cy="272" rx="106" ry="45" fill="#96a884"/>
            <ellipse cx="408" cy="267" rx="100" ry="48" fill="#9aaa86"/>
            <ellipse cx="14"  cy="166" rx="39" ry="32"  fill="#cec0d8"/>
            <ellipse cx="470" cy="170" rx="42" ry="34"  fill="#c2b4d4"/>
          </g>
        </svg>

        <div class="mwc-content">
          <div class="mwc-label">9 projects total</div>
          <div class="mwc-title">More work</div>
          <div class="mwc-arrow">
            <svg viewBox="0 0 14 14" fill="none" stroke="currentColor" stroke-width="1.5"
                 stroke-linecap="round" stroke-linejoin="round">
              <path d="M2 7h10M8 3l4 4-4 4"/>
            </svg>
          </div>
        </div>
      </div>"""

if old_html in content:
    content = content.replace(old_html, new_html, 1)
    sys.stdout.buffer.write(b'  OK: more-work-card HTML replaced\n')
else:
    sys.stdout.buffer.write(b'  MISS: more-work-card HTML\n')

changed = content != original
sys.stdout.buffer.write(f'Changed: {changed}\n'.encode())

if changed:
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    sys.stdout.buffer.write(b'Saved.\n')
