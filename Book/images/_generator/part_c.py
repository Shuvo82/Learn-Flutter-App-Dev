# -*- coding: utf-8 -*-
"""Diagrams for Part C: C1 store publishing and signing, C2 CI/CD, Git and cloud."""
from lib import D, C, INK, INK2, MUTED, SURF, EDGE, GRID, tw


# ------------------------------------------------------------------ C1
def c1_release_path():
    d = D('ch08-release-path', 246, 'Release management: the whole path of one version')
    row1 = [('Code freeze', 'blue'), ('Version bump', 'blue'), ('Release build', 'blue'), ('Sign', 'yellow'),
            ('Test\ninternal / beta', 'yellow')]
    row2 = [('Store listing +\npolicy forms', 'violet'), ('Submit for\nreview', 'violet'), ('Staged rollout', 'green'),
            ('Monitor crashes\nand reviews', 'green'), ('100% of users', 'green')]
    xs = [28 + i * 144 for i in range(5)]
    for i, (t, col) in enumerate(row1):
        d.box(xs[i], 62, 128, 48, t, col)
        if i < 4:
            d.arrow(xs[i] + 128, 86, xs[i + 1], 86)
    d.arrow(xs[4] + 64, 110, xs[4] + 64, 150)
    for i, (t, col) in enumerate(row2):
        x = xs[4 - i]
        d.box(x, 150, 128, 48, t, col)
        if i < 4:
            d.arrow(x, 174, xs[3 - i] + 128, 174)
    d.text(28, 224, 'then: the next release, or a hotfix', size=11.5, anchor='start', fill=INK2)
    d.save()


def c1_version():
    d = D('ch08-version-number', 262, 'Reading a version number', 'pubspec.yaml    version: 1.4.2+37')
    parts = [(176, 72, '1', 'violet', 'MAJOR', 'breaking change'), (286, 72, '4', 'blue', 'MINOR', 'new feature'),
             (396, 72, '2', 'green', 'PATCH', 'bug fix'), (522, 96, '37', 'yellow', 'BUILD', 'goes up on every upload')]
    for x, w, t, col, name, hint in parts:
        d.box(x, 70, w, 62, t, col, size=30, mono=True, weight='700')
        d.text(x + w / 2, 152, name, size=12, weight='700')
        d.text(x + w / 2, 168, hint, size=11.5, fill=INK2)
    d.text(267, 116, '.', size=34, weight='700')
    d.text(377, 116, '.', size=34, weight='700')
    d.text(495, 112, '+', size=30, weight='700')
    d.line(176, 190, 468, 190, INK2, 1.5)
    d.text(322, 212, 'Shown to users', size=12, weight='700')
    d.text(322, 229, 'Android versionName', size=11.5, fill=INK2)
    d.text(322, 245, 'iOS Version (CFBundleShortVersionString)', size=11.5, fill=INK2)
    d.line(522, 190, 618, 190, INK2, 1.5)
    d.text(600, 212, 'Internal counter', size=12, weight='700')
    d.text(600, 229, 'Android versionCode', size=11.5, fill=INK2)
    d.text(600, 245, 'iOS Build (CFBundleVersion)', size=11.5, fill=INK2)
    d.save()


def c1_android_signing():
    d = D('ch08-android-signing', 236, 'Android: Play App Signing uses two keys')
    d.group(20, 58, 330, 150, 'You')
    d.group(386, 58, 354, 150, 'Google Play')
    d.box(36, 96, 124, 52, 'Build the AAB', 'blue')
    d.box(196, 96, 138, 52, 'Sign with the', 'yellow', sub='UPLOAD key', subink=INK, subsize=12.5)
    d.box(400, 96, 96, 52, 'Verify the', 'grey', sub='upload key', subink=INK, subsize=12.5, weight='400')
    d.box(512, 96, 130, 52, 'Re-sign with the', 'yellow', sub='APP SIGNING key', subink=INK, subsize=12.5)
    d.box(658, 96, 70, 52, 'Small', 'green', sub='APKs', subink=INK, subsize=12.5)
    d.arrow(160, 122, 196, 122)
    d.arrow(334, 122, 400, 122, 'upload', lsize=11)
    d.arrow(496, 122, 512, 122)
    d.arrow(642, 122, 658, 122)
    d.arrow(693, 148, 693, 172)
    d.text(693, 190, "users' phones", size=11.5, fill=INK2)
    d.text(36, 184, 'Lost or leaked upload key? Google can reset it.', size=11.5, anchor='start', fill=INK2)
    d.text(400, 184, 'Google keeps the app signing key safe.', size=11.5, anchor='start', fill=INK2)
    d.save()


def c1_ios_signing():
    d = D('ch08-ios-signing', 284, 'iOS: what a provisioning profile ties together')
    a = d.box(24, 62, 190, 46, 'Certificate', 'violet', sub='WHO: the developer')
    b = d.box(24, 122, 190, 46, 'App ID (Bundle ID)', 'blue', sub='WHAT: which app')
    c = d.box(24, 182, 190, 46, 'Devices + entitlements', 'grey', sub='WHERE, and what it may do')
    p = d.box(270, 112, 136, 66, 'Provisioning\nprofile', 'yellow', size=13.5)
    d.arrow(214, 85, 270, 128)
    d.arrow(214, 145, 270, 145)
    d.arrow(214, 205, 270, 162)
    ipa = d.box(446, 122, 100, 46, 'Signed IPA', 'green')
    asc = d.box(586, 122, 150, 46, 'App Store Connect', 'grey')
    d.arrow(406, 145, 446, 145)
    d.arrow(546, 145, 586, 145)
    tf = d.box(446, 216, 130, 44, 'TestFlight', 'blue', sub='beta testers')
    ar = d.box(606, 216, 130, 44, 'App Review', 'blue', sub='then the App Store')
    d.arrow(630, 168, 530, 216)
    d.arrow(680, 168, 680, 216)
    d.text(338, 200, 'development · ad hoc\n· App Store', size=11, fill=INK2)
    d.save()


def c1_staged_rollout():
    d = D('ch08-staged-rollout', 270, 'Staged rollout: release to a small share of users first',
          'Share of users who receive the new version')
    base, top = 220, 92
    sc = (base - top) / 100.0
    col = C['blue'][1]
    for v in (0, 50, 100):
        y = base - v * sc
        d.line(70, y, 520, y, '#b9b7b0' if v == 0 else GRID, 1)
        d.text(62, y + 4, '%d%%' % v, size=11, anchor='end', fill=MUTED)
    for i, v in enumerate([5, 20, 50, 100]):
        cx = 130 + i * 112
        h = v * sc
        r = min(4, h / 2)
        d.raw('<path d="M%.1f %.1f V%.1f Q%.1f %.1f %.1f %.1f H%.1f Q%.1f %.1f %.1f %.1f V%.1f Z" fill="%s"/>'
              % (cx - 12, base, base - h + r, cx - 12, base - h, cx - 12 + r, base - h,
                 cx + 12 - r, cx + 12, base - h, cx + 12, base - h + r, base, col))
        d.text(cx, base - h - 7, '%d%%' % v, size=12, weight='600')
        d.text(cx, base + 18, 'Stage %d' % (i + 1), size=11.5, fill=INK2)
    d.text(556, 104, 'At every stage', size=12.5, anchor='start', weight='700')
    for i, t in enumerate(['watch crash-free users', 'check for new issues', 'a problem? HALT the rollout',
                           'there is no rollback:', 'ship a higher version']):
        if i != 4:
            d.circle(562, 124 + i * 20, 2.5, INK2)
        d.text(572, 128 + i * 20, t, size=11.5, anchor='start', fill=INK2)
    d.save()


# ------------------------------------------------------------------ C2
def c2_ci_cd():
    d = D('ch09-ci-cd', 308, 'CI, Continuous Delivery and Continuous Deployment')
    stages = [('Commit', 150), ('Build', 262), ('Test', 374), ('Package', 486), ('Production', 672)]
    rows = [(74, 'Continuous\nIntegration', 3), (150, 'Continuous\nDelivery', 5), (226, 'Continuous\nDeployment', 5)]
    for y, name, n in rows:
        d.text(24, y + 16, name, size=12.5, anchor='start', weight='700')
        for i in range(n):
            t, cx = stages[i]
            col = 'green' if t == 'Production' else 'blue'
            w = 100 if t == 'Production' else 92
            d.box(cx - w / 2, y, w, 38, t, col)
            if 0 < i < 4:
                d.arrow(stages[i - 1][1] + 46, y + 19, cx - 46, y + 19)
    d.text(436, 97, 'every push is built and tested automatically', size=11.5, anchor='start', fill=INK2)
    # delivery: manual gate
    d.arrow(532, 169, 548, 169)
    d.pill(578, 158, 'approve', 'yellow', size=11)
    d.arrow(608, 169, 622, 169)
    d.text(578, 204, 'a person approves the release', size=11.5, fill=INK2)
    # deployment: all automatic
    d.arrow(532, 245, 622, 245, 'automatic', lsize=11)
    d.text(380, 292, 'Mobile apps normally use Continuous Delivery, because the stores review every release.',
           size=12, weight='600')
    d.save()


def c2_pipeline():
    d = D('ch09-pipeline', 330, 'A mobile CI/CD pipeline')
    xs = [40, 216, 392, 568]
    row1 = [('1', 'Checkout', 'source code', 'grey'), ('2', 'Setup', 'Flutter, pub get (cached)', 'grey'),
            ('3', 'Analyze', 'format, lint', 'blue'), ('4', 'Test', 'unit + widget tests', 'blue')]
    row2 = [('5', 'Build', 'AAB / IPA', 'violet'), ('6', 'Sign', 'keystore / certificate', 'yellow'),
            ('7', 'Distribute', 'Firebase, TestFlight,\nPlay internal track', 'green'), ('8', 'Notify', 'Slack / email', 'grey')]
    d.text(40, 70, 'Every pull request runs steps 1 to 4. They must pass before the merge.', size=11.5, anchor='start', fill=INK2)
    d.line(40, 78, 720, 78, C['blue'][1], 2)
    for i, (n, t, s, col) in enumerate(row1):
        d.box(xs[i], 92, 152, 62, t, col, sub=s, size=13)
        d.num(xs[i], 92, n, col)
        if i < 3:
            d.arrow(xs[i] + 152, 123, xs[i + 1], 123)
    d.arrow(xs[3] + 76, 154, xs[3] + 76, 200)
    for i, (n, t, s, col) in enumerate(row2):
        x = xs[3 - i]
        d.box(x, 200, 152, 62, t, col, sub=s, size=13)
        d.num(x, 200, n, col)
        if i < 3:
            d.arrow(x, 231, xs[2 - i] + 152, 231)
    d.text(40, 290, 'Merge to main: steps 1 to 7, the build goes to testers.', size=11.5, anchor='start', fill=INK2)
    d.text(40, 308, 'Version tag (v1.4.2): build the store release and upload it for a staged rollout.', size=11.5, anchor='start', fill=INK2)
    d.save()


def c2_tools():
    d = D('ch09-ci-and-fastlane', 270, 'The CI service and Fastlane do different jobs')
    d.group(30, 58, 460, 190, 'CI service: GitHub Actions / GitLab CI / Bitrise')
    d.text(42, 96, 'Decides WHEN to run (push, pull request, tag) and gives the machine.', size=11.5, anchor='start', fill=INK2)
    d.box(48, 118, 150, 62, 'Analyze + test', 'blue', sub='flutter analyze\nflutter test', submono=True, subsize=10.5)
    d.box(248, 118, 222, 62, 'Fastlane lanes', 'yellow', sub='sign · build · upload', size=13.5)
    d.arrow(198, 149, 248, 149)
    d.text(42, 220, 'Fastlane is not a CI server: it runs inside one, or on your laptop.', size=11.5, anchor='start', weight='600')
    d.box(566, 96, 170, 46, 'TestFlight / App Store', 'green')
    d.box(566, 170, 170, 46, 'Google Play', 'green')
    d.arrow(470, 140, 566, 119)
    d.arrow(470, 158, 566, 193)
    d.save()


def c2_git_flow():
    d = D('ch09-git-flow', 338, 'Git Flow: branches for a team that releases to the stores')
    lanes = [('main', 86, 'blue'), ('hotfix/*', 136, 'red'), ('release/*', 186, 'yellow'), ('develop', 236, 'violet'),
             ('feature/*', 286, 'green')]
    Y = {n: y for n, y, _ in lanes}
    COL = {n: C[c][1] for n, _, c in lanes}
    for n, y, c in lanes:
        d.text(24, y + 4, n, size=12, anchor='start', weight='700', mono=True)
        d.line(124, y, 736, y, GRID, 1)

    def seg(a, b, col, dash=False):
        d.line(a[0], a[1], b[0], b[1], col, 2, dash=dash)

    m = [(150, Y['main']), (340, Y['main']), (650, Y['main'])]
    dv = [(190, Y['develop']), (360, Y['develop']), (430, Y['develop']), (490, Y['develop']), (704, Y['develop'])]
    ft = [(240, Y['feature/*']), (300, Y['feature/*'])]
    hf = [(260, Y['hotfix/*'])]
    rl = [(540, Y['release/*']), (600, Y['release/*'])]
    # main and develop trunks
    seg(m[0], m[1], COL['main']); seg(m[1], m[2], COL['main'])
    for a, b in zip(dv, dv[1:]):
        seg(a, b, COL['develop'])
    seg(m[0], dv[0], COL['develop'])
    # feature
    seg(dv[0], ft[0], COL['feature/*']); seg(ft[0], ft[1], COL['feature/*']); seg(ft[1], dv[1], COL['feature/*'])
    # hotfix
    seg(m[0], hf[0], COL['hotfix/*']); seg(hf[0], m[1], COL['hotfix/*']); seg(hf[0], dv[2], COL['hotfix/*'], dash=True)
    # release
    seg(dv[3], rl[0], COL['release/*']); seg(rl[0], rl[1], COL['release/*']); seg(rl[1], m[2], COL['release/*'])
    seg(rl[1], dv[4], COL['release/*'], dash=True)
    for pts, n in [(m, 'main'), (dv, 'develop'), (ft, 'feature/*'), (hf, 'hotfix/*'), (rl, 'release/*')]:
        for x, y in pts:
            d.circle(x, y, 6, COL[n], SURF, sw=2)
    for (x, y), tag in zip(m, ['v1.4.0', 'v1.4.1', 'v1.5.0']):
        d.text(x, y - 14, tag, size=11, weight='700', mono=True)
    d.text(242, Y['hotfix/*'] + 18, 'urgent fix', size=11, anchor='end', fill=INK2)
    d.text(570, Y['release/*'] + 20, 'bug fixes only', size=11, fill=INK2)
    d.text(270, Y['feature/*'] + 24, 'pull request + review + CI', size=11, fill=INK2)
    d.text(580, Y['feature/*'] + 24, 'dashed line = merged back into develop', size=11, fill=INK2)
    d.save()


def c2_merge_vs_rebase():
    d = D('ch09-merge-vs-rebase', 282, 'git merge and git rebase')
    blue, green, yel = C['blue'], C['green'], C['yellow']

    def dot(x, y, t, col, dash=False):
        d.circle(x, y, 14, col[0], col[1], sw=1.8, dash=dash)
        d.text(x, y + 4.5, t, size=12, weight='700')

    def ln(a, b, col=INK2, dash=False):
        d.line(a[0], a[1], b[0], b[1], col, 1.8, dash=dash)

    # merge
    d.text(190, 70, 'merge', size=14, weight='700', mono=True)
    A, B, Cc, M = (50, 112), (120, 112), (210, 112), (310, 112)
    Dd, E = (170, 178), (250, 178)
    for a, b in [(A, B), (B, Cc), (Cc, M), (B, Dd), (Dd, E), (E, M)]:
        ln(a, b)
    for p, t in [(A, 'A'), (B, 'B'), (Cc, 'C')]:
        dot(p[0], p[1], t, blue)
    dot(Dd[0], Dd[1], 'D', green)
    dot(E[0], E[1], 'E', green)
    dot(M[0], M[1], 'M', yel)
    d.text(334, 116, 'main', size=11.5, anchor='start', fill=INK2)
    d.text(274, 182, 'feature', size=11.5, anchor='start', fill=INK2)
    d.text(190, 232, 'Keeps the true history.', size=12, weight='600')
    d.text(190, 250, 'Adds a merge commit (M).', size=11.5, fill=INK2)
    d.line(380, 66, 380, 262, EDGE, 1.2)
    # rebase
    d.text(570, 70, 'rebase', size=14, weight='700', mono=True)
    pts = [(420, 112, 'A', blue), (480, 112, 'B', blue), (540, 112, 'C', blue), (610, 112, "D'", green), (680, 112, "E'", green)]
    for (x1, y1, _, _), (x2, y2, _, _) in zip(pts, pts[1:]):
        ln((x1, y1), (x2, y2))
    ln((480, 112), (520, 178), '#b9b7b0', dash=True)
    ln((520, 178), (590, 178), '#b9b7b0', dash=True)
    d.circle(520, 178, 14, SURF, '#b9b7b0', sw=1.5, dash=True)
    d.text(520, 182.5, 'D', size=12, fill=MUTED)
    d.circle(590, 178, 14, SURF, '#b9b7b0', sw=1.5, dash=True)
    d.text(590, 182.5, 'E', size=12, fill=MUTED)
    d.text(614, 182, 'old commits, dropped', size=11.5, anchor='start', fill=MUTED)
    for x, y, t, col in pts:
        dot(x, y, t, col)
    d.text(708, 116, 'main', size=11.5, anchor='start', fill=INK2)
    d.text(570, 232, 'Linear history, but commits are rewritten.', size=12, weight='600')
    d.text(570, 250, 'Never rebase a shared branch.', size=11.5, fill=INK2)
    d.save()


def c2_cloud_models():
    d = D('ch09-cloud-models', 316, 'Cloud service models: who manages what')
    you, prov = C['blue'], C['grey']
    std = ['Application', 'Data', 'Runtime', 'Operating system', 'Servers, network']
    cols = [('IaaS', 'e.g. AWS EC2', std, 4), ('PaaS', 'e.g. Google App Engine', std, 2), ('SaaS', 'e.g. Gmail', std, 0),
            ('BaaS', 'e.g. Firebase', ['Your mobile app', 'Login (Auth)', 'Database', 'Storage, push, functions',
                                       'Servers, network'], 1)]
    for i, (name, eg, layers, n) in enumerate(cols):
        x = 40 + i * 176
        d.text(x + 76, 76, name, size=15, weight='700')
        d.text(x + 76, 94, eg, size=11.5, fill=INK2)
        for j, l in enumerate(layers):
            c = you if j < n else prov
            d.box(x, 106 + j * 34, 152, 30, l, 'blue' if j < n else 'grey', weight='600' if j < n else '400', size=11.5, r=5)
    d.rect(232, 290, 12, 12, you[0], you[1], rx=3)
    d.text(250, 300, 'you manage', size=11.5, anchor='start', fill=INK2)
    d.rect(360, 290, 12, 12, prov[0], prov[1], rx=3)
    d.text(378, 300, 'the provider manages', size=11.5, anchor='start', fill=INK2)
    d.save()


def c2_container_vs_vm():
    d = D('ch09-container-vs-vm', 318, 'Virtual machines and containers')
    # VMs
    x = 40
    d.text(x + 160, 74, 'Virtual machines', size=13.5, weight='700')
    for cx in (x, x + 168):
        d.box(cx, 88, 152, 40, 'App', 'blue')
        d.box(cx, 132, 152, 44, 'Guest OS', 'orange', sub='a full operating system')
    d.box(x, 180, 320, 30, 'Hypervisor', 'grey', weight='400')
    d.box(x, 214, 320, 30, 'Hardware', 'grey', weight='400')
    d.text(x + 160, 270, 'Each VM carries a full OS:', size=12, weight='600')
    d.text(x + 160, 288, 'heavy, slow to start, strongly isolated.', size=11.5, fill=INK2)
    # containers
    x = 400
    d.text(x + 160, 74, 'Containers (Docker)', size=13.5, weight='700')
    for i in range(3):
        d.box(x + i * 109, 88, 102, 50, 'App', 'blue', sub='+ its libraries')
    d.box(x, 142, 320, 30, 'Docker engine', 'violet', weight='400')
    d.box(x, 176, 320, 34, 'Host OS', 'orange', sub='one shared kernel')
    d.box(x, 214, 320, 30, 'Hardware', 'grey', weight='400')
    d.text(x + 160, 270, 'Containers share the host kernel:', size=12, weight='600')
    d.text(x + 160, 288, 'light, start in seconds.', size=11.5, fill=INK2)
    d.save()


ALL_C = [c1_release_path, c1_version, c1_android_signing, c1_ios_signing, c1_staged_rollout,
         c2_ci_cd, c2_pipeline, c2_tools, c2_git_flow, c2_merge_vs_rebase, c2_cloud_models, c2_container_vs_vm]
