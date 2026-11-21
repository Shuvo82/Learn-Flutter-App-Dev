# -*- coding: utf-8 -*-
"""Diagrams for Part A: A1 Flutter/Dart/native, A2 UI-UX, A3 offline storage and sync."""
from lib import D, C, INK, INK2, MUTED, SURF, EDGE, GRID, tw


# ------------------------------------------------------------------ A1
def a1_app_approaches():
    d = D('ch01-app-approaches', 298, 'Three ways to build a mobile app',
          'What sits between your code and the screen')
    cols = [
        ('Native', 'Kotlin / Swift code', 'Platform UI widgets', 'green',
         'best performance\ntwo codebases, two teams'),
        ('Cross-platform (Flutter)', 'Dart code, one codebase', 'Flutter engine draws\nevery pixel itself', 'blue',
         'near-native speed\none codebase, one team'),
        ('Hybrid (WebView)', 'HTML / CSS / JavaScript', 'WebView: a browser\ninside the app', 'orange',
         'lowest performance\ncheapest to build'),
    ]
    for i, (t, code, ui, col, note) in enumerate(cols):
        x = 30 + i * 240
        d.text(x + 110, 84, t, size=13.5, weight='700')
        d.box(x, 96, 220, 38, code, 'white', weight='400')
        d.arrow(x + 110, 134, x + 110, 150)
        d.box(x, 150, 220, 52, ui, col)
        d.arrow(x + 110, 202, x + 110, 218)
        d.box(x, 218, 220, 30, 'Android / iOS', 'grey', weight='400')
        d.text(x + 110, 268, note, size=11.5, fill=INK2)
    d.save()


def a1_flutter_architecture():
    d = D('ch01-flutter-architecture', 330, "Flutter's three layers")
    x, w = 200, 420
    d.box(x, 58, w, 62, 'Framework (Dart)', 'blue', sub='widgets · rendering · animation · gestures', size=13.5)
    d.box(x, 132, w, 62, 'Engine (C++)', 'violet', sub='Impeller / Skia graphics · Dart runtime · text layout', size=13.5)
    d.box(x, 206, w, 62, 'Embedder (one per platform)', 'green', sub='Android (Kotlin/Java) · iOS (Swift/Obj-C)', size=13.5)
    d.box(x, 280, w, 32, 'Operating system and device', 'grey', weight='400')
    for y, t in [(93, 'You write code here'), (167, 'Draws the pixels'), (241, 'Talks to the OS')]:
        d.text(170, y, t, anchor='end', size=12, fill=INK2)
        d.arrow(176, y - 4, 196, y - 4, lw=1.3)
    d.save()


def a1_event_loop():
    d = D('ch01-event-loop', 424, 'Dart runs one thing at a time: the event loop')
    d.box(30, 62, 190, 64, 'Synchronous code', 'blue', sub='runs first, to the end')
    d.box(285, 62, 190, 64, 'Microtask queue', 'yellow', sub='scheduleMicrotask, .then()')
    d.box(540, 62, 190, 64, 'Event queue', 'green', sub='I/O, timers, taps, Future()')
    d.num(30, 62, '1', 'blue')
    d.num(285, 62, '2', 'yellow')
    d.num(540, 62, '3', 'green')
    d.arrow(220, 94, 285, 94, 'then')
    d.arrow(475, 94, 540, 94, 'if empty')
    d.path([(635, 126), (635, 150), (380, 150), (380, 126)])
    d.text(507, 166, 'after every event, empty the microtasks again', size=11.5, fill=INK2)
    d.rect(30, 186, 700, 62, '#f1f0ec', EDGE, rx=8, sw=1)
    d.text(380, 210, "print('1');  Future(() => print('2'));  scheduleMicrotask(() => print('3'));  print('4');",
           size=11.5, mono=True)
    d.text(380, 234, 'Output:  1  4  3  2      (sync code, then the microtask, then the event)', size=12, weight='600')

    d.text(24, 284, 'Isolates: separate workers, each with its own memory', size=14, anchor='start', weight='700')
    d.box(60, 300, 240, 72, 'Main isolate', 'blue', sub='UI + event loop\nown memory')
    d.box(460, 300, 240, 72, 'Worker isolate', 'violet', sub='heavy work: parse JSON, images\nown memory')
    d.arrow(300, 322, 460, 322, 'message (SendPort)')
    d.arrow(460, 350, 300, 350, 'result', dy=15)
    d.text(380, 400, 'Nothing is shared, so there are no locks and no race conditions.', size=12, fill=INK2)
    d.save()


def a1_three_trees():
    d = D('ch01-three-trees', 322, 'The three trees behind every Flutter screen')
    cols = [
        (30, 'Widget tree', 'blue', ['Padding', 'Row', 'Text'], 'configuration\nimmutable, cheap\nrebuilt often'),
        (285, 'Element tree', 'yellow', ['Element', 'Element', 'Element'], 'the live instance, holds State\n= BuildContext\nlong-lived'),
        (540, 'RenderObject tree', 'green', ['RenderPadding', 'RenderFlex', 'RenderParagraph'], 'layout and paint\nexpensive\nlong-lived, reused'),
    ]
    for x, title, col, nodes, cap in cols:
        d.text(x + 95, 76, title, size=13.5, weight='700')
        for i, n in enumerate(nodes):
            y = 90 + i * 56
            d.box(x, y, 190, 36, n, col, mono=True, size=12)
            if i < 2:
                d.arrow(x + 95, y + 36, x + 95, y + 56)
        d.text(x + 95, 262, cap, size=11.5, fill=INK2)
    for i in range(3):
        y = 108 + i * 56
        d.arrow(220, y, 285, y, 'creates' if i == 0 else None, dash=True)
        d.arrow(475, y, 540, y, 'owns' if i == 0 else None, dash=True)
    d.save()


def a1_state_lifecycle():
    d = D('ch01-state-lifecycle', 224, 'State lifecycle of a StatefulWidget')
    items = [('createState', 104, 'green'), ('initState', 90, 'green'), ('didChangeDependencies', 176, 'blue'),
             ('build', 64, 'blue'), ('deactivate', 96, 'red'), ('dispose', 80, 'red')]
    gap = (712 - sum(w for _, w, _ in items)) / 5.0
    x = 24
    pos = {}
    for name, w, col in items:
        d.box(x, 116, w, 38, name, col, mono=True, size=12)
        pos[name] = (x, w)
        x += w + gap
    names = [n for n, _, _ in items]
    for a, b in zip(names, names[1:]):
        d.arrow(pos[a][0] + pos[a][1], 135, pos[b][0], 135)
    bx = pos['build'][0] + pos['build'][1] / 2
    d.box(bx - 118, 58, 104, 30, 'setState()', 'white', mono=True, size=12)
    d.box(bx + 2, 58, 136, 30, 'didUpdateWidget()', 'white', mono=True, size=12)
    d.arrow(bx - 62, 88, bx - 10, 116)
    d.arrow(bx + 60, 88, bx + 10, 116)
    d.text(bx + 148, 78, 'rebuild', size=11.5, anchor='start', fill=INK2)
    ix = pos['initState'][0] + pos['initState'][1] / 2
    dx = pos['dispose'][0] + pos['dispose'][1] / 2
    d.text(ix, 176, 'once: create\ncontrollers, listeners', size=11.5, fill=INK2)
    d.text(bx, 176, 'many times:\nkeep it fast', size=11.5, fill=INK2)
    d.text(dx - 6, 176, 'once: cancel,\nclose, dispose', size=11.5, fill=INK2)
    d.save()


def a1_platform_channel():
    d = D('ch01-platform-channel', 296, 'Platform channel: how Flutter calls native code')
    d.box(40, 62, 250, 78, 'Dart (Flutter)', 'blue', sub="MethodChannel('fieldapp/device')", submono=True, size=13.5)
    d.box(470, 62, 250, 78, 'Native (Kotlin / Swift)', 'green', sub='MethodCallHandler', submono=True, size=13.5)
    d.arrow(290, 86, 470, 86, "invokeMethod('getBatteryLevel')", lsize=11)
    d.arrow(470, 116, 290, 116, 'result.success(value) / error', dy=15, lsize=11)
    d.pill(380, 160, 'same channel name on both sides · always asynchronous', 'yellow')
    chips = [('MethodChannel', 'one call, one reply'), ('EventChannel', 'a stream, native to Dart'),
             ('BasicMessageChannel', 'free-form messages, both ways')]
    for i, (a, b) in enumerate(chips):
        d.box(30 + i * 240, 212, 220, 58, a, 'white', sub=b, mono=True, size=12)
    d.save()


def a1_activity_lifecycle():
    d = D('ch01-activity-lifecycle', 434, 'Android Activity lifecycle')
    rows = [('onCreate', 64, 'created: build the UI, initialise'),
            ('onStart', 114, 'becoming visible'),
            ('onResume', 164, 'in front, takes input: start camera, sensors'),
            (None, 216, None),
            ('onPause', 280, 'losing focus: pause camera, save small data'),
            ('onStop', 330, 'not visible: release heavy resources'),
            ('onDestroy', 380, 'final clean-up (finish, or rotation)')]
    prev = None
    for name, y, note in rows:
        if name is None:
            d.box(300, y, 160, 42, 'Activity running', 'green')
            bottom = y + 42
        else:
            col = 'blue' if y < 216 else 'orange'
            d.box(300, y, 160, 34, name, col, mono=True, size=12.5)
            d.text(476, y + 21, note, size=11.5, anchor='start', fill=INK2)
            bottom = y + 34
        if prev is not None:
            d.arrow(380, prev, 380, y)
        prev = bottom
    # onPause -> onResume
    d.path([(300, 297), (262, 297), (262, 181), (300, 181)])
    d.text(254, 236, 'back to\nthe front', size=11, anchor='end', fill=INK2)
    # onStop -> onRestart -> onStart
    d.box(58, 220, 120, 34, 'onRestart', 'blue', mono=True, size=12.5)
    d.path([(300, 347), (118, 347), (118, 254)])
    d.path([(118, 220), (118, 131), (300, 131)])
    d.text(206, 364, 'user returns to the app', size=11, fill=INK2)
    d.save()


# ------------------------------------------------------------------ A2
def _screen(d, x, y, w, h, style, alt=False):
    """A tiny phone screen. style: 'wire' or 'color'."""
    d.rect(x, y, w, h, '#ffffff', '#55544f', rx=14, sw=2)
    ix, iw = x + 12, w - 24
    if style == 'wire':
        d.rect(ix, y + 18, iw, 18, '#e4e2dc')
        d.rect(ix, y + 46, iw, 62, 'none', '#9a9892', sw=1.2)
        d.line(ix, y + 46, ix + iw, y + 108, '#9a9892', 1.2)
        d.line(ix + iw, y + 46, ix, y + 108, '#9a9892', 1.2)
        d.rect(ix, y + 120, iw * 0.8, 7, '#d6d4cd', rx=3)
        d.rect(ix, y + 134, iw * 0.6, 7, '#d6d4cd', rx=3)
        d.rect(ix, y + h - 46, iw, 26, 'none', '#9a9892', rx=6, sw=1.2)
    else:
        d.rect(ix, y + 18, iw, 18, C['blue'][1], rx=3)
        if alt:
            d.circle(x + w / 2, y + 86, 22, C['green'][0], C['green'][1], sw=2)
            d.polyline([(x + w / 2 - 10, y + 86), (x + w / 2 - 3, y + 93), (x + w / 2 + 11, y + 79)], C['green'][1], lw=3)
            d.text(x + w / 2, y + 130, 'Saved', size=12, weight='600')
        else:
            d.rect(ix, y + 46, iw, 62, '#cfe3fa', rx=4)
            d.poly([(ix + 10, y + 100), (ix + iw * 0.4, y + 64), (ix + iw * 0.62, y + 86), (ix + iw * 0.75, y + 74),
                    (ix + iw - 8, y + 100)], '#8fbcf0')
            d.rect(ix, y + 120, iw * 0.8, 7, '#c9c7c0', rx=3)
            d.rect(ix, y + 134, iw * 0.6, 7, '#c9c7c0', rx=3)
            d.rect(ix, y + h - 46, iw, 26, C['green'][1], rx=6)
            d.text(x + w / 2, y + h - 28.5, 'Save', size=11.5, weight='600', fill='#ffffff')


def a2_wireframe_mockup_prototype():
    d = D('ch02-wireframe-mockup-prototype', 344, 'Wireframe, mockup, prototype')
    y, h = 62, 212
    _screen(d, 50, y, 140, h, 'wire')
    _screen(d, 258, y, 140, h, 'color')
    _screen(d, 466, y, 124, h, 'color')
    _screen(d, 626, y, 110, h, 'color', alt=True)
    d.circle(528, y + h - 33, 15, 'none', C['orange'][1], sw=2.5)
    d.arrow(546, y + h - 33, 624, y + 120, color=C['orange'][1], lw=2)
    d.text(612, y + h - 14, 'tap', size=11.5, fill=INK2)
    for cx, a, b in [(120, 'Wireframe', 'what goes where, no colour'), (328, 'Mockup', 'the final look, a static picture'),
                     (600, 'Prototype', 'clickable, shows the flow')]:
        d.text(cx, 300, a, size=13.5, weight='700')
        d.text(cx, 320, b, size=11.5, fill=INK2)
    d.save()


def a2_material_vs_hig():
    d = D('ch02-material-vs-hig', 412, 'Material Design and iOS Human Interface Guidelines')
    y, w, h = 84, 170, 290
    for x, ios in [(150, False), (440, True)]:
        d.text(x + w / 2, 72, 'iOS (HIG, Apple)' if ios else 'Android (Material, Google)', size=13.5, weight='700')
        d.rect(x, y, w, h, '#ffffff', '#55544f', rx=16, sw=2)
        blue = C['blue'][1]
        if ios:
            d.rect(x + 2, y + 20, w - 4, 36, '#f6f5f1')
            d.text(x + 12, y + 43, '‹ Back', size=12, anchor='start', fill=blue)
            d.text(x + w / 2, y + 43, 'Visits', size=13, weight='600')
            d.text(x + w - 16, y + 45, '+', size=19, fill=blue)
        else:
            d.rect(x + 2, y + 20, w - 4, 36, C['blue'][0])
            d.arrow(x + 28, y + 38, x + 12, y + 38, color=INK, lw=1.8)
            d.text(x + 42, y + 43, 'Visits', size=13, anchor='start', weight='600')
        for i in range(4):
            d.rect(x + 12, y + 68 + i * 36, w - 24, 26, '#f1f0ec', rx=6)
            d.rect(x + 20, y + 78 + i * 36, 70 - i * 8, 6, '#c9c7c0', rx=3)
        if not ios:
            d.rect(x + w - 56, y + 198, 42, 42, blue, rx=13)
            d.text(x + w - 35, y + 227, '+', size=24, fill='#ffffff')
        d.rect(x + 2, y + h - 50, w - 4, 36, '#f6f5f1' if ios else '#f1f0ec', rx=0)
        d.line(x + 2, y + h - 50, x + w - 2, y + h - 50, EDGE)
        if ios:
            d.rect(x + w / 2 - 26, y + h - 9, 52, 4, '#55544f', rx=2)
        for i in range(3):
            cx = x + 32 + i * 53
            active = i == 0
            if not ios and active:
                d.rect(cx - 19, y + h - 42, 38, 20, '#cfe3fa', rx=10)
            d.circle(cx, y + h - 32, 6, blue if active else '#a6a49d')
            if ios:
                d.rect(cx - 12, y + h - 21, 24, 3, blue if active else '#c9c7c0', rx=1.5)

    def call(side, ty, text, px, py):
        if side == 'M':
            d.text(424, ty, text, size=11.5, anchor='end', fill=INK2)
            d.line(428, ty - 4, px, py, LEAD, 1)
        elif side == 'L':
            d.text(132, ty, text, size=11.5, anchor='end', fill=INK2)
            d.line(136, ty - 4, px, py, LEAD, 1)
        else:
            d.text(628, ty, text, size=11.5, anchor='start', fill=INK2)
            d.line(624, ty - 4, px, py, LEAD, 1)
        d.circle(px, py, 2.5, LEAD)

    LEAD = '#8a8984'
    call('L', y + 30, 'Title left-aligned', 150 + 60, y + 38)
    call('L', y + 96, 'System back button\nor back gesture', 150 + 18, y + 40)
    call('L', y + 166, 'Touch targets\nat least 48 × 48 dp', 150 + 14, y + 152)
    call('L', y + 224, 'FAB = primary action', 150 + w - 54, y + 220)
    call('L', y + 262, 'Navigation bar', 150 + 6, y + h - 32)
    call('R', y + 30, 'Title centred', 440 + w / 2 + 22, y + 38)
    call('R', y + 62, 'Action in the\nnavigation bar', 440 + w - 10, y + 40)
    call('M', y + 124, 'Swipe from the\nleft edge to\ngo back', 440 + 3, y + 150)
    call('R', y + 196, 'Touch targets\nat least 44 × 44 pt', 440 + w - 14, y + 188)
    call('R', y + 262, 'Tab bar', 440 + w - 6, y + h - 32)
    d.text(150 + w / 2, 396, 'font: Roboto · unit: dp', size=11.5, fill=MUTED)
    d.text(440 + w / 2, 396, 'font: San Francisco · unit: pt', size=11.5, fill=MUTED)
    d.save()


def a2_layout_rule():
    d = D('ch02-layout-rule', 262, 'The Flutter layout rule', 'Constraints go down. Sizes go up. Parent sets position.')
    d.box(50, 78, 190, 46, 'Parent', 'blue', size=13.5)
    d.box(50, 196, 190, 46, 'Child', 'green', size=13.5)
    d.arrow(100, 124, 100, 196, color=C['blue'][1], lw=2)
    d.arrow(190, 196, 190, 124, color=C['green'][1], lw=2)
    d.num(100, 160, '1', 'blue')
    d.num(190, 160, '2', 'green')
    d.num(50, 196, '3', 'violet')
    rows = [(96, '1', 'blue', 'Constraints go down', 'The parent gives min and max width and height: "at most 300 × 200".'),
            (154, '2', 'green', 'Sizes go up', 'The child picks a size inside those limits: "I will be 120 × 40".'),
            (212, '3', 'violet', 'Parent sets position', 'The parent decides where the child sits: "you go at (90, 80)".')]
    for y, n, col, a, b in rows:
        d.num(292, y - 4, n, col)
        d.text(312, y, a, size=13, anchor='start', weight='700')
        d.text(312, y + 19, b, size=11.5, anchor='start', fill=INK2)
    d.save()


def a2_expanded_flexible():
    d = D('ch02-expanded-flexible', 214, 'Expanded and Flexible inside a Row')
    x0, w = 190, 540
    for y, name, hint in [(64, 'Expanded', 'must fill'), (136, 'Flexible', 'may fill')]:
        d.text(24, y + 22, name, size=13.5, anchor='start', weight='700')
        d.text(24, y + 40, hint, size=11.5, anchor='start', fill=INK2)
        d.rect(x0 - 6, y - 6, w + 12, 58, 'none', EDGE, rx=8, sw=1.2, dash=True)
        d.box(x0, y, 90, 46, 'fixed: 90', 'grey', weight='400', size=12)
    d.box(x0 + 94, 64, w - 94, 46, 'Expanded child takes ALL the remaining space', 'blue')
    d.box(x0 + 94, 136, 250, 46, 'Flexible child: only what it needs', 'green')
    d.text(x0 + 94 + 250 + (w - 94 - 250) / 2, 164, 'space left unused', size=11.5, fill=MUTED)
    d.text(x0 + w / 2, 204, 'Both take a flex share. Expanded = FlexFit.tight, Flexible = FlexFit.loose.', size=11.5, fill=INK2)
    d.save()


def a2_breakpoints():
    d = D('ch02-breakpoints', 312, 'Responsive breakpoints: one app, three layouts')
    base = 232
    edge = '#55544f'
    # phone
    d.rect(88, base - 160, 88, 160, '#ffffff', edge, rx=10, sw=2)
    for i in range(5):
        d.rect(96, base - 150 + i * 28, 72, 20, C['blue'][0], rx=4)
    # small tablet
    d.rect(266, base - 140, 180, 140, '#ffffff', edge, rx=10, sw=2)
    for r in range(3):
        for c in range(2):
            d.rect(276 + c * 84, base - 130 + r * 42, 76, 32, C['blue'][0], rx=4)
    # tablet
    d.rect(498, base - 160, 240, 160, '#ffffff', edge, rx=10, sw=2)
    for i in range(5):
        d.rect(506, base - 150 + i * 28, 78, 20, C['blue'][1] if i == 1 else C['blue'][0], rx=4)
    d.line(592, base - 152, 592, base - 8, EDGE)
    d.rect(600, base - 150, 130, 140, C['green'][0], rx=6)
    d.rect(610, base - 138, 80, 8, '#9fd8bf', rx=4)
    d.rect(610, base - 120, 108, 6, '#bfe6d4', rx=3)
    d.rect(610, base - 106, 96, 6, '#bfe6d4', rx=3)
    d.rect(610, base - 92, 104, 6, '#bfe6d4', rx=3)
    for cx, a, b, c in [(132, 'Compact', 'width under 600', 'one column'),
                        (356, 'Medium', 'width 600 to 839', 'two columns'),
                        (618, 'Expanded', 'width 840 and above', 'list + detail side by side')]:
        d.text(cx, 258, a, size=13.5, weight='700')
        d.text(cx, 277, b, size=11.5, fill=INK2)
        d.text(cx, 294, c, size=11.5, fill=INK2)
    d.save()


# ------------------------------------------------------------------ A3
def a3_offline_first():
    d = D('ch03-offline-first', 326, 'Offline-first: the local database is the source of truth')
    d.group(20, 58, 548, 250, 'On the phone: always works')
    d.box(44, 98, 120, 56, 'UI', 'blue', size=13.5)
    d.box(224, 98, 140, 56, 'Repository', 'violet', size=13.5)
    d.box(440, 98, 112, 56, 'Local DB', 'green', sub='SQLite', size=13.5)
    d.box(224, 222, 140, 56, 'Sync engine', 'yellow', size=13.5)
    d.box(616, 222, 124, 56, 'Server', 'orange', sub='REST API', size=13.5)
    d.arrow(164, 114, 224, 114, 'actions')
    d.arrow(224, 140, 164, 140, 'stream', dy=15)
    d.arrow(364, 126, 440, 126, 'read / write', both=True, lsize=11)
    d.arrow(294, 154, 294, 222, 'enqueue', dx=-8, dy=4, anchor='end')
    d.arrow(364, 250, 616, 250, 'push / pull, when online', both=True, dx=36)
    d.path([(340, 222), (340, 190), (496, 190), (496, 154)])
    d.text(420, 184, 'upsert pulled rows', size=11.5, fill=INK2)
    d.text(294, 298, 'The UI reads and writes the local DB only. It never waits for the network.', size=12, weight='600')
    d.save()


def a3_caching_strategies():
    d = D('ch03-caching-strategies', 322, 'Three caching strategies: which source comes first?')
    rows = [
        (66, 'Cache-first', 'rarely changing data:\ndistrict list, templates',
         ('green', 'Read the cache', 'found: show it and stop'), 'only if missing',
         ('orange', 'Network', 'fetch, save, show')),
        (146, 'Network-first', 'data that must be fresh:\napproval status',
         ('orange', 'Try the network', 'success: show and save'), 'only if it fails',
         ('green', 'Cache', 'show the saved copy')),
        (226, 'Stale-while-revalidate', 'most list screens',
         ('green', 'Show the cache at once', 'the user sees data instantly'), 'at the same time',
         ('orange', 'Network in background', 'update the cache, then the UI')),
    ]
    for y, name, use, b1, lab, b2 in rows:
        d.text(24, y + 20, name, size=13.5, anchor='start', weight='700')
        d.text(24, y + 38, use, size=11.5, anchor='start', fill=INK2)
        d.box(210, y, 200, 56, b1[1], b1[0], sub=b1[2])
        d.num(210, y, '1', b1[0])
        d.arrow(410, y + 28, 520, y + 28, lab)
        d.box(520, y, 216, 56, b2[1], b2[0], sub=b2[2])
        d.num(520, y, '2', b2[0])
    d.rect(250, 298, 12, 12, C['green'][0], C['green'][1], rx=3)
    d.text(268, 308, 'local cache', size=11.5, anchor='start', fill=INK2)
    d.rect(370, 298, 12, 12, C['orange'][0], C['orange'][1], rx=3)
    d.text(388, 308, 'network', size=11.5, anchor='start', fill=INK2)
    d.save()


def a3_sync_cycle():
    d = D('ch03-sync-cycle', 470, 'The sync cycle: push first, then pull',
          'Push steps in blue, pull steps in green')
    d.seq([(96, 'UI', 'blue'), (286, 'Local DB + outbox', 'green'), (476, 'Sync engine', 'yellow'),
           (666, 'Server', 'orange')], top=66, bottom=452, hw=156)
    d.msg(0, 1, 134, 'save record + outbox row', n='1', ncolor='grey')
    d.msg(1, 0, 164, 'shown at once as "pending"', n='2', ncolor='grey', dash=True)
    d.line(24, 190, 736, 190, EDGE, 1.2, dash=True)
    d.rect(300, 180, 160, 20, SURF)
    d.pill(380, 179, 'the network comes back', 'grey')
    d.msg(1, 2, 236, 'read outbox, oldest first', n='3', ncolor='blue')
    d.msg(2, 3, 266, 'PUSH + Idempotency-Key', n='4', ncolor='blue')
    d.msg(3, 2, 296, '200 OK (or 409 Conflict)', n='5', ncolor='blue', dash=True)
    d.msg(2, 1, 326, 'mark the row "synced"', n='6', ncolor='blue')
    d.msg(2, 3, 362, 'PULL changes since cursor', n='7', ncolor='green')
    d.msg(3, 2, 392, 'changed rows, in pages', n='8', ncolor='green', dash=True)
    d.msg(2, 1, 422, 'upsert in one transaction', n='9', ncolor='green')
    d.msg(1, 0, 446, 'stream updates the screen', dash=True)
    d.save()


def a3_backoff():
    d = D('ch03-exponential-backoff', 244, 'Exponential backoff: the wait doubles after each failure',
          'Seconds to wait before each retry, plus a small random jitter')
    base, top = 196, 80
    vals = [1, 2, 4, 8, 16]
    sc = (base - top) / 16.0
    col = C['blue'][1]
    d.line(70, base, 690, base, '#b9b7b0', 1)
    for i, v in enumerate(vals):
        cx = 130 + i * 125
        h = v * sc
        r = 4 if h >= 8 else h / 2
        d.raw('<path d="M%.1f %.1f V%.1f Q%.1f %.1f %.1f %.1f H%.1f Q%.1f %.1f %.1f %.1f V%.1f Z" fill="%s"/>'
              % (cx - 12, base, base - h + r, cx - 12, base - h, cx - 12 + r, base - h,
                 cx + 12 - r, cx + 12, base - h, cx + 12, base - h + r, base, col))
        d.text(cx, base - h - 7, '%d s' % v, size=12, weight='600')
        d.text(cx, base + 18, 'Retry %d' % (i + 1), size=11.5, fill=INK2)
    d.text(380, 234, 'A weak network or a busy server is not flooded with requests.', size=11.5, fill=INK2)
    d.save()


def a3_conflict():
    d = D('ch03-sync-conflict', 318, 'How a sync conflict happens',
          'The same record changes in two places between two syncs')
    ys, yp = 112, 226
    d.text(24, ys + 4, 'Server', size=13, anchor='start', weight='700')
    d.text(24, yp - 4, 'Phone', size=13, anchor='start', weight='700')
    d.text(24, yp + 12, '(offline)', size=11.5, anchor='start', fill=INK2)
    d.arrow(120, ys, 734, ys, color='#9a9892')
    d.arrow(120, yp, 734, yp, color='#9a9892')
    d.text(730, ys - 10, 'time', size=11, anchor='end', fill=MUTED)
    # last sync
    d.line(170, ys, 170, yp, LIFE_, 1.2, dash=True)
    d.circle(170, ys, 5, C['green'][1], SURF, sw=2)
    d.circle(170, yp, 5, C['green'][1], SURF, sw=2)
    d.text(178, 172, 'last sync:\nboth have version 3', size=11.5, anchor='start', fill=INK2)
    # office edit
    d.circle(400, ys, 6, C['violet'][1], SURF, sw=2)
    d.text(400, ys - 14, 'office edits the visit: now version 4', size=11.5)
    # officer edit
    d.circle(320, yp, 6, C['blue'][1], SURF, sw=2)
    d.text(320, yp + 22, 'officer edits the same visit\n(still based on version 3)', size=11.5)
    # push and 409
    d.arrow(560, yp, 560, ys + 2, color=C['blue'][1], lw=2)
    d.text(552, 160, 'PUSH: "my copy\nstarted from v3"', size=11.5, anchor='end')
    d.arrow(610, ys, 610, yp - 2, color=C['red'][1], lw=2, dash=True)
    d.text(618, 160, '409 Conflict:\n"server is at v4"', size=11.5, anchor='start')
    d.box(470, 250, 266, 50, 'Apply the conflict rule', 'red', sub='server wins · merge fields · ask the user')
    d.save()


LIFE_ = '#b9b7b0'

ALL_A = [a1_app_approaches, a1_flutter_architecture, a1_event_loop, a1_three_trees, a1_state_lifecycle,
         a1_platform_channel, a1_activity_lifecycle,
         a2_wireframe_mockup_prototype, a2_material_vs_hig, a2_layout_rule, a2_expanded_flexible, a2_breakpoints,
         a3_offline_first, a3_caching_strategies, a3_sync_cycle, a3_backoff, a3_conflict]
