# Writes one standalone HTML page per banner into src/ (A = network mesh, B = terminal,
# C = light roadmap; -x = X header, -li = LinkedIn background, -fb = Facebook cover).
# Then render them to PNG with render.mjs (see README.md).
import json, os
EX = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src')
os.makedirs(EX + '/img', exist_ok=True)
TERM = 'img/pose-terminal.png'; TERM_AR = 887/941
LAP = 'img/pose-laptop.png'; LAP_AR = 422/887
HERO = 'img/hero.png'; HERO_AR = 355/1100
FONTS = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Sora:wght@600;700&amp;family=IBM+Plex+Sans:wght@400;500&amp;family=JetBrains+Mono:wght@400;500&amp;display=swap">'
SIZES = {'x': (1500, 500), 'li': (1584, 396), 'fb': (1640, 624)}
PLAT = {'x': 'X header', 'li': 'LinkedIn background', 'fb': 'Facebook cover'}

def img(src, ar, left, top, h, extra=''):
    w = round(h * ar)
    return f'<img src="{src}" alt="" style="position: absolute; left: {left}px; top: {top}px; width: {w}px; height: {h}px; {extra}">'

def page(name, p, title, bg, body, lang='en'):
    w, h = SIZES[p]
    ex = f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<title>{title}</title>
{FONTS}
<style>
html,body{{margin:0;font-family:'IBM Plex Sans',sans-serif;color:#0b1f3f;overflow:hidden}}
</style>
</head>
<body>
<div style="position: relative; width: {w}px; height: {h}px; overflow: hidden; background: {bg}">
{body}
</div>
</body>
</html>
'''
    open(os.path.join(EX, name.replace('.dc.html', '.html')), 'w').write(ex)

# ---------- A: network mesh ----------
def mesh(w, h, nodes, links, bright=True):
    s = f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" style="position: absolute; left: 0; top: 0" aria-hidden="true">'
    # faint background lattice
    for i in range(0, w + 1, 120):
        s += f'<line x1="{i}" y1="0" x2="{i - 260}" y2="{h}" stroke="#1c3660" stroke-width="1"/>'
    for a, b in links:
        (x1, y1), (x2, y2) = nodes[a], nodes[b]
        s += f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#8ec5ff" stroke-opacity="0.55" stroke-width="2" stroke-dasharray="6 7"/>'
    for i, (x, y) in enumerate(nodes):
        s += f'<circle cx="{x}" cy="{y}" r="26" fill="#2563eb" fill-opacity="0.18"/>'
        s += f'<rect x="{x-14}" y="{y-16}" width="28" height="32" rx="5" fill="#0b1f3f" stroke="#8ec5ff" stroke-width="2"/>'
        s += f'<line x1="{x-8}" y1="{y-6}" x2="{x+8}" y2="{y-6}" stroke="#8ec5ff" stroke-width="2"/>'
        s += f'<line x1="{x-8}" y1="{y+4}" x2="{x+8}" y2="{y+4}" stroke="#8ec5ff" stroke-width="2"/>'
    s += '</svg>'
    return s

ALL = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
mono = "font-family: 'JetBrains Mono', monospace"
sora = "font-family: 'Sora', sans-serif"
def chips(items, size=17, fg='#e9e8e2', line='#2b4a7a'):
    return '<div style="display: flex; gap: 10px; flex-wrap: wrap">' + ''.join(
        f'<span style="{mono}; font-size: {size}px; color: {fg}; border: 1.5px solid {line}; border-radius: 999px; padding: 6px 14px">{t}</span>' for t in items) + '</div>'
STACK = ['Linux', 'Docker', 'WireGuard', 'PostgreSQL', 'Python']

page('A-x.dc.html', 'x', 'Mesh · X header', '#0b1f3f', f'''
{mesh(1500, 500, [(90,80),(310,70),(130,250),(330,240)], ALL)}
<div style="position: absolute; left: 110px; top: 300px; {mono}; font-size: 14px; color: #94a3bd; letter-spacing: 0.08em">wg0 · 4 nodes · 99.98%</div>
<div style="position: absolute; left: 430px; top: 92px; width: 640px; display: flex; flex-direction: column; gap: 22px">
<div style="{mono}; font-size: 19px; letter-spacing: 0.12em; color: #8ec5ff">DEVOPS ENGINEER · DATA SCIENCE</div>
<div style="{sora}; font-weight: 700; font-size: 50px; line-height: 1.12; color: #ffffff">I build and secure the infrastructure behind data‑driven products.</div>
{chips(STACK)}
<div style="{mono}; font-size: 19px; color: #8ec5ff">josuejunior.fleuridor.com</div>
</div>
{img(LAP, LAP_AR, 1150, 40, 700)}''')

stats_li = ''.join(f'<div style="display: flex; flex-direction: column; gap: 2px"><span style="{sora}; font-weight: 700; font-size: 34px; color: #ffffff">{v}</span><span style="{mono}; font-size: 14px; color: #b8c4d9">{l}</span></div>' for v, l in [('8+','years in production'),('99.98%','uptime, 4 servers'),('7','certifications'),('500+','students taught')])
page('A-li.dc.html', 'li', 'Mesh · LinkedIn background', '#0b1f3f', f'''
{mesh(1584, 396, [(80,60),(300,50),(120,200),(330,190)], ALL)}
<div style="position: absolute; left: 430px; top: 58px; width: 780px; display: flex; flex-direction: column; gap: 18px">
<div style="{mono}; font-size: 16px; letter-spacing: 0.12em; color: #8ec5ff">DEVOPS ENGINEER · DATA SCIENCE SPECIALIST</div>
<div style="{sora}; font-weight: 700; font-size: 38px; line-height: 1.15; color: #ffffff">I build and secure the infrastructure behind data‑driven products.</div>
<div style="display: flex; gap: 40px">{stats_li}</div>
</div>
{img(LAP, LAP_AR, 1270, 26, 560)}''')

page('A-fb.dc.html', 'fb', 'Mesh · Facebook cover', '#0b1f3f', f'''
{mesh(1640, 624, [(350,60),(580,100),(790,50),(960,105)], [(0,1),(1,2),(2,3),(0,2),(1,3)])}
<div style="position: absolute; left: 330px; top: 170px; width: 700px; display: flex; flex-direction: column; gap: 22px">
<div style="{mono}; font-size: 19px; letter-spacing: 0.12em; color: #8ec5ff">INGÉNIEUR DEVOPS · DATA SCIENCE</div>
<div style="{sora}; font-weight: 700; font-size: 54px; line-height: 1.12; color: #ffffff">Je construis et sécurise l’infrastructure des produits data.</div>
<div style="{mono}; font-size: 19px; color: #b8c4d9">Jacksonville, FL ↔ Cap‑Haïtien, Haïti</div>
<div style="{mono}; font-size: 19px; color: #8ec5ff">josuejunior.fleuridor.com/fr</div>
</div>
{img(LAP, LAP_AR, 1030, 70, 760)}''', lang='fr')

# ---------- B: terminal ----------
GRID = "#071429; background-image: linear-gradient(#0f2447 1px, transparent 1px), linear-gradient(90deg, #0f2447 1px, transparent 1px); background-size: 40px 40px"
def term(left, top, w, lines, fs=21, title='josue@lab: ~'):
    rows = ''
    for kind, t in lines:
        if kind == '$':
            rows += f'<div><span style="color: #8ec5ff">$</span> <span style="color: #ffffff">{t}</span></div>'
        elif kind == 'cur':
            rows += f'<div><span style="color: #8ec5ff">$</span> <span style="color: #ffffff">{t}</span><span style="display: inline-block; width: 0.6em; height: 1.05em; margin-left: 4px; vertical-align: -0.15em; background: #8ec5ff"></span></div>'
        else:
            rows += f'<div style="color: #b8c4d9; margin-bottom: 10px">{t}</div>'
    return f'''<div style="position: absolute; left: {left}px; top: {top}px; width: {w}px; background: #0b1f3f; border: 1.5px solid #2b4a7a; border-radius: 14px; overflow: hidden; box-shadow: 0 24px 60px rgba(0,0,0,0.35)">
<div style="display: flex; align-items: center; gap: 8px; padding: 12px 16px; background: #123061; border-bottom: 1.5px solid #1c3660">
<span style="width: 12px; height: 12px; border-radius: 50%; background: #2b4a7a"></span><span style="width: 12px; height: 12px; border-radius: 50%; background: #2b4a7a"></span><span style="width: 12px; height: 12px; border-radius: 50%; background: #2b4a7a"></span>
<span style="{mono}; font-size: 14px; color: #94a3bd; margin-left: 10px">{title}</span>
</div>
<div style="padding: 20px 24px; {mono}; font-size: {fs}px; line-height: 1.45">{rows}</div>
</div>'''
def bigstat(left, top, v, l, fs=64):
    return f'<div style="position: absolute; left: {left}px; top: {top}px; display: flex; flex-direction: column; gap: 4px"><span style="{sora}; font-weight: 700; font-size: {fs}px; color: #8ec5ff; line-height: 1">{v}</span><span style="{mono}; font-size: 15px; color: #b8c4d9">{l}</span></div>'

EN = [('$','whoami'),('o','Josué Junior Fleuridor · DevOps Engineer'),('$','uptime --fleet'),('o','4 servers · 99.98% uptime'),('$','ls ~/certs'),('o','security+  network+  linux+  clnp  cisco-ds'),('cur','open josuejunior.fleuridor.com')]
page('B-x.dc.html', 'x', 'Terminal · X header', GRID, f'''
{bigstat(70, 90, '99.98%', 'uptime across 4 servers')}
<div style="position: absolute; left: 70px; top: 200px; {mono}; font-size: 15px; color: #94a3bd">Linux · Docker · WireGuard</div>
{term(420, 64, 610, EN, fs=19)}
{img(TERM, TERM_AR, 1030, 30, 500)}''')

EN_LI = [('$','whoami'),('o','Josué Junior Fleuridor · DevOps Engineer · Data Science'),('$','uptime --fleet && ls ~/certs'),('o','4 servers · 99.98%  |  security+ network+ linux+ clnp'),('cur','open josuejunior.fleuridor.com')]
page('B-li.dc.html', 'li', 'Terminal · LinkedIn background', GRID, f'''
{bigstat(64, 50, '8+ yrs', 'running production systems', fs=54)}
{bigstat(64, 150, '500+', 'students taught', fs=40)}
{term(420, 34, 760, EN_LI, fs=18)}
{img(TERM, TERM_AR, 1190, 16, 390)}''')

FR = [('$','whoami'),('o','Josué Junior Fleuridor · Ingénieur DevOps'),('$','uptime --fleet'),('o','4 serveurs · 99,98 % de disponibilité'),('$','ls ~/parcours'),('o','haiti  jacksonville  devora'),('cur','open josuejunior.fleuridor.com/fr')]
page('B-fb.dc.html', 'fb', 'Terminal · Facebook cover', GRID, f'''
{term(300, 110, 580, FR, fs=20, title='josue@lab: ~')}
{img(TERM, TERM_AR, 882, 110, 520)}''', lang='fr')

# ---------- C: light roadmap ----------
def roadmap(left, top, steps, gap=48, fs=17):
    items = ''
    for i, (k, t) in enumerate(steps):
        last = i == len(steps) - 1
        dot = '#2563eb' if last else '#ffffff'
        items += f'''<div style="display: flex; flex-direction: column; gap: 10px; position: relative">
<div style="width: 18px; height: 18px; border-radius: 50%; background: {dot}; border: 3px solid #2563eb; box-sizing: border-box"></div>
<div style="{mono}; font-size: {fs-2}px; letter-spacing: 0.08em; color: #1d4ed8">{k}</div>
<div style="font-size: {fs}px; color: #0b1f3f; font-weight: 500">{t}</div>
</div>'''
    return f'''<div style="position: absolute; left: {left}px; top: {top}px">
<div style="position: absolute; left: 9px; right: 0; top: 8px; height: 2px; background: #c7d7fb"></div>
<div style="position: relative; display: flex; gap: {gap}px">{items}</div>
</div>'''
def stage(cx, cy, r):
    return f'<div style="position: absolute; left: {cx-r}px; top: {cy-r}px; width: {2*r}px; height: {2*r}px; border-radius: 50%; background: #e8f0fe; border: 2px solid #c7d7fb; box-sizing: border-box"></div>'

STEPS_EN = [('HAITI', '500+ students taught'), ('JACKSONVILLE', 'FinTech certificate, FSCJ'), ('TODAY', 'DevOps Engineer, Devora')]
page('C-x.dc.html', 'x', 'Roadmap · X header', '#f4f3ee', f'''
<div style="position: absolute; left: 60px; top: 60px; width: 300px; height: 240px; background-image: radial-gradient(#c7d7fb 2px, transparent 2px); background-size: 24px 24px"></div>
<div style="position: absolute; left: 430px; top: 80px; width: 640px; display: flex; flex-direction: column; gap: 20px">
<div style="{mono}; font-size: 18px; letter-spacing: 0.12em; color: #1d4ed8">DEVOPS ENGINEER · DATA SCIENCE SPECIALIST</div>
<div style="{sora}; font-weight: 700; font-size: 46px; line-height: 1.14; color: #0b1f3f">From teaching Linux in Haiti to running production at 99.98%.</div>
</div>
{roadmap(432, 330, STEPS_EN)}
{stage(1300, 300, 190)}
{img(HERO, HERO_AR, 1160, 50, 900)}''')

page('C-li.dc.html', 'li', 'Roadmap · LinkedIn background', '#f4f3ee', f'''
<div style="position: absolute; left: 60px; top: 40px; width: 300px; height: 180px; background-image: radial-gradient(#c7d7fb 2px, transparent 2px); background-size: 24px 24px"></div>
<div style="position: absolute; left: 430px; top: 50px; width: 760px; display: flex; flex-direction: column; gap: 14px">
<div style="{mono}; font-size: 15px; letter-spacing: 0.12em; color: #1d4ed8">DEVOPS ENGINEER · DATA SCIENCE SPECIALIST</div>
<div style="{sora}; font-weight: 700; font-size: 36px; line-height: 1.15; color: #0b1f3f">From teaching Linux in Haiti to running production at 99.98%.</div>
</div>
{roadmap(432, 240, STEPS_EN, gap=56, fs=16)}
{stage(1380, 220, 160)}
{img(HERO, HERO_AR, 1262, 30, 720)}''')

STEPS_FR = [('HAÏTI', '500+ étudiants formés'), ('JACKSONVILLE', 'Certificat FinTech, FSCJ'), ('AUJOURD’HUI', 'Ingénieur DevOps, Devora')]
page('C-fb.dc.html', 'fb', 'Roadmap · Facebook cover', '#f4f3ee', f'''
<div style="position: absolute; left: 330px; top: 130px; width: 700px; display: flex; flex-direction: column; gap: 20px">
<div style="{mono}; font-size: 18px; letter-spacing: 0.12em; color: #1d4ed8">INGÉNIEUR DEVOPS · DATA SCIENCE</div>
<div style="{sora}; font-weight: 700; font-size: 48px; line-height: 1.14; color: #0b1f3f">De l’enseignement de Linux en Haïti à la production à 99,98 %.</div>
</div>
{roadmap(332, 420, STEPS_FR, gap=44)}
{stage(1210, 330, 190)}
{img(HERO, HERO_AR, 1070, 70, 980)}''', lang='fr')

print('wrote', sorted(f for f in os.listdir(EX) if f.endswith('.html')))
