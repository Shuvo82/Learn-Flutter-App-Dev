# -*- coding: utf-8 -*-
"""Diagrams for chapter F (Probability)."""
from lib import D, C, INK, INK2, MUTED, SURF, EDGE, tw


def f_scale():
    d = D('ch13-probability-scale', 330, 'The probability scale: every probability is between 0 and 1')
    x0, x1, y = 90, 670, 120

    def X(p):
        return x0 + (x1 - x0) * p
    d.rect(x0, y - 7, x1 - x0, 14, C['blue'][0], C['blue'][1], rx=7, sw=1.2)
    marks = [(0, '0', 'Impossible', 'a 7 on one die', 0),
             (1 / 6.0, '1/6 ≈ 0.17', 'Unlikely', 'a 6 on one die', 1),
             (0.5, '1/2 = 0.5', 'Even chance', 'heads on a coin', 0),
             (1, '1', 'Certain', 'a number from 1 to 6', 0)]
    for p, val, word, ex, row in marks:
        x = X(p)
        d.circle(x, y, 7, C['blue'][1])
        d.text(x, y - 18, val, size=12.5, weight='700')
        ty = y + 38 + row * 52
        if row:
            d.line(x, y + 9, x, ty - 14, '#b9b7b0', 1, dash=True)
        d.text(x, ty, word, size=12.5, weight='700')
        d.text(x, ty + 16, ex, size=11.5, fill=INK2)
    f, st = C['green']
    d.rect(20, 264, 720, 50, f, st, rx=8, sw=1.4)
    d.text(380, 285, 'P(event) = favourable outcomes ÷ all equally likely outcomes',
           size=13, weight='700')
    d.text(380, 304, 'P(not A) = 1 − P(A)  ·  the probabilities of all the outcomes add up to 1',
           size=12, fill=INK2)
    d.save()


def f_two_dice():
    d = D('ch13-two-dice', 400, 'Two dice: 6 × 6 = 36 equally likely outcomes',
          'Each cell shows the sum. The green cells are the 6 ways to get 7.')
    x0, y0, cw, ch = 150, 112, 52, 40
    d.text(x0 + 3 * cw, 84, 'Die 2', size=12.5, weight='700', fill=INK2)
    d.text(84, y0 + 3 * ch + 4, 'Die 1', size=12.5, weight='700', fill=INK2)
    for j in range(6):
        d.text(x0 + j * cw + cw / 2, y0 - 8, str(j + 1), size=12.5, weight='700')
    for i in range(6):
        d.text(x0 - 14, y0 + i * ch + ch / 2 + 4, str(i + 1), size=12.5, weight='700')
        for j in range(6):
            s = i + j + 2
            if s == 7:
                f, st = C['green']
            else:
                f, st = '#ffffff', EDGE
            d.rect(x0 + j * cw, y0 + i * ch, cw, ch, f, st, sw=1)
            d.text(x0 + j * cw + cw / 2, y0 + i * ch + ch / 2 + 4.5, str(s), size=13,
                   weight='700' if s == 7 else '400', fill=INK if s == 7 else INK2)
    rows = [('All outcomes', '6 × 6 = 36'),
            ('Sum = 7', '6 ways → 6/36 = 1/6'),
            ('A double (1,1) … (6,6)', '6 ways → 1/6'),
            ('Sum = 12', 'only (6,6) → 1/36'),
            ('Sum ≥ 10', '6 ways → 1/6'),
            ('Sum = 2 or 12', '2 ways → 2/36 = 1/18')]
    for k, (a, b) in enumerate(rows):
        y = 124 + k * 40
        d.text(498, y, a, size=12.5, weight='700', anchor='start')
        d.text(498, y + 17, b, size=12, anchor='start', fill=INK2)
    d.save()


def f_deck():
    d = D('ch13-card-deck', 330, 'A deck of 52 cards: 4 suits × 13 cards')
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    suits = [('♠ Spades', INK), ('♣ Clubs', INK), ('♥ Hearts', '#c62828'), ('♦ Diamonds', '#c62828')]
    x0, y0, w, h, gap = 150, 66, 40, 42, 4
    for i, (name, col) in enumerate(suits):
        y = y0 + i * (h + 8)
        d.text(24, y + h / 2 + 5, name, size=13, weight='700', anchor='start', fill=col)
        for j, r in enumerate(ranks):
            face = r in ('J', 'Q', 'K')
            f, st = (C['yellow'][0], C['yellow'][1]) if face else ('#ffffff', '#b3b1aa')
            d.rect(x0 + j * (w + gap), y, w, h, f, st, rx=5, sw=1.1)
            d.text(x0 + j * (w + gap) + w / 2, y + h / 2 + 5, r, size=13, weight='700', fill=col)
    d.text(24, 286, '26 red (♥ ♦) · 26 black (♠ ♣) · 12 face cards (J, Q, K: yellow) · 4 aces · 4 kings',
           size=12.5, anchor='start', weight='600')
    d.text(24, 308, 'P(king) = 4/52 = 1/13  ·  P(heart) = 13/52 = 1/4  ·  P(face card) = 12/52 = 3/13',
           size=12.5, anchor='start', fill=INK2)
    d.save()


def f_venn():
    d = D('ch13-or-rule', 336, 'The OR rule: add, then subtract the overlap')

    def circ(cx, cy, r, color):
        f, st = C[color]
        d.raw('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s" fill-opacity="0.75" stroke="%s" stroke-width="1.6"/>'
              % (cx, cy, r, f, st))
    d.text(205, 70, 'Can happen together: subtract the overlap', size=13, weight='700')
    circ(160, 184, 78, 'red')
    circ(250, 184, 78, 'blue')
    d.text(120, 98, 'Red cards (26)', size=12, weight='700', fill=C['red'][1])
    d.text(292, 98, 'Kings (4)', size=12, weight='700', fill=C['blue'][1])
    d.text(128, 189, '24', size=15, weight='700')
    d.text(205, 182, '2', size=15, weight='700')
    d.text(205, 198, 'red kings', size=10.5, fill=INK2)
    d.text(285, 189, '2', size=15, weight='700')
    d.text(205, 290, 'P(A or B) = P(A) + P(B) − P(A and B)', size=12.5, weight='700')
    d.text(205, 310, 'P(red or king) = 26/52 + 4/52 − 2/52 = 28/52 = 7/13', size=12, fill=INK2)

    d.line(400, 60, 400, 316, EDGE, 1.2, dash=True)
    d.text(580, 70, 'Mutually exclusive: just add', size=13, weight='700')
    circ(510, 184, 62, 'yellow')
    circ(650, 184, 62, 'green')
    d.text(510, 180, 'Kings', size=12.5, weight='700')
    d.text(510, 198, '4', size=15, weight='700')
    d.text(650, 180, 'Queens', size=12.5, weight='700')
    d.text(650, 198, '4', size=15, weight='700')
    d.text(580, 268, 'no card is both', size=11.5, fill=INK2, italic=True)
    d.text(580, 290, 'P(A or B) = P(A) + P(B)', size=12.5, weight='700')
    d.text(580, 310, 'P(king or queen) = 4/52 + 4/52 = 8/52 = 2/13', size=12, fill=INK2)
    d.save()


def f_tree():
    d = D('ch13-tree-diagram', 392, 'A tree diagram: two balls drawn without replacement',
          'The bag has 3 red and 2 blue balls. The first ball is not put back.')
    d.box(24, 196, 92, 44, 'Bag', 'grey', sub='3 R + 2 B', size=12.5, subsize=11)

    def node(x, y, t):
        col = 'red' if t == 'R' else 'blue'
        d.circle(x, y, 17, C[col][0], C[col][1], sw=1.6)
        d.text(x, y + 5, t, size=13, weight='700', fill=C[col][1])
    L1 = [(290, 136, 'R', '3/5'), (290, 300, 'B', '2/5')]
    L2 = {'R': [(500, 96, 'R', '2/4', 'left: 2 R + 2 B'), (500, 176, 'B', '2/4', None)],
          'B': [(500, 260, 'R', '3/4', 'left: 3 R + 1 B'), (500, 340, 'B', '1/4', None)]}
    res = {('R', 'R'): ('3/5 × 2/4 = 6/20', 'both red'), ('R', 'B'): ('3/5 × 2/4 = 6/20', 'red, then blue'),
           ('B', 'R'): ('2/5 × 3/4 = 6/20', 'blue, then red'), ('B', 'B'): ('2/5 × 1/4 = 2/20', 'both blue')}
    for x, y, t, p in L1:
        d.line(116, 218, x - 17, y, '#9a9892', 1.6)
        d.text((116 + x) / 2 - 6, (218 + y) / 2 - 6 if y < 218 else (218 + y) / 2 + 18, p,
               size=13, weight='700', fill=C['red' if t == 'R' else 'blue'][1])
        node(x, y, t)
        for x2, y2, t2, p2, note in L2[t]:
            d.line(x + 17, y, x2 - 17, y2, '#9a9892', 1.6)
            d.text((x + x2) / 2, (y + y2) / 2 - 8 if y2 < y else (y + y2) / 2 + 18, p2,
                   size=13, weight='700', fill=C['red' if t2 == 'R' else 'blue'][1])
            node(x2, y2, t2)
            a, b = res[(t, t2)]
            d.text(530, y2 - 2, a, size=12.5, weight='700', anchor='start')
            d.text(530, y2 + 14, b, size=11, anchor='start', fill=INK2)
        d.text(x, y + 34, 'then ' + ('2 R + 2 B' if t == 'R' else '3 R + 1 B') + ' left', size=10.5, fill=MUTED)
    d.text(380, 380, 'Multiply ALONG a branch (AND). Add the ends you want (OR). All ends add up to 20/20 = 1.',
           size=12, weight='600')
    d.save()


def f_perm_comb():
    d = D('ch13-perm-vs-comb', 318, 'Permutation or combination? Choose 2 letters from A, B, C')
    d.group(20, 60, 360, 186, 'Permutation: ORDER MATTERS')
    d.group(400, 60, 340, 186, 'Combination: order does NOT matter')
    pairs = [('AB', 'BA'), ('AC', 'CA'), ('BC', 'CB')]
    for i, (a, b) in enumerate(pairs):
        y = 88 + i * 44
        d.box(60, y, 70, 34, a, 'blue', size=14)
        d.box(150, y, 70, 34, b, 'blue', size=14)
        d.box(450, y, 70, 34, a, 'green', size=14)
        d.text(536, y + 22, '(' + b + ' is the same)', size=11.5, anchor='start', fill=MUTED)
    d.text(300, 160, '6', size=30, weight='700', fill=C['blue'][1])
    d.text(300, 182, 'ways', size=12, fill=INK2)
    d.text(690, 160, '3', size=30, weight='700', fill=C['green'][1])
    d.text(690, 182, 'ways', size=12, fill=INK2)
    d.text(200, 236, 'AB ≠ BA (e.g. president + secretary)', size=11.5, fill=INK2)
    d.text(570, 236, 'AB = BA (e.g. a team of two)', size=11.5, fill=INK2)
    d.text(200, 274, 'nPr = n! ÷ (n − r)!', size=13.5, weight='700', mono=True)
    d.text(200, 296, '3P2 = 3! ÷ 1! = 6', size=12.5, mono=True, fill=INK2)
    d.text(570, 274, 'nCr = n! ÷ (r! × (n − r)!)', size=13.5, weight='700', mono=True)
    d.text(570, 296, '3C2 = 3! ÷ (2! × 1!) = 3', size=12.5, mono=True, fill=INK2)
    d.save()


def f_bayes():
    d = D('ch13-bayes-frequency', 384, 'Conditional probability with counts: is a flagged build really bad?',
          '2% of builds have a bug. The test catches 95% of bad builds, but also flags 10% of good ones.')
    root = d.box(24, 172, 120, 52, '1,000 builds', 'grey', size=13)
    bad = d.box(210, 96, 170, 50, '20 have a bug', 'red', sub='2% of 1,000')
    good = d.box(210, 252, 170, 50, '980 are fine', 'green', sub='98% of 1,000')
    d.link(root, bad)
    d.link(root, good)
    c = [d.box(470, 66, 200, 44, '19 flagged', 'red', sub='95% of 20: true alarm', fill=C['red'][0]),
         d.box(470, 122, 200, 40, '1 missed', 'white', sub=None),
         d.box(470, 222, 200, 44, '98 flagged', 'orange', sub='10% of 980: false alarm'),
         d.box(470, 278, 200, 40, '882 not flagged', 'white')]
    d.link(bad, c[0])
    d.link(bad, c[1])
    d.link(good, c[2])
    d.link(good, c[3])
    f, st = C['yellow']
    d.rect(20, 330, 720, 44, f, st, rx=8, sw=1.4)
    d.text(380, 349, 'Flagged = 19 + 98 = 117.  Really bad among them = 19.', size=12.5, weight='700')
    d.text(380, 366, 'P(bug | flagged) = 19 ÷ 117 ≈ 0.16 = 16%, not 95%!', size=12.5, weight='700',
           fill=C['red'][1])
    d.save()


ALL_F = [f_scale, f_two_dice, f_deck, f_venn, f_tree, f_perm_comb, f_bayes]
