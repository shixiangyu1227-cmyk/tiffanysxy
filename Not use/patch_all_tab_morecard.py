import re, sys

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()
original = content

# ── 1. Add ALL tab after AI-Powered ────────────────────────────────
old_tail = '      <button class="work-tab" data-tab="ai-powered" role="tab" aria-selected="false">AI-Powered</button>\n    </div>'
new_tail = ('      <button class="work-tab" data-tab="ai-powered" role="tab" aria-selected="false">AI-Powered</button>\n'
            '      <span class="work-tab-sep" aria-hidden="true">&middot;</span>\n'
            '      <button class="work-tab" data-tab="all" role="tab" aria-selected="false">All</button>\n'
            '    </div>')
if old_tail in content:
    content = content.replace(old_tail, new_tail, 1)
    sys.stdout.buffer.write(b'  OK: ALL tab added\n')
else:
    sys.stdout.buffer.write(b'  MISS: tab tail not found\n')

# ── 2. Update JS filterCards to handle 'all' ───────────────────────
old_match = "          const match = card.dataset.category.split(' ').includes(cat);"
new_match  = "          const match = cat === 'all' || card.dataset.category.split(' ').includes(cat);"
if old_match in content:
    content = content.replace(old_match, new_match, 1)
    sys.stdout.buffer.write(b'  OK: filterCards updated for all\n')
else:
    sys.stdout.buffer.write(b'  MISS: filterCards match line\n')

# ── 3. Replace more-work-card CSS block ────────────────────────────
old_css = """    /* ─── MORE WORK CARD ─────────────────────────────── */
    .more-work-card {
      display: none;
      background: rgba(255,255,255,.18);
      backdrop-filter: blur(18px) saturate(1.4);
      -webkit-backdrop-filter: blur(18px) saturate(1.4);
      border: 1px solid rgba(255,255,255,.35);
      box-shadow: inset 0 1px 0 rgba(255,255,255,.45), 0 8px 32px rgba(58,74,46,.12);
      cursor: none;
      align-items: center; justify-content: center;
      flex-direction: column;
      gap: .75rem;
      min-height: 220px;
      transition: background .3s var(--ease), box-shadow .3s var(--ease);
      text-decoration: none;
    }
    .more-work-card.visible { display: flex; }
    .more-work-card:hover {
      background: rgba(255,255,255,.28);
      box-shadow: inset 0 1px 0 rgba(255,255,255,.55), 0 12px 40px rgba(58,74,46,.18);
    }
    .more-work-card-label {
      font-family: var(--font-mon); font-size: .7rem;
      letter-spacing: .18em; text-transform: uppercase;
      color: rgba(58,74,46,.6);
    }
    .more-work-card-text {
      font-family: var(--font-serif); font-size: 1.85rem;
      font-weight: 400; color: var(--ink);
      line-height: 1.1;
    }
    .more-work-card-arrow {
      width: 38px; height: 38px;
      border: 1.5px solid rgba(58,74,46,.3);
      border-radius: 50%;
      display: flex; align-items: center; justify-content: center;
      margin-top: .3rem;
      transition: border-color .3s, transform .3s var(--ease);
    }
    .more-work-card:hover .more-work-card-arrow {
      border-color: rgba(58,74,46,.8);
      transform: translateX(4px);
    }
    .more-work-card-arrow svg { width: 14px; height: 14px; }"""

new_css = """    /* ─── MORE WORK CARD — Meadow Scene ──────────────── */
    .more-work-card {
      display: none;
      position: relative;
      overflow: hidden;
      cursor: none;
      min-height: 220px;
      transition: transform .4s var(--ease);
    }
    .more-work-card.visible { display: block; }
    .more-work-card:hover { transform: scale(1.012); }
    .mwc-scene {
      position: absolute; inset: 0;
      width: 100%; height: 100%;
      display: block;
    }
    .mwc-content {
      position: absolute;
      top: 38%; left: 50%;
      transform: translate(-50%, -50%);
      display: flex; flex-direction: column;
      align-items: center; gap: .5rem;
      z-index: 2; text-align: center;
      pointer-events: none;
    }
    .mwc-label {
      font-family: var(--font-mon); font-size: .65rem;
      letter-spacing: .18em; text-transform: uppercase;
      color: rgba(255,255,255,.95);
      background: rgba(35,60,18,.32);
      backdrop-filter: blur(6px);
      -webkit-backdrop-filter: blur(6px);
      padding: .28rem .9rem; border-radius: 100px;
      border: 1px solid rgba(255,255,255,.22);
    }
    .mwc-title {
      font-family: var(--font-serif); font-size: 2.1rem;
      font-weight: 400; font-style: italic;
      color: rgba(255,255,255,.98);
      text-shadow: 0 2px 18px rgba(22,45,10,.45);
      line-height: 1;
    }
    .mwc-arrow {
      width: 36px; height: 36px;
      border: 1.5px solid rgba(255,255,255,.65);
      border-radius: 50%;
      display: flex; align-items: center; justify-content: center;
      margin-top: .1rem;
      transition: border-color .3s, transform .3s var(--ease);
      color: white;
    }
    .more-work-card:hover .mwc-arrow {
      border-color: white;
      transform: translateX(4px);
    }
    .mwc-arrow svg { width: 13px; height: 13px; }"""

if old_css in content:
    content = content.replace(old_css, new_css, 1)
    sys.stdout.buffer.write(b'  OK: more-work-card CSS replaced\n')
else:
    sys.stdout.buffer.write(b'  MISS: more-work-card CSS block\n')

# ── 4. Replace more-work-card HTML ─────────────────────────────────
old_html = """      <!-- More work card — visible only in Design tab, triggers All view -->
      <div class="more-work-card" id="more-work-card" role="button" tabindex="0" aria-label="Show all projects">
        <div class="more-work-card-label">9 projects total</div>
        <div class="more-work-card-text">More work</div>
        <div class="more-work-card-arrow">
          <svg viewBox="0 0 14 14" fill="none" stroke="var(--ink)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
            <path d="M2 7h10M8 3l4 4-4 4"/>
          </svg>
        </div>
      </div>"""

new_html = """      <!-- More work card — animated meadow scene -->
      <div class="more-work-card" id="more-work-card" role="button" tabindex="0" aria-label="Show all projects">
        <!-- Scenic SVG: sky · clouds · hills · wildflowers -->
        <svg class="mwc-scene" viewBox="0 0 480 280" preserveAspectRatio="xMidYMid slice"
             xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
          <defs>
            <linearGradient id="mwc-sky-g" x1="0" y1="0" x2="0" y2="1">
              <stop offset="0%"   stop-color="#9ed4ee"/>
              <stop offset="52%"  stop-color="#c0dfa0"/>
              <stop offset="100%" stop-color="#8db56c"/>
            </linearGradient>
          </defs>
          <!-- Sky -->
          <rect width="480" height="280" fill="url(#mwc-sky-g)"/>

          <!-- Cloud A — drifts right -->
          <g>
            <animateTransform attributeName="transform" type="translate"
              values="0,0; 24,0; 0,0" dur="10s"
              calcMode="spline" keySplines="0.45 0 0.55 1;0.45 0 0.55 1"
              repeatCount="indefinite"/>
            <ellipse cx="95"  cy="60"  rx="52" ry="25" fill="white" opacity=".88"/>
            <ellipse cx="70"  cy="70"  rx="34" ry="21" fill="white" opacity=".88"/>
            <ellipse cx="120" cy="70"  rx="38" ry="21" fill="white" opacity=".88"/>
          </g>

          <!-- Cloud B — drifts left -->
          <g>
            <animateTransform attributeName="transform" type="translate"
              values="0,0; -20,0; 0,0" dur="14s"
              calcMode="spline" keySplines="0.45 0 0.55 1;0.45 0 0.55 1"
              repeatCount="indefinite"/>
            <ellipse cx="290" cy="44"  rx="42" ry="21" fill="white" opacity=".78"/>
            <ellipse cx="269" cy="54"  rx="25" ry="16" fill="white" opacity=".78"/>
            <ellipse cx="313" cy="54"  rx="29" ry="16" fill="white" opacity=".78"/>
          </g>

          <!-- Cloud C — drifts right, slower -->
          <g>
            <animateTransform attributeName="transform" type="translate"
              values="0,0; 16,0; 0,0" dur="12s"
              calcMode="spline" keySplines="0.45 0 0.55 1;0.45 0 0.55 1"
              repeatCount="indefinite"/>
            <ellipse cx="425" cy="57"  rx="34" ry="17" fill="white" opacity=".70"/>
            <ellipse cx="407" cy="66"  rx="21" ry="13" fill="white" opacity=".70"/>
            <ellipse cx="445" cy="66"  rx="24" ry="13" fill="white" opacity=".70"/>
          </g>

          <!-- Far hill -->
          <path d="M0,155 Q80,95 160,125 Q240,155 320,115 Q380,88 480,105 L480,280 L0,280 Z"
                fill="#8ab46a"/>

          <!-- Mid hill -->
          <path d="M0,180 Q70,140 150,162 Q230,185 310,152 Q370,132 480,158 L480,280 L0,280 Z"
                fill="#5d8e3c"/>

          <!-- Small purple flower on mid hill (160,160) -->
          <g transform="translate(160,160)">
            <g><animateTransform attributeName="transform" type="rotate"
              values="-4,0,0; 4,0,0; -4,0,0" dur="3.0s" begin="0.5s"
              calcMode="spline" keySplines="0.45 0 0.55 1;0.45 0 0.55 1"
              repeatCount="indefinite"/>
              <line x1="0" y1="0" x2="0" y2="-14" stroke="#3d7028" stroke-width="1.2"/>
              <circle cx="0"  cy="-21" r="3"   fill="#8b5cc8" opacity=".85"/>
              <circle cx="5"  cy="-18" r="3"   fill="#9467d4" opacity=".80"/>
              <circle cx="5"  cy="-12" r="3"   fill="#9467d4" opacity=".80"/>
              <circle cx="0"  cy="-9"  r="3"   fill="#8b5cc8" opacity=".85"/>
              <circle cx="-5" cy="-12" r="3"   fill="#9467d4" opacity=".80"/>
              <circle cx="-5" cy="-18" r="3"   fill="#9467d4" opacity=".80"/>
              <circle cx="0"  cy="-15" r="2.5" fill="#f0d040"/>
            </g>
          </g>

          <!-- Small purple flower on mid hill (340,143) -->
          <g transform="translate(340,143)">
            <g><animateTransform attributeName="transform" type="rotate"
              values="4,0,0; -4,0,0; 4,0,0" dur="2.8s" begin="1.2s"
              calcMode="spline" keySplines="0.45 0 0.55 1;0.45 0 0.55 1"
              repeatCount="indefinite"/>
              <line x1="0" y1="0" x2="0" y2="-13" stroke="#3d7028" stroke-width="1.2"/>
              <circle cx="0"  cy="-20" r="3"   fill="#8b5cc8" opacity=".85"/>
              <circle cx="5"  cy="-17" r="3"   fill="#9467d4" opacity=".80"/>
              <circle cx="5"  cy="-11" r="3"   fill="#9467d4" opacity=".80"/>
              <circle cx="0"  cy="-8"  r="3"   fill="#8b5cc8" opacity=".85"/>
              <circle cx="-5" cy="-11" r="3"   fill="#9467d4" opacity=".80"/>
              <circle cx="-5" cy="-17" r="3"   fill="#9467d4" opacity=".80"/>
              <circle cx="0"  cy="-14" r="2.5" fill="#f0d040"/>
            </g>
          </g>

          <!-- Near hill (foreground) -->
          <path d="M0,210 Q60,188 130,200 Q200,213 280,195 Q340,182 480,205 L480,280 L0,280 Z"
                fill="#3a6a22"/>

          <!-- Purple flower 1 (55,202) -->
          <g transform="translate(55,202)">
            <g><animateTransform attributeName="transform" type="rotate"
              values="-5,0,0; 5,0,0; -5,0,0" dur="3.2s" begin="0s"
              calcMode="spline" keySplines="0.45 0 0.55 1;0.45 0 0.55 1"
              repeatCount="indefinite"/>
              <line x1="0" y1="0" x2="0" y2="-18" stroke="#2e5c1a" stroke-width="1.5"/>
              <circle cx="0"    cy="-31.5" r="4.5" fill="#8b5cc8" opacity=".90"/>
              <circle cx="5.6"  cy="-28.3" r="4.5" fill="#9467d4" opacity=".88"/>
              <circle cx="5.6"  cy="-21.7" r="4.5" fill="#9467d4" opacity=".88"/>
              <circle cx="0"    cy="-18.5" r="4.5" fill="#8b5cc8" opacity=".90"/>
              <circle cx="-5.6" cy="-21.7" r="4.5" fill="#9467d4" opacity=".88"/>
              <circle cx="-5.6" cy="-28.3" r="4.5" fill="#9467d4" opacity=".88"/>
              <circle cx="0"    cy="-25"   r="4"   fill="#f0d040"/>
            </g>
          </g>

          <!-- Red flower 1 (85,196) -->
          <g transform="translate(85,196)">
            <g><animateTransform attributeName="transform" type="rotate"
              values="-6,0,0; 4,0,0; -6,0,0" dur="2.5s" begin="0.6s"
              calcMode="spline" keySplines="0.45 0 0.55 1;0.45 0 0.55 1"
              repeatCount="indefinite"/>
              <line x1="0" y1="0" x2="0" y2="-18" stroke="#2e5c1a" stroke-width="1.5"/>
              <ellipse cx="0"  cy="-30" rx="5" ry="6" fill="#c94060" opacity=".90"/>
              <ellipse cx="7"  cy="-24" rx="6" ry="5" fill="#c94060" opacity=".90"/>
              <ellipse cx="0"  cy="-18" rx="5" ry="6" fill="#d4506e" opacity=".85"/>
              <ellipse cx="-7" cy="-24" rx="6" ry="5" fill="#d4506e" opacity=".85"/>
              <circle  cx="0"  cy="-24" r="3.5" fill="#1a0a00" opacity=".75"/>
              <circle  cx="0"  cy="-24" r="1.5" fill="#f0d040" opacity=".90"/>
            </g>
          </g>

          <!-- Purple flower 2 (125,200) -->
          <g transform="translate(125,200)">
            <g><animateTransform attributeName="transform" type="rotate"
              values="4,0,0; -4,0,0; 4,0,0" dur="2.8s" begin="1.2s"
              calcMode="spline" keySplines="0.45 0 0.55 1;0.45 0 0.55 1"
              repeatCount="indefinite"/>
              <line x1="0" y1="0" x2="0" y2="-18" stroke="#2e5c1a" stroke-width="1.5"/>
              <circle cx="0"    cy="-31.5" r="4.5" fill="#a070e0" opacity=".90"/>
              <circle cx="5.6"  cy="-28.3" r="4.5" fill="#9467d4" opacity=".88"/>
              <circle cx="5.6"  cy="-21.7" r="4.5" fill="#9467d4" opacity=".88"/>
              <circle cx="0"    cy="-18.5" r="4.5" fill="#a070e0" opacity=".90"/>
              <circle cx="-5.6" cy="-21.7" r="4.5" fill="#9467d4" opacity=".88"/>
              <circle cx="-5.6" cy="-28.3" r="4.5" fill="#9467d4" opacity=".88"/>
              <circle cx="0"    cy="-25"   r="4"   fill="#f0d040"/>
            </g>
          </g>

          <!-- Red flower 2 (175,207) -->
          <g transform="translate(175,207)">
            <g><animateTransform attributeName="transform" type="rotate"
              values="4,0,0; -5,0,0; 4,0,0" dur="3.0s" begin="0.3s"
              calcMode="spline" keySplines="0.45 0 0.55 1;0.45 0 0.55 1"
              repeatCount="indefinite"/>
              <line x1="0" y1="0" x2="0" y2="-18" stroke="#2e5c1a" stroke-width="1.5"/>
              <ellipse cx="0"  cy="-30" rx="5" ry="6" fill="#d44060" opacity=".90"/>
              <ellipse cx="7"  cy="-24" rx="6" ry="5" fill="#c93050" opacity=".90"/>
              <ellipse cx="0"  cy="-18" rx="5" ry="6" fill="#d44060" opacity=".85"/>
              <ellipse cx="-7" cy="-24" rx="6" ry="5" fill="#c93050" opacity=".85"/>
              <circle  cx="0"  cy="-24" r="3.5" fill="#1a0a00" opacity=".75"/>
              <circle  cx="0"  cy="-24" r="1.5" fill="#f0d040" opacity=".90"/>
            </g>
          </g>

          <!-- Purple flower 3 (235,206) -->
          <g transform="translate(235,206)">
            <g><animateTransform attributeName="transform" type="rotate"
              values="-5,0,0; 5,0,0; -5,0,0" dur="3.5s" begin="0.9s"
              calcMode="spline" keySplines="0.45 0 0.55 1;0.45 0 0.55 1"
              repeatCount="indefinite"/>
              <line x1="0" y1="0" x2="0" y2="-18" stroke="#2e5c1a" stroke-width="1.5"/>
              <circle cx="0"    cy="-31.5" r="4.5" fill="#8b5cc8" opacity=".90"/>
              <circle cx="5.6"  cy="-28.3" r="4.5" fill="#9467d4" opacity=".88"/>
              <circle cx="5.6"  cy="-21.7" r="4.5" fill="#9467d4" opacity=".88"/>
              <circle cx="0"    cy="-18.5" r="4.5" fill="#8b5cc8" opacity=".90"/>
              <circle cx="-5.6" cy="-21.7" r="4.5" fill="#9467d4" opacity=".88"/>
              <circle cx="-5.6" cy="-28.3" r="4.5" fill="#9467d4" opacity=".88"/>
              <circle cx="0"    cy="-25"   r="4"   fill="#f0d040"/>
            </g>
          </g>

          <!-- Red flower 3 (305,196) -->
          <g transform="translate(305,196)">
            <g><animateTransform attributeName="transform" type="rotate"
              values="-6,0,0; 4,0,0; -6,0,0" dur="2.6s" begin="0.2s"
              calcMode="spline" keySplines="0.45 0 0.55 1;0.45 0 0.55 1"
              repeatCount="indefinite"/>
              <line x1="0" y1="0" x2="0" y2="-18" stroke="#2e5c1a" stroke-width="1.5"/>
              <ellipse cx="0"  cy="-30" rx="5" ry="6" fill="#c04050" opacity=".90"/>
              <ellipse cx="7"  cy="-24" rx="6" ry="5" fill="#c04050" opacity=".90"/>
              <ellipse cx="0"  cy="-18" rx="5" ry="6" fill="#c94060" opacity=".85"/>
              <ellipse cx="-7" cy="-24" rx="6" ry="5" fill="#c94060" opacity=".85"/>
              <circle  cx="0"  cy="-24" r="3.5" fill="#1a0a00" opacity=".75"/>
              <circle  cx="0"  cy="-24" r="1.5" fill="#f0d040" opacity=".90"/>
            </g>
          </g>

          <!-- Purple flower 4 (365,188) -->
          <g transform="translate(365,188)">
            <g><animateTransform attributeName="transform" type="rotate"
              values="4,0,0; -4,0,0; 4,0,0" dur="3.1s" begin="1.5s"
              calcMode="spline" keySplines="0.45 0 0.55 1;0.45 0 0.55 1"
              repeatCount="indefinite"/>
              <line x1="0" y1="0" x2="0" y2="-18" stroke="#2e5c1a" stroke-width="1.5"/>
              <circle cx="0"    cy="-31.5" r="4.5" fill="#9870d8" opacity=".90"/>
              <circle cx="5.6"  cy="-28.3" r="4.5" fill="#a070e0" opacity=".88"/>
              <circle cx="5.6"  cy="-21.7" r="4.5" fill="#a070e0" opacity=".88"/>
              <circle cx="0"    cy="-18.5" r="4.5" fill="#9870d8" opacity=".90"/>
              <circle cx="-5.6" cy="-21.7" r="4.5" fill="#a070e0" opacity=".88"/>
              <circle cx="-5.6" cy="-28.3" r="4.5" fill="#a070e0" opacity=".88"/>
              <circle cx="0"    cy="-25"   r="4"   fill="#f0d040"/>
            </g>
          </g>

          <!-- Purple flower 5 (430,202) -->
          <g transform="translate(430,202)">
            <g><animateTransform attributeName="transform" type="rotate"
              values="-5,0,0; 5,0,0; -5,0,0" dur="2.9s" begin="0.7s"
              calcMode="spline" keySplines="0.45 0 0.55 1;0.45 0 0.55 1"
              repeatCount="indefinite"/>
              <line x1="0" y1="0" x2="0" y2="-18" stroke="#2e5c1a" stroke-width="1.5"/>
              <circle cx="0"    cy="-31.5" r="4.5" fill="#8b5cc8" opacity=".90"/>
              <circle cx="5.6"  cy="-28.3" r="4.5" fill="#9467d4" opacity=".88"/>
              <circle cx="5.6"  cy="-21.7" r="4.5" fill="#9467d4" opacity=".88"/>
              <circle cx="0"    cy="-18.5" r="4.5" fill="#8b5cc8" opacity=".90"/>
              <circle cx="-5.6" cy="-21.7" r="4.5" fill="#9467d4" opacity=".88"/>
              <circle cx="-5.6" cy="-28.3" r="4.5" fill="#9467d4" opacity=".88"/>
              <circle cx="0"    cy="-25"   r="4"   fill="#f0d040"/>
            </g>
          </g>
        </svg>

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

if old_html in content:
    content = content.replace(old_html, new_html, 1)
    sys.stdout.buffer.write(b'  OK: more-work-card HTML replaced\n')
else:
    sys.stdout.buffer.write(b'  MISS: more-work-card HTML\n')

# ── Summary ─────────────────────────────────────────────────────────
changed = content != original
sys.stdout.buffer.write(f'Changed: {changed}\n'.encode())

if changed:
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    sys.stdout.buffer.write(b'Saved.\n')
