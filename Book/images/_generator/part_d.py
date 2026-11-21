# -*- coding: utf-8 -*-
"""Diagrams for Part D (architecture, testing, support, Agile) and the revision sheet (E)."""
import math

from lib import D, C, INK, INK2, MUTED, SURF, EDGE, GRID, tw


# ------------------------------------------------------------------ D1
def d1_mvc_mvp_mvvm():
    d = D('ch10-mvc-mvp-mvvm', 330, 'MVC, MVP and MVVM')
    # MVC
    x0 = 24
    d.group(x0, 58, 224, 254)
    d.text(x0 + 112, 82, 'MVC', size=14, weight='700')
    d.box(x0 + 14, 104, 84, 36, 'View', 'blue')
    d.box(x0 + 126, 104, 84, 36, 'Controller', 'yellow')
    d.box(x0 + 70, 206, 84, 36, 'Model', 'green')
    d.arrow(x0 + 98, 122, x0 + 126, 122)
    d.text(x0 + 112, 98, 'input', size=11, fill=INK2)
    d.arrow(x0 + 168, 140, x0 + 132, 206)
    d.text(x0 + 160, 180, 'updates', size=11, anchor='start', fill=INK2)
    d.arrow(x0 + 92, 206, x0 + 56, 140)
    d.text(x0 + 64, 180, 'reads', size=11, anchor='end', fill=INK2)
    d.text(x0 + 112, 276, 'The View may read\nthe Model directly.', size=11.5, fill=INK2)
    # MVP
    x0 = 268
    d.group(x0, 58, 224, 254)
    d.text(x0 + 112, 82, 'MVP', size=14, weight='700')
    d.box(x0 + 62, 96, 100, 34, 'View', 'blue')
    d.box(x0 + 62, 166, 100, 34, 'Presenter', 'yellow')
    d.box(x0 + 62, 236, 100, 34, 'Model', 'green')
    d.arrow(x0 + 92, 130, x0 + 92, 166)
    d.arrow(x0 + 132, 166, x0 + 132, 130)
    d.text(x0 + 84, 152, 'events', size=11, anchor='end', fill=INK2)
    d.text(x0 + 140, 152, 'view.show()', size=10.5, anchor='start', mono=True)
    d.arrow(x0 + 112, 200, x0 + 112, 236, both=True)
    d.text(x0 + 112, 292, '1 Presenter : 1 View, by interface', size=11.5, fill=INK2)
    # MVVM
    x0 = 512
    d.group(x0, 58, 224, 254)
    d.text(x0 + 112, 82, 'MVVM', size=14, weight='700')
    d.box(x0 + 62, 96, 100, 34, 'View', 'blue')
    d.box(x0 + 62, 166, 100, 34, 'ViewModel', 'yellow')
    d.box(x0 + 62, 236, 100, 34, 'Model', 'green')
    d.arrow(x0 + 92, 130, x0 + 92, 166)
    d.arrow(x0 + 132, 166, x0 + 132, 130, dash=True)
    d.text(x0 + 84, 152, 'calls', size=11, anchor='end', fill=INK2)
    d.text(x0 + 140, 152, 'state stream', size=11, anchor='start', fill=INK2)
    d.arrow(x0 + 112, 200, x0 + 112, 236, both=True)
    d.text(x0 + 112, 292, 'ViewModel does not know the View', size=11.5, fill=INK2)
    d.save()


def d1_bloc():
    d = D('ch10-bloc', 232, 'BLoC: events go in, states come out')
    d.box(30, 86, 120, 66, 'UI', 'blue', sub='widgets', size=14)
    d.box(340, 86, 150, 66, 'BLoC / Cubit', 'yellow', sub='business logic', size=14)
    d.box(540, 86, 110, 66, 'Repository', 'violet')
    d.box(680, 86, 56, 66, 'API\nDB', 'grey')
    d.arrow(150, 104, 340, 104, 'Event: LoadVisits, SubmitVisit', color=C['blue'][1], lw=2, lfill=INK)
    d.arrow(340, 134, 150, 134, 'State: Loading, Loaded, Error', color=C['yellow'][1], lw=2, dy=16, lfill=INK)
    d.arrow(490, 119, 540, 119, both=True)
    d.arrow(650, 119, 680, 119, both=True)
    d.text(380, 204, 'One direction only. The UI never changes the state by itself.', size=12, fill=INK2)
    d.save()


def d1_clean_architecture():
    d = D('ch10-clean-architecture', 386, 'Clean Architecture: dependencies point inward, to the domain')
    bands = [(62, 'PRESENTATION', 'blue', ['Pages / Widgets', 'BLoC / Cubit'], None),
             (168, 'DOMAIN', 'yellow', ['Use cases', 'Entities', 'Repository interfaces'],
              'pure Dart: knows nothing about Flutter, Dio or the database'),
             (274, 'DATA', 'green', ['Repository impl', 'Models (DTO)', 'Remote (Dio)', 'Local (Drift)'], None)]
    for y, name, col, chips, note in bands:
        d.rect(40, y, 680, 76, C[col][0], C[col][1], rx=10, sw=2 if name == 'DOMAIN' else 1.5)
        d.text(56, y + 22, name, size=12, anchor='start', weight='700')
        if note:
            d.text(704, y + 22, note, size=11.5, anchor='end', fill=INK2)
        for i, c in enumerate(chips):
            d.box(56 + i * 163, y + 34, 151, 30, c, 'white', size=12, weight='400', r=6)
    d.arrow(380, 138, 380, 168, color=INK, lw=2)
    d.text(392, 157, 'depends on', size=11.5, anchor='start', fill=INK2)
    d.arrow(380, 274, 380, 244, color=INK, lw=2)
    d.text(392, 263, 'depends on (it implements the interfaces)', size=11.5, anchor='start', fill=INK2)
    d.text(380, 370, 'Call flow:  UI → BLoC → Use case → Repository (interface) → RepositoryImpl → Remote / Local',
           size=12, weight='600')
    d.save()


def d1_test_pyramid():
    d = D('ch10-test-pyramid', 284, 'The test pyramid')
    ax, top, base, half = 290, 64, 250, 190

    def hw(y):
        return (y - top) / float(base - top) * half

    bands = [(top, 126, 'orange'), (129, 188, 'blue'), (191, base, 'green')]
    for y1, y2, col in bands:
        d.poly([(ax - hw(y1), y1), (ax + hw(y1), y1), (ax + hw(y2), y2), (ax - hw(y2), y2)], C[col][1])
    d.text(ax, 116, 'E2E', size=11.5, weight='700', fill='#ffffff')
    d.text(ax, 164, 'Widget', size=13, weight='700', fill='#ffffff')
    d.text(ax, 226, 'Unit', size=13, weight='700', fill='#ffffff')
    rows = [(96, 'Integration / E2E tests', 'few · slow · real device or emulator'),
            (158, 'Widget tests', 'some · fast · no device needed'),
            (220, 'Unit tests', 'many · milliseconds · one function or class')]
    for (y, a, b), (y1, y2, col) in zip(rows, bands):
        mid = (y1 + y2) / 2.0
        d.line(ax + hw(mid) + 6, mid, 492, mid, '#9a9892', 1)
        d.text(500, y, a, size=12.5, anchor='start', weight='700')
        d.text(500, y + 17, b, size=11.5, anchor='start', fill=INK2)
    d.arrow(86, 246, 86, 70, color='#9a9892')
    d.text(76, 150, 'slower,\ncostlier,\nmore\nconfidence', size=11.5, anchor='end', fill=INK2)
    d.save()


def d1_tdd():
    d = D('ch10-tdd-cycle', 238, 'TDD: red, green, refactor')
    items = [(190, 'RED', 'red', 'write a failing test'), (380, 'GREEN', 'green', 'minimum code to pass'),
             (570, 'REFACTOR', 'blue', 'clean up, tests still pass')]
    for cx, t, col, cap in items:
        d.text(cx, 72, cap, size=11.5, fill=INK2)
        d.circle(cx, 128, 44, C[col][0], C[col][1], sw=2.5)
        d.text(cx, 133, t, size=13, weight='700')
    d.arrow(234, 128, 336, 128, lw=2)
    d.arrow(424, 128, 526, 128, lw=2)
    d.path([(570, 172), (570, 200), (190, 200), (190, 172)], lw=2)
    d.text(380, 220, 'then the next small behaviour', size=11.5, fill=INK2)
    d.save()


# ------------------------------------------------------------------ D2
def d2_bug_lifecycle():
    d = D('ch11-bug-lifecycle', 282, 'Bug life cycle')
    items = [('New', 60, 'grey'), ('Assigned', 84, 'blue'), ('Open', 64, 'blue'), ('Fixed', 64, 'yellow'),
             ('Retest', 70, 'yellow'), ('Verified', 82, 'green'), ('Closed', 70, 'green')]
    gap = (712 - sum(w for _, w, _ in items)) / 6.0
    x = 24
    P = {}
    for n, w, col in items:
        P[n] = d.box(x, 78, w, 38, n, col)
        x += w + gap
    names = [n for n, _, _ in items]
    for a, b in zip(names, names[1:]):
        d.arrow(P[a][0] + P[a][2], 97, P[b][0], 97)
    ox = P['Open'][0] + P['Open'][2] / 2
    rx = P['Retest'][0] + P['Retest'][2] / 2
    ax = P['Assigned'][0] + P['Assigned'][2] / 2
    d.box(186, 172, 150, 36, 'Rejected / Duplicate', 'grey', weight='400')
    d.box(352, 172, 138, 36, 'Deferred (fix later)', 'grey', weight='400')
    d.box(540, 172, 170, 36, 'Reopened (fix failed)', 'red')
    d.arrow(ox - 8, 116, 262, 172)
    d.arrow(ox + 8, 116, 400, 172)
    d.arrow(rx + 6, 116, 600, 172)
    d.path([(625, 208), (625, 244), (ax, 244), (ax, 116)], color=C['red'][1])
    d.text(390, 262, 'the bug goes back to the developer', size=11.5, fill=INK2)
    d.save()


def d2_severity_priority():
    d = D('ch11-severity-priority', 346, 'Severity and priority are two different things')
    x0, y0, cw, ch = 200, 86, 262, 96
    cells = [(0, 0, 'orange', 'Crash in a report that is\nused once a year'),
             (1, 0, 'red', 'The app crashes on login\nfor everyone'),
             (0, 1, 'grey', 'Slight misalignment on\na settings page'),
             (1, 1, 'yellow', "The app's name misspelled\non the home screen")]
    for cx, cy, col, t in cells:
        d.box(x0 + cx * (cw + 6), y0 + cy * (ch + 6), cw, ch, t, col, weight='400', size=12.5)
    d.text(x0 + cw / 2, 76, 'Low priority: fix later', size=12, weight='700')
    d.text(x0 + cw + 6 + cw / 2, 76, 'High priority: fix now', size=12, weight='700')
    d.text(186, y0 + 44, 'High severity', size=12, anchor='end', weight='700')
    d.text(186, y0 + 61, 'big damage', size=11.5, anchor='end', fill=INK2)
    d.text(186, y0 + ch + 6 + 44, 'Low severity', size=12, anchor='end', weight='700')
    d.text(186, y0 + ch + 6 + 61, 'small damage', size=11.5, anchor='end', fill=INK2)
    d.text(380, 310, 'Severity = how badly the bug damages the system (set by QA).', size=12, fill=INK2)
    d.text(380, 329, 'Priority = how soon it must be fixed (set by the product owner or manager).', size=12, fill=INK2)
    d.save()


def d2_backward_compat():
    d = D('ch11-backward-compatibility', 300, 'Backward compatibility has four sides')
    c = d.box(290, 142, 180, 62, 'New app version', 'blue', sub='must still work with…', size=13.5)
    boxes = [d.box(30, 62, 236, 60, '(a) Older OS and devices', 'orange', sub='minSdk, version checks, fallbacks'),
             d.box(494, 62, 236, 60, '(b) Older app versions', 'violet', sub='keep API /v1 alive, additive changes'),
             d.box(30, 224, 236, 60, '(c) Older local data', 'green', sub='database migrations v1 → v2 → v3'),
             d.box(494, 224, 236, 60, '(d) Newer libraries', 'yellow', sub='small upgrades, pinned versions, tests')]
    d.arrow(300, 142, 266, 116)
    d.arrow(460, 142, 494, 116)
    d.arrow(300, 204, 266, 230)
    d.arrow(460, 204, 494, 230)
    d.save()


# ------------------------------------------------------------------ D3
def d3_sdlc():
    d = D('ch12-sdlc', 338, 'SDLC: the software development life cycle')
    names = ['1. Planning', '2. Requirements', '3. Design', '4. Implementation', '5. Testing', '6. Deployment',
             '7. Maintenance']
    cols = ['grey', 'blue', 'blue', 'violet', 'yellow', 'green', 'green']
    cx, cy, rx, ry, w, h = 380, 192, 262, 106, 150, 40
    B = []
    for i, (n, col) in enumerate(zip(names, cols)):
        a = math.radians(-90 + i * 360.0 / 7)
        x, y = cx + rx * math.cos(a), cy + ry * math.sin(a)
        B.append(d.box(x - w / 2, y - h / 2, w, h, n, col))
    for i in range(7):
        d.link(B[i], B[(i + 1) % 7])
    d.text(cx, cy - 2, 'SDLC', size=18, weight='700')
    d.text(cx, cy + 18, 'maintenance feeds the next plan', size=11.5, fill=INK2)
    d.save()


def d3_waterfall_vs_agile():
    d = D('ch12-waterfall-vs-agile', 330, 'Waterfall and Agile')
    d.text(190, 72, 'Waterfall', size=14, weight='700')
    steps = ['Requirements', 'Design', 'Coding', 'Testing', 'Deployment']
    for i, s in enumerate(steps):
        x, y = 34 + i * 50, 86 + i * 40
        d.box(x, y, 112, 30, s, 'green' if i == 4 else 'blue', size=12)
        if i < 4:
            d.arrow(x + 81, y + 30, x + 81, y + 40)
    d.text(190, 300, 'One delivery at the end. Change is expensive.', size=11.5, fill=INK2)
    d.line(380, 62, 380, 312, EDGE, 1.2)
    d.text(570, 72, 'Agile', size=14, weight='700')
    for i in range(3):
        cx = 460 + i * 110
        d.circle(cx, 138, 42, C['blue'][0], C['blue'][1], sw=2)
        d.text(cx, 134, 'Sprint %d' % (i + 1), size=12.5, weight='700')
        d.text(cx, 151, 'plan · build', size=10.5, fill=INK2)
        d.text(cx, 164, 'test · review', size=10.5, fill=INK2)
        if i < 2:
            d.arrow(cx + 42, 138, cx + 68, 138)
        d.arrow(cx, 180, cx, 206)
        d.box(cx - 46, 206, 92, 22 + i * 14, 'Increment %d' % (i + 1), 'green', size=11.5)
    d.text(570, 282, 'Working software after every sprint.', size=11.5, fill=INK2)
    d.text(570, 300, 'Change is expected.', size=11.5, fill=INK2)
    d.save()


def d3_v_model():
    d = D('ch12-v-model', 314, 'The V-model: every development phase has a matching test phase')
    L = [d.box(30, 66, 176, 40, 'Requirements', 'blue'), d.box(86, 130, 176, 40, 'System design', 'blue'),
         d.box(142, 194, 176, 40, 'Module design', 'blue')]
    code = d.box(292, 258, 176, 40, 'Coding', 'yellow')
    R = [d.box(554, 66, 176, 40, 'Acceptance testing (UAT)', 'green'), d.box(498, 130, 176, 40, 'System testing', 'green'),
         d.box(442, 194, 176, 40, 'Unit testing', 'green')]
    d.arrow(150, 106, 166, 130)
    d.arrow(206, 170, 222, 194)
    d.arrow(262, 234, 320, 258)
    d.arrow(440, 258, 498, 234)
    d.arrow(538, 194, 554, 170)
    d.arrow(594, 130, 610, 106)
    for (l, r) in zip(L, R):
        y = l[1] + 20
        d.arrow(l[0] + l[2], y, r[0], y, dash=True, both=True, color='#9a9892')
    d.text(380, 80, 'tested by', size=11.5, fill=INK2)
    d.save()


def d3_scrum():
    d = D('ch12-scrum', 372, 'Scrum in one picture', 'Events in blue · artifacts in violet · roles at the bottom')
    d.box(24, 104, 120, 72, 'Product\nBacklog', 'violet', sub='ordered wish list')
    d.box(178, 118, 110, 44, 'Sprint\nPlanning', 'blue')
    d.box(322, 104, 120, 72, 'Sprint\nBacklog', 'violet', sub='items for this sprint')
    d.arrow(144, 140, 178, 140)
    d.arrow(288, 140, 322, 140)
    d.circle(540, 140, 60, C['blue'][0], C['blue'][1], sw=2.5)
    d.text(540, 138, 'SPRINT', size=14, weight='700')
    d.text(540, 156, '1 to 4 weeks', size=11.5, fill=INK2)
    d.circle(596, 82, 30, '#ffffff', C['blue'][1], sw=2)
    d.text(596, 80, 'Daily', size=11, weight='700')
    d.text(596, 93, '15 min', size=10.5, fill=INK2)
    d.arrow(442, 140, 480, 140)
    d.box(640, 110, 100, 60, 'Increment', 'violet', sub='working product')
    d.arrow(600, 140, 640, 140)
    d.box(594, 232, 146, 46, 'Sprint Review', 'blue', sub='demo the product')
    d.box(384, 232, 170, 46, 'Sprint Retrospective', 'blue', sub='improve the process')
    d.arrow(690, 170, 690, 232)
    d.arrow(594, 255, 554, 255)
    d.path([(384, 255), (233, 255), (233, 162)])
    d.text(306, 272, 'next sprint', size=11.5, fill=INK2)
    roles = [('Product Owner', 'decides what to build, and the order'), ('Scrum Master', 'guards the process, removes blockers'),
             ('Developers', 'build the increment')]
    for i, (a, b) in enumerate(roles):
        d.box(24 + i * 240, 306, 232, 48, a, 'white', sub=b)
    d.save()


def d3_burndown():
    d = D('ch12-burndown', 296, 'A sprint burndown chart', 'Example sprint: 40 story points, 10 working days')
    x0, x1, base, top = 80, 540, 240, 90
    sy = (base - top) / 40.0
    sx = (x1 - x0) / 10.0
    for v in (0, 10, 20, 30, 40):
        y = base - v * sy
        d.line(x0, y, x1, y, '#b9b7b0' if v == 0 else GRID, 1)
        d.text(x0 - 8, y + 4, str(v), size=11, anchor='end', fill=MUTED)
    for dd in range(0, 11, 2):
        d.text(x0 + dd * sx, base + 17, str(dd), size=11, fill=MUTED)
    d.text(x0, 78, 'story points left', size=11.5, anchor='start', fill=MUTED)
    d.text((x0 + x1) / 2, base + 36, 'day of the sprint', size=11.5, fill=MUTED)
    grey, blue = '#8a8984', C['blue'][1]
    d.line(x0, top, x1, base, grey, 2)
    actual = [40, 38, 36, 36, 30, 27, 22, 18, 12, 6, 0]
    pts = [(x0 + i * sx, base - v * sy) for i, v in enumerate(actual)]
    d.polyline(pts, blue, lw=2)
    d.circle(pts[-1][0], pts[-1][1], 5, blue, SURF, sw=2)
    d.line(566, 100, 590, 100, grey, 2)
    d.text(598, 104, 'ideal burndown', size=11.5, anchor='start', fill=INK2)
    d.line(566, 122, 590, 122, blue, 2)
    d.text(598, 126, 'actual work left', size=11.5, anchor='start', fill=INK2)
    d.text(566, 164, 'Above the ideal line', size=12, anchor='start', weight='600')
    d.text(566, 181, 'the team is behind', size=11.5, anchor='start', fill=INK2)
    d.text(566, 210, 'Flat line (days 2 to 3)', size=12, anchor='start', weight='600')
    d.text(566, 227, 'no progress: a blocker', size=11.5, anchor='start', fill=INK2)
    d.save()


def d3_kanban():
    d = D('ch12-kanban', 290, 'A Kanban board with work-in-progress limits')
    cols = [('To Do', None, ['Bangla labels', 'Photo upload', 'Pagination']),
            ('In Progress', 'max 3', ['Fix sync crash', 'Visit form', 'Push setup']),
            ('Review', 'max 2', ['Login screen']),
            ('Done', None, ['Splash screen', 'Theme'])]
    for i, (name, lim, cards) in enumerate(cols):
        x = 40 + i * 176
        full = lim is not None and len(cards) >= int(lim.split()[-1])
        d.rect(x, 62, 160, 186, '#f6f5f1', C['red'][1] if full else EDGE, rx=10, sw=1.8 if full else 1.2)
        d.text(x + 12, 84, name, size=12.5, anchor='start', weight='700')
        if lim:
            d.text(x + 148, 84, lim, size=11, anchor='end', fill=C['red'][1] if full else INK2, weight='600')
        for j, c in enumerate(cards):
            d.box(x + 10, 98 + j * 44, 140, 36, c, 'white', weight='400', size=12, r=6)
    d.text(380, 272, 'Cards move left to right. A full column takes no new work until a card moves on.', size=11.5, fill=INK2)
    d.save()


# ------------------------------------------------------------------ E
def e_system_design():
    d = D('ch14-system-design', 398, 'Template: a field app, end to end')
    d.group(20, 58, 470, 252, 'Flutter app, on the phone')
    xs = [(36, 56, 'UI', 'blue'), (112, 70, 'BLoC', 'blue'), (202, 96, 'Use cases', 'blue'), (318, 100, 'Repository', 'violet')]
    for x, w, t, col in xs:
        d.box(x, 92, w, 40, t, col)
    for (x, w, _, _), (nx, _, _, _) in zip(xs, xs[1:]):
        d.arrow(x + w, 112, nx, 112)
    d.box(280, 170, 176, 52, 'Local DB', 'green', sub='Drift + SQLCipher')
    d.box(280, 246, 176, 46, 'Sync engine', 'yellow', sub='outbox, push then pull')
    d.arrow(368, 132, 368, 170)
    d.arrow(368, 222, 368, 246, both=True)
    d.box(36, 170, 200, 52, 'Keystore / Keychain', 'violet', sub='tokens, database key')
    d.box(36, 246, 200, 46, 'Biometric unlock', 'grey', sub='local_auth')
    d.box(566, 86, 170, 52, 'Keycloak (SSO)', 'yellow', sub='OAuth2 + PKCE')
    d.box(566, 164, 170, 48, 'FCM / APNs', 'grey', sub='push notifications')
    d.box(566, 242, 170, 54, 'Backend REST API', 'orange', sub='HTTPS · JSON / XML')
    d.arrow(418, 104, 566, 104, 'login, tokens', lsize=11, dx=28)
    d.arrow(566, 188, 490, 188, 'push', lsize=11)
    d.arrow(456, 269, 566, 269, 'push / pull', both=True, lsize=11, dx=8)
    bottom = [('Crashlytics / Sentry', 'crash and performance monitoring'), ('CI/CD', 'GitHub Actions + Fastlane'),
              ('Stores', 'Play Store, App Store, staged rollout')]
    for i, (a, b) in enumerate(bottom):
        d.box(20 + i * 245, 330, 230, 50, a, 'white', sub=b)
    d.save()


ALL_D = [d1_mvc_mvp_mvvm, d1_bloc, d1_clean_architecture, d1_test_pyramid, d1_tdd,
         d2_bug_lifecycle, d2_severity_priority, d2_backward_compat,
         d3_sdlc, d3_waterfall_vs_agile, d3_v_model, d3_scrum, d3_burndown, d3_kanban,
         e_system_design]
