"""Chequeos estáticos de index.html.

Uso (desde la raíz del proyecto):  python3 -I doc/tools/check.py [archivo.html]

5. Cada bloque: exactamente 3 preguntas de desarrollo y 20 verdadero/falso con respuesta (data-a V/F).
6. Texto prohibido: menciones a los materiales de entrada (resúmenes) que no deben publicarse.

1. Balance de etiquetas HTML (parser de la biblioteca estándar).
2. Cada scrolly: el data-s máximo del diagrama no supera la cantidad de pasos.
3. ids duplicados y enlaces internos (#id) rotos.
4. Imágenes referenciadas que no existen en disco.
"""
import os
import re
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import sys
FILE = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "index.html")
src = open(FILE, encoding="utf-8").read()
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr",
        "path", "circle", "rect", "line", "ellipse", "polygon", "polyline", "stop", "use"}


class P(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack, self.err = [], []

    def handle_starttag(self, tag, attrs):
        if tag not in VOID:
            self.stack.append((tag, self.getpos()[0]))

    def handle_startendtag(self, tag, attrs):
        pass

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if self.stack and self.stack[-1][0] == tag:
            self.stack.pop()
        else:
            self.err.append("línea %d: </%s> no coincide con <%s> abierto en %s" % (
                self.getpos()[0], tag, self.stack[-1][0] if self.stack else "-", self.stack[-1][1] if self.stack else "-"))
            for i in range(len(self.stack) - 1, -1, -1):
                if self.stack[i][0] == tag:
                    del self.stack[i:]
                    break


p = P()
p.feed(src)
problems = p.err + ["sin cerrar: <%s> línea %d" % s for s in p.stack]

scrollies = re.split(r'<div class="scrolly', src)[1:]
n_sc = 0
for i, chunk in enumerate(scrollies):
    fig = chunk.split('<div class="fig">', 1)
    steps = len(re.findall(r'<div class="step"', fig[0]))
    svg = fig[1].split("</svg>", 1)[0] if len(fig) > 1 else ""
    ss = [int(x) for x in re.findall(r'data-s="(\d+)"', svg)]
    n_sc += 1
    if ss and max(ss) > steps:
        lab = re.search(r'aria-label="([^"]+)"', svg)
        problems.append("scrolly #%d (%s): data-s máx %d > %d pasos" % (i, lab.group(1) if lab else "?", max(ss), steps))
    if ss and steps > max(ss) + 1:
        lab = re.search(r'aria-label="([^"]+)"', svg)
        print("aviso: scrolly #%d (%s): %d pasos y data-s máx %d" % (i, lab.group(1) if lab else "?", steps, max(ss)))

ids = re.findall(r'\sid="([^"]+)"', src)
dup = sorted({x for x in ids if ids.count(x) > 1})
if dup:
    problems.append("ids duplicados: " + ", ".join(dup))
for ref in sorted(set(re.findall(r'href="#([^"]+)"', src))):
    if ref not in ids and "'" not in ref:
        problems.append("enlace roto: #" + ref)
for img in sorted(set(re.findall(r'src="(img/[^"]+)"', src))):
    if not os.path.exists(os.path.join(ROOT, img)):
        problems.append("imagen ausente: " + img)

# 5. anatomía de cada bloque
for m in re.finditer(r'<section class="bloque" id="([^"]+)"', src):
    end = src.find('<section class="bloque"', m.end())
    for alt in ('<section class="repaso"', '<header class="tema-h"'):
        k = src.find(alt, m.end())
        if k != -1 and (end == -1 or k < end):
            end = k
    chunk = src[m.start(): end if end != -1 else len(src)]
    nd = len(re.findall(r'<details class="preg dev"', chunk))
    vf = re.findall(r'<li data-a="([^"]*)"', chunk)
    if nd != 3:
        problems.append("%s: %d preguntas de desarrollo (deben ser 3)" % (m.group(1), nd))
    if len(vf) != 20 or any(a not in ("V", "F") for a in vf):
        problems.append("%s: %d V/F (deben ser 20 con data-a V o F)" % (m.group(1), len(vf)))
    elif not 7 <= vf.count("V") <= 13:
        problems.append("%s: V/F desbalanceado (%d V)" % (m.group(1), vf.count("V")))
    for need in ('class="lectura"', 'class="scrolly', 'class="quotes"', 'class="trampas"', '<details class="preg">', 'class="chip yr"'):
        if need not in chunk:
            problems.append("%s: falta %s" % (m.group(1), need))
# 6. texto prohibido
# la lista sensible (nombres) vive fuera de git, en trabajo/prohibido.txt (una cadena por línea)
BAD = ["recursos/", ".docx", ".pdf", "resumen de"]
_pf = os.path.join(ROOT, "trabajo", "prohibido.txt")
if os.path.exists(_pf):
    BAD += [x.strip() for x in open(_pf, encoding="utf-8") if x.strip()]
for bad in BAD:
    if bad.lower() in src.lower():
        problems.append("texto prohibido: %r" % bad)

print("%d scrollies, %d diagramas, %d bytes" % (n_sc, len(re.findall(r"<svg viewBox", src)), len(src.encode())))
print("\n".join(problems) if problems else "OK: sin problemas")
