# -*- coding: utf-8 -*-
"""Small SVG drawing helpers for the book's diagrams.

Run `python build.py` in this folder to regenerate every image in ../ (Book/images).
Each diagram is a plain SVG with its own light background, so it reads the same
in a dark or a light Markdown preview.
"""
import html
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.normpath(os.path.join(HERE, '..'))
FONT = "'Segoe UI', 'Noto Sans', Helvetica, Arial, sans-serif"
MONO = "Consolas, 'Cascadia Mono', 'Courier New', monospace"
INK, INK2, MUTED = '#1c1c1a', '#52514e', '#7a7974'
SURF, EDGE, GRID = '#fcfcfb', '#d9d7d0', '#e7e5df'
LIFE = '#b9b7b0'
# name: (soft fill, strong stroke)
C = {
    'blue':   ('#e6f0fc', '#2a78d6'),
    'green':  ('#e1f5ec', '#16996a'),
    'orange': ('#fdeadf', '#e0602c'),
    'yellow': ('#fdf2d3', '#cf8d00'),
    'violet': ('#ebe8fb', '#6250d6'),
    'red':    ('#fde6e6', '#d93f3e'),
    'grey':   ('#f1f0ec', '#8a8984'),
    'white':  ('#ffffff', '#b3b1aa'),
}
ALL = []
TITLES = {}


def tw(t, size, bold=False, mono=False):
    """Rough text width in px."""
    if mono:
        return len(t) * size * 0.55
    return len(t) * size * (0.56 if bold else 0.52)


def esc(t):
    return html.escape(str(t), quote=True)


class D:
    def __init__(self, name, h, title, sub=None, w=760):
        self.name, self.w, self.h = name, w, h
        self.e, self.warn = [], []
        self.title = title
        self._lx = []
        self.text(24, 32, title, size=16, anchor='start', weight='700')
        if sub:
            self.text(24, 51, sub, size=12.5, anchor='start', fill=INK2)

    # ---- primitives -------------------------------------------------
    def raw(self, s):
        self.e.append(s)

    def text(self, x, y, t, size=12.5, anchor='middle', fill=INK, weight='400',
             mono=False, italic=False, lh=1.3):
        fam = MONO if mono else FONT
        st = ' font-style="italic"' if italic else ''
        for i, line in enumerate(str(t).split('\n')):
            yy = y + i * size * lh
            self.e.append(
                '<text x="%.1f" y="%.1f" font-family="%s" font-size="%s" font-weight="%s" '
                'fill="%s" text-anchor="%s"%s>%s</text>'
                % (x, yy, FONT if not mono else MONO, size, weight, fill, anchor, st, esc(line)))
            wd = tw(line, size, weight in ('600', '700'), mono)
            x0 = x - wd / 2 if anchor == 'middle' else (x - wd if anchor == 'end' else x)
            if x0 < 6 or x0 + wd > self.w - 6 or yy > self.h - 5:
                self.warn.append('text outside canvas: %r' % line)

    def rect(self, x, y, w, h, fill, stroke='none', rx=0, sw=1.5, dash=False, opacity=None):
        da = ' stroke-dasharray="5 4"' if dash else ''
        op = ' opacity="%s"' % opacity if opacity is not None else ''
        self.e.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%s" fill="%s" '
                      'stroke="%s" stroke-width="%s"%s%s/>' % (x, y, w, h, rx, fill, stroke, sw, da, op))

    def line(self, x1, y1, x2, y2, color=EDGE, lw=1, dash=False):
        da = ' stroke-dasharray="5 4"' if dash else ''
        self.e.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="%s" '
                      'stroke-linecap="round"%s/>' % (x1, y1, x2, y2, color, lw, da))

    def circle(self, cx, cy, r, fill, stroke='none', sw=1.5, dash=False):
        da = ' stroke-dasharray="5 4"' if dash else ''
        self.e.append('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s" stroke="%s" stroke-width="%s"%s/>'
                      % (cx, cy, r, fill, stroke, sw, da))

    def poly(self, pts, fill, stroke='none', sw=1.5):
        p = ' '.join('%.1f,%.1f' % (x, y) for x, y in pts)
        self.e.append('<polygon points="%s" fill="%s" stroke="%s" stroke-width="%s" stroke-linejoin="round"/>'
                      % (p, fill, stroke, sw))

    def polyline(self, pts, color, lw=2, dash=False):
        p = ' '.join('%.1f,%.1f' % (x, y) for x, y in pts)
        da = ' stroke-dasharray="5 4"' if dash else ''
        self.e.append('<polyline points="%s" fill="none" stroke="%s" stroke-width="%s" '
                      'stroke-linejoin="round" stroke-linecap="round"%s/>' % (p, color, lw, da))

    # ---- shapes with labels ----------------------------------------
    def _labels(self, x, y, w, h, label, sub, size, subsize, weight, mono, submono, ink, subink):
        L = str(label).split('\n') if label else []
        S = str(sub).split('\n') if sub else []
        subsize = subsize or max(size - 1.5, 10.5)
        lh1, lh2 = size * 1.25, subsize * 1.3
        gap = 2 if (L and S) else 0
        total = len(L) * lh1 + len(S) * lh2 + gap
        top = y + (h - total) / 2
        cx = x + w / 2
        for i, l in enumerate(L):
            self.text(cx, top + i * lh1 + lh1 / 2 + size * 0.35, l, size=size, weight=weight, mono=mono, fill=ink)
            if tw(l, size, weight in ('600', '700'), mono) > w - 2:
                self.warn.append('label wider than box: %r' % l)
        top2 = top + len(L) * lh1 + gap
        for i, l in enumerate(S):
            self.text(cx, top2 + i * lh2 + lh2 / 2 + subsize * 0.35, l, size=subsize, mono=submono, fill=subink)
            if tw(l, subsize, False, submono) > w - 2:
                self.warn.append('sub-label wider than box: %r' % l)
        if total > h - 2:
            self.warn.append('labels taller than box: %r' % label)

    def box(self, x, y, w, h, label='', color='blue', sub=None, size=12.5, subsize=None, r=8,
            weight='600', mono=False, submono=False, dash=False, sw=1.5, fill=None, stroke=None,
            ink=INK, subink=INK2):
        f, st = C[color]
        self.rect(x, y, w, h, fill or f, stroke or st, rx=r, sw=sw, dash=dash)
        self._labels(x, y, w, h, label, sub, size, subsize, weight, mono, submono, ink, subink)
        return (x, y, w, h)

    def group(self, x, y, w, h, label=None):
        self.rect(x, y, w, h, '#f6f5f1', EDGE, rx=10, sw=1.2, dash=True)
        if label:
            self.text(x + 12, y + 18, label, size=11.5, anchor='start', fill=INK2, weight='600')
        return (x, y, w, h)

    def pill(self, cx, y, label, color='grey', size=11.5, weight='600'):
        w = tw(label, size, True) + 22
        h = size + 11
        f, st = C[color]
        self.rect(cx - w / 2, y, w, h, f, st, rx=h / 2, sw=1.2)
        self.text(cx, y + h / 2 + size * 0.35, label, size=size, weight=weight)
        return (cx - w / 2, y, w, h)

    def diamond(self, cx, cy, w, h, label, color='yellow', size=12):
        f, st = C[color]
        self.poly([(cx, cy - h / 2), (cx + w / 2, cy), (cx, cy + h / 2), (cx - w / 2, cy)], f, st)
        L = str(label).split('\n')
        lh = size * 1.25
        top = cy - len(L) * lh / 2
        for i, l in enumerate(L):
            self.text(cx, top + i * lh + lh / 2 + size * 0.35, l, size=size, weight='600')
        return (cx - w / 2, cy - h / 2, w, h)

    def num(self, x, y, n, color='blue', r=9.5):
        self.circle(x, y, r, C[color][1])
        self.text(x, y + 4, n, size=11, weight='700', fill='#ffffff')

    # ---- arrows -----------------------------------------------------
    def head(self, x, y, ang, color, size=8.5):
        hw = size * 0.48
        bx, by = x - size * math.cos(ang), y - size * math.sin(ang)
        px, py = -math.sin(ang) * hw, math.cos(ang) * hw
        self.poly([(x, y), (bx + px, by + py), (bx - px, by - py)], color, color, sw=1)

    def arrow(self, x1, y1, x2, y2, label=None, color=INK2, dash=False, both=False, lw=1.6, t=0.5,
              dx=0, dy=-6, lsize=11.5, anchor='middle', lfill=INK2, lweight='400', head=True, mono=False):
        ang = math.atan2(y2 - y1, x2 - x1)
        k = 6
        sx, sy, ex, ey = x1, y1, x2, y2
        if head:
            ex, ey = x2 - k * math.cos(ang), y2 - k * math.sin(ang)
        if both:
            sx, sy = x1 + k * math.cos(ang), y1 + k * math.sin(ang)
        self.line(sx, sy, ex, ey, color=color, lw=lw, dash=dash)
        if head:
            self.head(x2, y2, ang, color)
        if both:
            self.head(x1, y1, ang + math.pi, color)
        if label:
            self.text(x1 + (x2 - x1) * t + dx, y1 + (y2 - y1) * t + dy, label, size=lsize,
                      anchor=anchor, fill=lfill, weight=lweight, mono=mono)

    def path(self, pts, color=INK2, dash=False, lw=1.6, head=True):
        pts = [tuple(p) for p in pts]
        (x1, y1), (x2, y2) = pts[-2], pts[-1]
        ang = math.atan2(y2 - y1, x2 - x1)
        end = (x2 - 6 * math.cos(ang), y2 - 6 * math.sin(ang)) if head else (x2, y2)
        self.polyline(pts[:-1] + [end], color, lw=lw, dash=dash)
        if head:
            self.head(x2, y2, ang, color)

    @staticmethod
    def _edge(rect, tx, ty):
        x, y, w, h = rect
        cx, cy = x + w / 2, y + h / 2
        dx, dy = tx - cx, ty - cy
        if dx == 0 and dy == 0:
            return cx, cy
        sc = min((w / 2) / abs(dx) if dx else 1e9, (h / 2) / abs(dy) if dy else 1e9)
        return cx + dx * sc, cy + dy * sc

    def link(self, a, b, **kw):
        """Arrow from the edge of rect a to the edge of rect b (centre to centre)."""
        acx, acy = a[0] + a[2] / 2, a[1] + a[3] / 2
        bcx, bcy = b[0] + b[2] / 2, b[1] + b[3] / 2
        x1, y1 = self._edge(a, bcx, bcy)
        x2, y2 = self._edge(b, acx, acy)
        self.arrow(x1, y1, x2, y2, **kw)

    # ---- sequence diagrams -----------------------------------------
    def seq(self, lanes, top=62, bottom=300, hw=150, hh=34):
        """lanes: list of (x, label, colour)."""
        self._lx = [l[0] for l in lanes]
        for x, label, color in lanes:
            self.line(x, top + hh, x, bottom, color=LIFE, lw=1.2, dash=True)
            self.box(x - hw / 2, top, hw, hh, label, color)

    def msg(self, a, b, y, label, n=None, ncolor='blue', dash=False, color=INK2, lsize=11.5, mono=False):
        x1, x2 = self._lx[a], self._lx[b]
        self.arrow(x1, y, x2, y, dash=dash, color=color)
        mid = (x1 + x2) / 2
        wd = tw(label, lsize, False, mono)
        off = 11 if n else 0
        self.rect(mid - wd / 2 - 4 - off, y - 21, wd + 8 + 2 * off, 17, SURF)
        if n:
            self.num(mid - wd / 2 - 3, y - 12, n, ncolor, r=8.5)
        self.text(mid + off, y - 8, label, size=lsize, mono=mono, fill=INK)

    # ---- output -----------------------------------------------------
    def save(self):
        svg = ('<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d" '
               'role="img" aria-label="%s">\n'
               '<rect x="0.5" y="0.5" width="%d" height="%d" rx="12" fill="%s" stroke="%s"/>\n%s\n</svg>\n'
               % (self.w, self.h, self.w, self.h, esc(self.title), self.w - 1, self.h - 1, SURF, EDGE,
                  '\n'.join(self.e)))
        with open(os.path.join(OUT, self.name + '.svg'), 'w', encoding='utf-8', newline='\n') as f:
            f.write(svg)
        ALL.append((self.name, self.w, self.h, self.warn))
        TITLES[self.name] = self.title
