# -*- coding: utf-8 -*-
"""Regenerate every diagram of the book.

    python build.py            write all SVG files into Book/images
    python build.py <dir>      also write preview sheets (HTML) into <dir> for a visual check
"""
import importlib
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lib  # noqa: E402

PARTS = ['part_a', 'part_b', 'part_c', 'part_d', 'part_f', 'part_n']


def main():
    for p in PARTS:
        try:
            mod = importlib.import_module(p)
        except ModuleNotFoundError:
            continue
        for fn in getattr(mod, 'ALL_' + p[-1].upper()):
            fn()
    bad = 0
    for name, w, h, warns in lib.ALL:
        for wn in warns:
            bad += 1
            print('%s: %s' % (name, wn.encode('ascii', 'replace').decode()))
    print('%d diagrams written to %s (%d warnings)' % (len(lib.ALL), lib.OUT, bad))

    if len(sys.argv) > 1:
        out = sys.argv[1]
        os.makedirs(out, exist_ok=True)
        per = 6
        items = lib.ALL
        for n in range(0, len(items), per):
            chunk = items[n:n + per]
            rows = ''.join('<figure><img src="file:///%s/%s.svg"><figcaption>%s</figcaption></figure>'
                           % (lib.OUT.replace('\\', '/'), name, name) for name, w, h, _ in chunk)
            page = ('<!doctype html><meta charset="utf-8"><style>body{margin:16px;background:#1e1e1e;'
                    'display:grid;grid-template-columns:760px 760px;gap:14px;align-items:start}'
                    'figure{margin:0}figcaption{color:#aaa;font:12px sans-serif;margin-top:2px}'
                    'img{display:block}</style>' + rows)
            with open(os.path.join(out, 'sheet-%02d.html' % (n // per + 1)), 'w', encoding='utf-8') as f:
                f.write(page)
            hs = [h for _, _, h, _ in chunk]
            tall = sum(max(hs[i:i + 2]) + 34 for i in range(0, len(hs), 2)) + 32
            print('sheet-%02d %d' % (n // per + 1, tall))


if __name__ == '__main__':
    main()
