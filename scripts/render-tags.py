import re, sys, yaml
sys.stdout.reconfigure(encoding="utf-8")
LEGACY = {'0':'000000','1':'0000AA','2':'00AA00','3':'00AAAA','4':'AA0000','5':'AA00AA','6':'FFAA00','7':'AAAAAA',
          '8':'555555','9':'5555FF','a':'55FF55','b':'55FFFF','c':'FF5555','d':'FF55FF','e':'FFFF55','f':'FFFFFF'}
def render(s):
    out, color, bold, buf = [], 'FFFFFF', False, ''
    def flush():
        nonlocal buf
        if buf:
            esc = buf.replace('&','&amp;').replace('<','&lt;')
            style = f'color:#{color}' + (';font-weight:700' if bold else '')
            out.append(f'<span style="{style}">{esc}</span>')
            buf = ''
    i = 0
    while i < len(s):
        m = re.match(r'#([0-9A-Fa-f]{6})', s[i:])
        if m:
            flush(); color, bold = m.group(1).upper(), False; i += 7; continue
        if s[i] == '&' and i + 1 < len(s) and s[i+1].lower() in '0123456789abcdefklmnor':
            c = s[i+1].lower(); flush()
            if c in LEGACY: color, bold = LEGACY[c], False
            elif c == 'l': bold = True
            elif c == 'r': color, bold = 'FFFFFF', False
            i += 2; continue
        buf += s[i]; i += 1
    flush()
    return '<span class="mc-tag">' + ''.join(out) + '</span>'
tags = yaml.safe_load(open(sys.argv[1], encoding='utf-8'))['deluxetags']
for k in sys.argv[2:]:
    print(k, render(tags[k]['tag']))
