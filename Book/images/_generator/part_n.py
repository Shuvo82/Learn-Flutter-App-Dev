# -*- coding: utf-8 -*-
"""Diagrams for the Foundations notes (Notes/Foundations 1 and 2)."""
import math

from lib import D, C, INK, INK2, MUTED, EDGE, tw


def n_growth():
    d = D('fd1-big-o-growth', 400, 'How the work grows: n = 1,000 items, one step = 1 microsecond',
          'The bar length is drawn on a log scale; each grid line is 10 times more work.')
    rows = [('O(1)', 'go straight to the seat number', 1, '1 step', '1 µs', 'green'),
            ('O(log n)', 'phone book: halve, halve, halve', 10, '10 steps', '10 µs', 'green'),
            ('O(n)', 'read the register from the top', 1e3, '1,000 steps', '1 ms', 'blue'),
            ('O(n log n)', 'a good sort (merge sort)', 1e4, '10,000 steps', '10 ms', 'yellow'),
            ('O(n²)', 'everyone shakes hands with everyone', 1e6, '1,000,000 steps', '1 second', 'orange'),
            ('O(2ⁿ)', 'try every on/off mix of n switches', None, '2¹⁰⁰⁰ steps', 'never ends', 'red')]
    x0, x1, y0, rh = 270, 590, 76, 44
    for k in range(7):
        x = x0 + (x1 - x0) * k / 6.0
        d.line(x, y0 - 6, x, y0 + rh * len(rows) - 8, '#ecebe6', 1)
    for i, (o, ex, steps, s_txt, t_txt, col) in enumerate(rows):
        y = y0 + i * rh
        d.text(24, y + 15, o, size=14, anchor='start', weight='700', mono=True)
        d.text(24, y + 31, ex, size=11.5, anchor='start', fill=INK2)
        f, st = C[col]
        if steps is None:
            w = x1 - x0 + 30
            d.rect(x0, y + 6, w, 24, f, st, rx=5, sw=1.3, dash=True)
            d.text(x0 + w / 2, y + 22, s_txt + ' · ' + t_txt, size=12, weight='700', fill=st)
        else:
            w = max(10, (x1 - x0) * math.log10(steps) / 6.0)
            d.rect(x0, y + 6, w, 24, f, st, rx=5, sw=1.3)
            d.text(x0 + w + 10, y + 16, s_txt, size=12, anchor='start', weight='700')
            d.text(x0 + w + 10, y + 31, t_txt, size=11.5, anchor='start', fill=INK2)
    f, st = C['yellow']
    d.rect(20, 340, 720, 48, f, st, rx=8, sw=1.4)
    d.text(380, 360, 'Up to O(n log n) stays fast even for big lists.  O(n²) is slow for thousands of items.',
           size=12.5, weight='700')
    d.text(380, 378, 'O(2ⁿ) only works when n is tiny (about 30 or less).', size=12, fill=INK2)
    d.save()


def n_halving():
    d = D('fd1-binary-search-halving', 352, 'Binary search: every step throws away half of what is left',
          'A sorted list of 16 numbers. We look for 47. Blue = still possible, yellow = the middle we check.')
    nums = [3, 7, 9, 12, 15, 18, 21, 25, 30, 34, 40, 42, 47, 51, 58, 63]
    steps = [(0, 15, 7, '25 < 47: drop the left half'),
             (8, 15, 11, '42 < 47: drop the left half'),
             (12, 15, 13, '51 > 47: drop the right half'),
             (12, 12, 12, 'found 47')]
    x0, cw, ch, y0, rh = 104, 28, 30, 78, 48
    for s, (lo, hi, mid, note) in enumerate(steps):
        y = y0 + s * rh
        left = hi - lo + 1
        d.text(24, y + 13, 'Step %d' % (s + 1), size=12.5, anchor='start', weight='700')
        d.text(24, y + 28, '%d left' % left, size=11.5, anchor='start', fill=INK2)
        for i, v in enumerate(nums):
            x = x0 + i * cw
            if i == mid:
                col = 'green' if left == 1 else 'yellow'
            elif lo <= i <= hi:
                col = 'blue'
            else:
                col = 'grey'
            f, st = C[col]
            if col == 'grey':
                d.rect(x, y, cw - 3, ch, '#f4f3ef', '#dedcd5', rx=4, sw=1)
                d.text(x + (cw - 3) / 2, y + 19, v, size=11, fill='#b9b7b0')
            else:
                d.rect(x, y, cw - 3, ch, f, st, rx=4, sw=1.3)
                d.text(x + (cw - 3) / 2, y + 19, v, size=11, weight='700')
        d.text(x0 + 16 * cw + 12, y + 19, note, size=11.5, anchor='start',
               fill=C['green'][1] if left == 1 else INK2, weight='700' if left == 1 else '400')
    f, st = C['green']
    d.rect(20, 278, 720, 64, f, st, rx=8, sw=1.4)
    d.text(380, 300, 'The question behind O(log n): how many times can I halve n until 1 is left?',
           size=12.5, weight='700')
    d.text(380, 318, '16 → 8 → 4 → 2 → 1 is 4 halvings, and 2⁴ = 16, so log₂ 16 = 4.', size=12, fill=INK2)
    d.text(380, 334, '1,000,000 items need only about 20 steps (2²⁰ ≈ 1,000,000). Double the list: just 1 more step.',
           size=12, fill=INK2)
    d.save()


ALL_N = [n_growth, n_halving]
