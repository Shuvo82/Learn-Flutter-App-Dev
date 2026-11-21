# -*- coding: utf-8 -*-
"""Diagrams for Part B: B1 API integration, B2 security, B3 performance, B4 push and monitoring."""
from lib import D, C, INK, INK2, MUTED, SURF, EDGE, GRID, LIFE, tw


# ------------------------------------------------------------------ B1
def b1_status_codes():
    d = D('b1-status-codes', 300, 'HTTP status codes by family', 'The first digit tells you who has to act')
    fams = [
        ('1xx', 'Info', 'grey', 100, ['rare in apps'], '—'),
        ('2xx', 'Success', 'green', 136, ['200 OK', '201 Created', '204 No Content'], 'continue'),
        ('3xx', 'Redirect', 'blue', 128, ['304 Not Modified'], 'use the cache'),
        ('4xx', 'Client error', 'yellow', 186, ['400 Bad Request', '401 Unauthorized', '403 Forbidden', '404 Not Found',
                                                '409 Conflict', '422 Unprocessable', '429 Too Many Requests'],
         'fix the request;\ndo not blindly retry'),
        ('5xx', 'Server error', 'red', 148, ['500 Server Error', '502 Bad Gateway', '503 Unavailable',
                                             '504 Gateway Timeout'], 'retry later,\nwith backoff'),
    ]
    x = 24
    for code, name, col, w, lines, act in fams:
        d.rect(x, 66, w, 176, C[col][0], C[col][1], rx=8)
        d.text(x + 12, 94, code, size=20, anchor='start', weight='700')
        d.text(x + 12, 112, name, size=12, anchor='start', fill=INK2)
        for i, l in enumerate(lines):
            d.text(x + 12, 136 + i * 15.5, l, size=11, anchor='start', mono=True)
        d.text(x + w / 2, 262, act, size=11.5, fill=INK2)
        x += w + 5
    d.save()


def b1_rest_anatomy():
    d = D('b1-rest-anatomy', 224, 'Anatomy of a REST request')
    parts = [('GET', 'red', 'method:\nthe action', 12), ('https://api.example.org', 'grey', 'host', 2),
             ('/api/v1', 'yellow', 'version', 2), ('/branches', 'blue', 'resource:\na plural noun', 2),
             ('/102', 'violet', 'id of one\nresource', 2), ('/members', 'blue', 'sub-resource', 2),
             ('?status=active&page=2', 'green', 'query: filter\nand pagination', 0)]
    widths = [len(t) * 13 * 0.55 + 16 for t, _, _, _ in parts]
    total = sum(widths) + sum(g for _, _, _, g in parts)
    x = (760 - total) / 2
    for i, ((t, col, lab, gap), w) in enumerate(zip(parts, widths)):
        d.box(x, 62, w, 36, t, col, mono=True, size=13, r=6)
        cx = x + w / 2
        low = i % 2 == 0
        ty = 134 if low else 178
        d.line(cx, 98, cx, ty - 14, '#9a9892', 1)
        d.circle(cx, ty - 14, 2.5, '#9a9892')
        d.text(cx, ty, lab, size=11.5, fill=INK2)
        x += w + gap
    d.save()


def b1_layers():
    d = D('b1-layers', 232, 'Where the API call lives: clean layers')
    d.box(24, 96, 80, 48, 'UI', 'blue', size=13)
    d.box(134, 96, 140, 48, 'BLoC / ViewModel', 'yellow', size=13)
    d.box(304, 96, 120, 48, 'Repository', 'violet', size=13)
    d.box(468, 62, 152, 48, 'Remote data source', 'orange', sub='Dio')
    d.box(468, 130, 152, 48, 'Local data source', 'green', sub='Drift')
    d.box(650, 62, 88, 48, 'REST API', 'grey')
    d.box(650, 130, 88, 48, 'SQLite', 'grey')
    d.arrow(104, 120, 134, 120)
    d.arrow(274, 120, 304, 120)
    d.arrow(424, 110, 468, 90)
    d.arrow(424, 130, 468, 150)
    d.arrow(620, 86, 650, 86)
    d.arrow(620, 154, 650, 154)
    d.text(380, 212, 'The repository decides: local database first, network in the background.', size=12, fill=INK2)
    d.save()


def b1_sdk_vs_api():
    d = D('b1-sdk-vs-api', 206, 'SDK and API are not the same thing')
    d.group(20, 58, 404, 100, 'Inside your app')
    d.box(36, 86, 150, 58, 'Your code', 'blue')
    d.box(250, 86, 158, 58, 'SDK', 'violet', sub='ready-made library,\ntools and docs', size=13.5)
    d.box(500, 86, 104, 58, 'API', 'yellow', sub='the interface', size=13.5)
    d.box(644, 86, 96, 58, 'Service', 'grey', sub='maps, payments')
    d.arrow(186, 115, 250, 115, 'simple calls', lsize=11)
    d.arrow(408, 115, 500, 115, 'HTTP requests', lsize=11)
    d.arrow(604, 115, 644, 115)
    d.text(380, 186, 'The API is the interface you call. The SDK is packaged code that calls it for you.', size=12, fill=INK2)
    d.save()


# ------------------------------------------------------------------ B2
def b2_encoding_hashing_encryption():
    d = D('b2-encoding-hashing-encryption', 322, 'Encoding, hashing and encryption')
    rows = [
        (66, 'Encoding', 'grey', 'two-way, no key', 'Base64 encode', 'Rmx1dHRlcjE=', True,
         'Anyone can reverse it. It only changes the format, it hides nothing.'),
        (150, 'Hashing', 'violet', 'one-way', 'SHA-256 hash', 'fixed-length fingerprint', False,
         'Cannot be reversed. The same input always gives the same hash. Used for passwords (with a salt).'),
        (234, 'Encryption', 'yellow', 'two-way, with a key', 'AES encrypt + key', 'unreadable ciphertext', False,
         'Reversed only by someone who holds the key. Used for data at rest and in transit.'),
    ]
    for y, name, col, tag, proc, out, mono, cap in rows:
        d.text(24, y + 18, name, size=13.5, anchor='start', weight='700')
        d.text(24, y + 36, tag, size=11.5, anchor='start', fill=INK2)
        d.box(170, y, 118, 44, 'Flutter1', 'white', mono=True, weight='400')
        d.arrow(288, y + 22, 326, y + 22)
        d.box(326, y, 156, 44, proc, col)
        d.arrow(482, y + 22, 520, y + 22)
        d.box(520, y, 216, 44, out, 'white', mono=mono, weight='400')
        d.text(170, y + 62, cap, size=11.5, anchor='start', fill=INK2)
    d.save()


def b2_symmetric_asymmetric():
    d = D('b2-symmetric-asymmetric', 366, 'Symmetric and asymmetric encryption')

    def row(y):
        xs = [(30, 100, 'Plain text', 'white'), (176, 100, 'Encrypt', 'blue'), (322, 116, 'Cipher text', 'grey'),
              (484, 100, 'Decrypt', 'blue'), (630, 100, 'Plain text', 'white')]
        for x, w, t, col in xs:
            d.box(x, y, w, 42, t, col, weight='600' if col == 'blue' else '400')
        for (x, w, _, _), (nx, _, _, _) in zip(xs, xs[1:]):
            d.arrow(x + w, y + 21, nx, y + 21)

    d.text(24, 76, 'Symmetric: one shared secret key (AES). Fast.', size=13.5, anchor='start', weight='700')
    row(90)
    d.line(226, 132, 300, 158, '#9a9892', 1.2)
    d.line(534, 132, 460, 158, '#9a9892', 1.2)
    d.pill(380, 150, 'the SAME secret key', 'yellow')

    d.text(24, 214, 'Asymmetric: a key pair (RSA). Slow.', size=13.5, anchor='start', weight='700')
    row(228)
    d.line(226, 270, 226, 288, '#9a9892', 1.2)
    d.line(534, 270, 534, 288, '#9a9892', 1.2)
    d.pill(226, 288, "receiver's PUBLIC key", 'green')
    d.pill(534, 288, "receiver's PRIVATE key", 'red')
    d.text(380, 336, 'Digital signature is the reverse: sign with the PRIVATE key, anyone verifies with the PUBLIC key.',
           size=11.5, fill=INK2)
    d.text(380, 353, 'TLS uses both: asymmetric to agree on a key, then symmetric for the data.', size=11.5, fill=INK2)
    d.save()


def b2_jwt():
    d = D('b2-jwt', 292, 'A JWT has three parts, joined by dots')
    segs = [(40, 190, 'red', 'eyJhbGciOiJSUzI1NiJ9', 'HEADER', '{"alg":"RS256",\n "typ":"JWT"}'),
            (250, 270, 'violet', 'eyJzdWIiOiJ1MTIzIiwicm9sZXMi…', 'PAYLOAD (claims)',
             '{"sub":"u123","exp":1795000000,\n "roles":["FIELD_OFFICER"]}'),
            (540, 196, 'blue', 'SflKxwRJSMeKKF2QT4fw…', 'SIGNATURE', 'sign(header.payload,\n     private key)')]
    for x, w, col, enc, name, body in segs:
        d.box(x, 62, w, 38, enc, col, mono=True, size=11.5, weight='400', r=6)
        d.arrow(x + w / 2, 100, x + w / 2, 122, lw=1.3)
        d.rect(x, 122, w, 84, '#ffffff', C[col][1], rx=8)
        d.text(x + 12, 142, name, size=11.5, anchor='start', weight='700')
        d.text(x + 12, 164, body, size=11, anchor='start', mono=True, lh=1.45)
    d.text(240, 88, '.', size=26, weight='700')
    d.text(530, 88, '.', size=26, weight='700')
    d.line(40, 222, 520, 222, C['red'][1], 2)
    d.text(280, 244, 'Base64URL-encoded, NOT encrypted: anyone can read it.', size=12, weight='600')
    d.text(280, 262, 'Never put a password or a secret in the payload.', size=11.5, fill=INK2)
    d.line(540, 222, 736, 222, C['blue'][1], 2)
    d.text(638, 244, 'Tamper-proof', size=12, weight='600')
    d.text(638, 262, 'change one character and\nverification fails', size=11.5, fill=INK2)
    d.save()


def b2_token_refresh():
    d = D('b2-token-refresh', 362, 'Silent token refresh: what the app does on a 401')
    d.seq([(110, 'Mobile app', 'blue'), (380, 'Backend API', 'orange'), (650, 'Keycloak', 'yellow')], top=62, bottom=316)
    d.msg(0, 1, 132, 'GET /visits (expired access token)', n='1')
    d.msg(1, 0, 164, '401 Unauthorized', n='2', ncolor='red', dash=True)
    d.msg(0, 2, 204, 'POST /token (refresh token)', n='3')
    d.msg(2, 0, 236, 'new access token + new refresh token', n='4', ncolor='green', dash=True)
    d.msg(0, 1, 276, 'repeat GET /visits (new access token)', n='5')
    d.msg(1, 0, 308, '200 OK + data', n='6', ncolor='green', dash=True)
    d.text(380, 344, 'If step 3 fails, the refresh token is no longer valid: clear the tokens and go to login.', size=11.5, fill=INK2)
    d.save()


def b2_pkce_flow():
    d = D('b2-pkce-flow', 768, 'Login with OAuth 2.0 Authorization Code + PKCE',
          'Green = the PKCE secret  ·  blue = normal login  ·  orange = using the token')
    APP, BRW, KC, API = 90, 290, 490, 680
    top, hh, hw, bottom = 66, 46, 150, 680
    for x, label, sub, color in [(APP, 'Flutter app', '(public client)', 'blue'),
                                 (BRW, 'System browser', '(Custom Tab)', 'grey'),
                                 (KC, 'Keycloak', '(login server)', 'yellow'),
                                 (API, 'Backend API', '(Django)', 'orange')]:
        d.line(x, top + hh, x, bottom, color=LIFE, lw=1.2, dash=True)
        d.box(x - hw / 2, top, hw, hh, label, color, sub=sub, size=12.5, subsize=11)
    d._lx = [APP, BRW, KC, API]

    def note(x, y, w, n, color, title, lines):
        """A step that happens inside one box (no arrow)."""
        h = 30 + 14 * len(lines)
        f, st = C[color]
        d.rect(x, y, w, h, f, st, rx=8, sw=1.4)
        d.num(x + 16, y + 16, n, color, r=8.5)
        d.text(x + 31, y + 20, title, size=12, weight='700', anchor='start')
        for i, l in enumerate(lines):
            d.text(x + 31, y + 37 + i * 14, l, size=10.5, anchor='start', mono=True)
            if len(l) * 10.5 * 0.6 > w - 36:
                d.warn.append('note line too wide: %r' % l)

    def sep(y, label):
        d.line(24, y, 736, y, EDGE, 1.2, dash=True)
        w = tw(label, 11.5, True) + 30
        d.rect(380 - w / 2, y - 10, w, 20, SURF)
        d.pill(380, y - 11, label, 'grey')

    # 1. the app makes the secret pair
    note(16, 126, 262, '1', 'green', 'Make a secret pair',
         ['code_verifier  = random secret', 'code_challenge = SHA256(verifier)'])

    sep(204, 'the user logs in (in the browser)')
    d.msg(0, 1, 244, 'open /auth + code_challenge', n='2', ncolor='green')
    d.msg(1, 2, 274, 'show the login page', dash=True)
    d.msg(1, 2, 306, 'user types password (+OTP)', n='3', ncolor='blue')
    d.msg(2, 0, 342, 'redirect: myapp://callback?code=XYZ', n='4', ncolor='blue', dash=True)

    sep(366, 'swap the code for tokens')
    d.msg(0, 2, 406, 'POST /token: code + code_verifier', n='5', ncolor='green')
    note(KC - 130, 420, 260, '6', 'green', 'Keycloak checks',
         ['SHA256(code_verifier)', '  == saved code_challenge ?'])
    d.msg(2, 0, 512, 'match: access + refresh + ID token', dash=True)
    note(16, 526, 262, '7', 'blue', 'Save tokens securely', ['Keystore / Keychain'])

    sep(590, 'use the token')
    d.msg(0, 3, 630, 'GET /visits + Bearer <access_token>', n='8', ncolor='orange')
    d.msg(3, 0, 664, '200 OK + data   (401 = token expired, refresh it)', dash=True)

    # footer: why PKCE
    f, st = C['green']
    d.rect(10, 694, 740, 62, f, st, rx=8, sw=1.4)
    d.circle(32, 725, 11, st)
    d.polyline([(26.5, 725), (30.5, 729.5), (37.5, 720.5)], '#ffffff', lw=2.2)
    d.text(54, 717, 'Why PKCE? A bad app may steal the code at step 4. But it does not have the',
           size=12, weight='600', anchor='start')
    d.text(54, 735, 'code_verifier (it never left the phone), so step 6 fails. No verifier = no tokens.',
           size=12, weight='600', anchor='start')
    d.save()


def b2_google_oidc():
    d = D('b2-google-oidc', 560, '"Sign in with Google": OAuth 2.0 and OIDC working together')
    d.seq([(110, 'Flutter app', 'blue'), (380, 'Google (OIDC provider)', 'yellow'), (650, 'Your backend', 'orange')],
          top=62, bottom=372, hw=184)
    d.msg(0, 1, 132, 'login: scope = openid email profile', n='1')
    d.text(392, 160, 'user picks an account and agrees (consent)', size=11, fill=INK2, anchor='start')
    d.msg(1, 0, 190, 'one-time authorization code', n='2', dash=True)
    d.msg(0, 1, 226, 'POST /token  { code, code_verifier }', n='3')
    d.msg(1, 0, 262, 'ID token (JWT)  +  access token', n='4', ncolor='green', dash=True)
    d.msg(0, 2, 298, 'POST /auth/google  { id_token }', n='5')
    d.text(640, 322, "backend verifies: Google's key, iss, aud, exp", size=11, fill=INK2, anchor='end')
    d.msg(2, 0, 356, "your app's own session tokens", n='6', ncolor='green', dash=True)
    # the two tokens
    d.box(24, 392, 350, 116, 'ID token  =  OIDC  =  WHO?', 'violet', size=13.5,
          sub='always a JWT, meant for the app\nclaims: sub, email, name, iss, aud, exp\n"Rahim (sub 1098…) logged in at 10:02"',
          subsize=11.5)
    d.box(386, 392, 350, 116, 'Access token  =  OAuth 2.0  =  WHAT?', 'blue', size=13.5,
          sub='carries scopes: what the app may access\nsent as Bearer to an API (e.g. Google Drive)\nformat not fixed: Google opaque, Keycloak JWT',
          subsize=11.5)
    d.text(380, 534, 'Use the ID token to know the user. Use the access token to call APIs. Never swap them.',
           size=12, weight='600')
    d.save()


def b2_sso():
    d = D('b2-sso', 290, 'Single Sign-On: log in once, use many apps')
    d.box(24, 126, 86, 58, 'User', 'white', sub='one login')
    d.box(228, 114, 176, 82, 'Keycloak', 'yellow', sub='identity provider (IdP)\nusers · roles · MFA', size=14)
    apps = [(66, 'Field app (mobile)'), (133, 'Reporting app (mobile)'), (200, 'Web portal')]
    d.arrow(110, 155, 228, 155, 'password + OTP', lsize=11)
    for i, (y, name) in enumerate(apps):
        d.box(540, y, 196, 44, name, 'blue')
        d.arrow(404, 140 + i * 15, 540, y + 22, 'tokens' if i == 0 else None, dy=-8)
    d.text(638, 262, 'no second login', size=11.5, fill=INK2)
    d.text(260, 262, 'Disable a user once in Keycloak and every app is closed to them.', size=11.5, fill=INK2)
    d.save()


def b2_biometric_flow():
    d = D('b2-biometric-flow', 500, 'Biometric login: a quick unlock, not a replacement for server login')
    d.box(300, 58, 160, 36, 'App opens', 'grey')
    d.arrow(380, 94, 380, 112)
    d.diamond(380, 150, 200, 76, 'Fingerprint login\nenabled?', 'yellow')
    # No branch
    d.path([(280, 150), (140, 150), (140, 214)])
    d.text(214, 143, 'No', size=11.5, weight='600', fill=INK2)
    d.box(40, 214, 200, 52, 'Full login at Keycloak', 'blue', sub='password + OTP')
    d.arrow(140, 266, 140, 296)
    d.box(40, 296, 200, 44, 'Ask: enable fingerprint?', 'white')
    d.arrow(140, 340, 140, 370)
    d.box(40, 370, 200, 62, 'Store the refresh token', 'green', sub='in Keystore / Keychain,\nlocked by biometrics')
    # Yes branch
    d.path([(480, 150), (620, 150), (620, 214)])
    d.text(546, 143, 'Yes', size=11.5, weight='600', fill=INK2)
    d.box(520, 214, 200, 44, 'OS biometric prompt', 'violet')
    d.arrow(620, 258, 620, 282)
    d.diamond(620, 316, 130, 68, 'Match?', 'yellow')
    d.arrow(620, 350, 620, 378, 'Yes', dx=8, dy=4, anchor='start', lweight='600')
    d.box(510, 378, 220, 44, 'OS releases the refresh token', 'green')
    d.arrow(620, 422, 620, 444)
    d.box(520, 444, 200, 40, 'New access token → Home', 'green')
    d.path([(555, 316), (380, 316), (380, 240), (240, 240)])
    d.text(468, 334, 'No: fails several times,\nor a new fingerprint was added', size=11, fill=INK2)
    d.text(140, 462, 'The app never sees the fingerprint.\nThe OS only answers yes or no.', size=11.5, fill=INK2)
    d.save()


def b2_db_encryption():
    d = D('b2-db-encryption', 196, 'How the local database is encrypted')
    d.box(30, 66, 190, 64, 'Random 256-bit key', 'yellow', sub='created on first run')
    d.box(285, 66, 190, 64, 'Keystore / Keychain', 'violet', sub='hardware-backed,\nkey cannot be extracted')
    d.box(540, 66, 190, 64, 'SQLCipher database', 'green', sub='AES-256 encrypted file')
    d.arrow(220, 98, 285, 98, 'stored in')
    d.arrow(475, 98, 540, 98, 'opens')
    d.text(380, 166, 'A copied database file is useless without the key.', size=12, weight='600')
    d.save()


def b2_defence_in_depth():
    d = D('b2-defence-in-depth', 284, 'Defence in depth: an attacker must pass every layer')
    d.box(20, 124, 74, 50, 'Attacker', 'red')
    layers = [('Device', 'orange', 'screen lock\nbiometrics\nencrypted storage'),
              ('App', 'blue', 'obfuscation\ninput validation\nroot detection'),
              ('Network', 'violet', 'HTTPS / TLS\ncertificate pinning\nshort-lived tokens'),
              ('Server', 'yellow', 'authentication\nRBAC on every call\nrate limit, audit log')]
    x = 112
    d.arrow(94, 149, 112, 149)
    for name, col, body in layers:
        d.rect(x, 66, 122, 166, C[col][0], C[col][1], rx=8)
        d.text(x + 61, 92, name, size=13.5, weight='700')
        d.text(x + 61, 132, body, size=11.5, fill=INK2, lh=1.7)
        d.arrow(x + 122, 149, x + 138, 149)
        x += 138
    d.box(664, 124, 76, 50, 'Data', 'green', size=13.5)
    d.text(380, 262, 'No single control is enough: each layer still protects when another one fails.', size=12, fill=INK2)
    d.save()


# ------------------------------------------------------------------ B3
def b3_frame_budget():
    d = D('b3-frame-budget', 286, 'The frame budget: 16.67 ms per frame at 60 fps',
          'Example frame times. A frame that takes longer is dropped, and the user sees jank.')
    base, top, x0, x1 = 236, 86, 70, 734
    sc = (base - top) / 40.0
    for v in (0, 10, 20, 30, 40):
        y = base - v * sc
        d.line(x0, y, x1, y, '#b9b7b0' if v == 0 else GRID, 1)
        d.text(x0 - 8, y + 4, '%d ms' % v if v == 40 else str(v), size=11, anchor='end', fill=MUTED)
    vals = [9, 11, 8, 12, 10, 28, 9, 13, 11, 35, 10, 12]
    for i, v in enumerate(vals):
        cx = 104 + i * 53
        h = v * sc
        bad = v > 16.67
        col = C['red'][1] if bad else C['blue'][1]
        d.raw('<path d="M%.1f %.1f V%.1f Q%.1f %.1f %.1f %.1f H%.1f Q%.1f %.1f %.1f %.1f V%.1f Z" fill="%s"/>'
              % (cx - 11, base, base - h + 4, cx - 11, base - h, cx - 7, base - h,
                 cx + 7, cx + 11, base - h, cx + 11, base - h + 4, base, col))
        if bad:
            d.text(cx, base - h - 8, 'jank: %d ms' % v, size=11.5, weight='600')
    yb = base - 16.67 * sc
    d.line(x0, yb, x1, yb, INK2, 1.5)
    d.text(x1, yb - 6, 'budget 16.67 ms', size=11.5, anchor='end', weight='600')
    d.text(402, 258, 'frames, in order', size=11.5, fill=MUTED)
    d.rect(250, 266, 11, 11, C['blue'][1], rx=3)
    d.text(267, 276, 'frame on time', size=11.5, anchor='start', fill=INK2)
    d.rect(400, 266, 11, 11, C['red'][1], rx=3)
    d.text(417, 276, 'missed frame (jank)', size=11.5, anchor='start', fill=INK2)
    d.save()


def b3_render_pipeline():
    d = D('b3-render-pipeline', 290, 'How Flutter renders one frame')
    d.box(24, 104, 116, 50, 'User input', 'grey', sub='or setState()')
    d.group(166, 62, 338, 114, 'UI thread (Dart)')
    d.box(182, 104, 92, 50, 'BUILD', 'blue')
    d.box(290, 104, 92, 50, 'LAYOUT', 'blue')
    d.box(398, 104, 92, 50, 'PAINT', 'blue')
    d.group(530, 62, 126, 114, 'Raster thread')
    d.box(542, 104, 102, 50, 'RASTERIZE', 'violet')
    d.box(680, 104, 58, 50, 'Screen', 'green')
    for a, b in [(140, 182), (274, 290), (382, 398), (490, 542), (644, 680)]:
        d.arrow(a, 129, b, 129)
    d.text(335, 198, 'Jank here: heavy build(), large rebuilds,\nlong Dart calculations', size=11.5, fill=INK2)
    d.text(600, 198, 'Jank here: blur, clips,\nopacity layers, huge images', size=11.5, fill=INK2)
    d.arrow(166, 254, 656, 254, both=True, color='#9a9892')
    d.text(411, 274, 'all of this must fit in 16.67 ms', size=12, weight='600')
    d.save()


def b3_lazy_list():
    d = D('b3-lazy-list', 392, 'Why ListView.builder is faster for long lists')
    blue = C['blue']
    for cx, title, sub in [(200, 'ListView(children: [...])', 'builds all 1,000 items at once'),
                           (560, 'ListView.builder', 'builds only what is visible')]:
        d.text(cx, 76, title, size=13, weight='700', mono=True)
        d.text(cx, 94, sub, size=11.5, fill=INK2)
    for cx, lazy in [(200, False), (560, True)]:
        for i in range(9):
            y = 122 + i * 25
            if not lazy or i < 5:
                d.rect(cx - 62, y, 124, 18, blue[1], rx=4, opacity=0.85)
            elif i == 5:
                d.rect(cx - 62, y, 124, 18, blue[0], blue[1], rx=4, sw=1.2)
            else:
                d.rect(cx - 62, y, 124, 18, 'none', '#b9b7b0', rx=4, sw=1.2, dash=True)
        d.rect(cx - 74, 112, 148, 132, 'none', '#1c1c1a', rx=12, sw=2.5)
        d.text(cx + 84, 180, 'screen', size=11.5, anchor='start', fill=INK2)
    d.text(84, 300, 'built, but\nnot visible', size=11.5, anchor='end', fill=INK2)
    d.text(644, 258, 'small buffer', size=11.5, anchor='start', fill=INK2)
    d.text(644, 300, 'not built yet', size=11.5, anchor='start', fill=INK2)
    d.text(200, 366, '… and 991 more: more memory, slow first frame', size=11.5, fill=INK2)
    d.text(560, 366, 'less memory, fast, rows are recycled while scrolling', size=11.5, fill=INK2)
    d.save()


def b3_memory_leak():
    d = D('b3-memory-leak', 270, 'What a memory leak looks like', 'Shape only, not measured data')
    blue, org = C['blue'][1], C['orange'][1]
    x0, x1, base = 60, 540, 226
    d.line(x0, base, x1, base, '#b9b7b0', 1)
    d.line(x0, 96, x1, 96, C['red'][1], 1.2)
    d.text(x0, 88, 'OS memory limit: above this the app is killed (OOM)', size=11.5, anchor='start', fill=INK2)
    healthy = [(60, 200), (120, 178), (180, 198), (240, 176), (300, 199), (360, 177), (420, 198), (480, 178), (540, 196)]
    leak = [(60, 200), (120, 186), (180, 178), (240, 160), (300, 152), (360, 134), (420, 126), (480, 108), (522, 97)]
    d.polyline(healthy, blue, lw=2)
    d.polyline(leak, org, lw=2)
    d.circle(540, 196, 5, blue, SURF, sw=2)
    d.circle(522, 97, 5, org, SURF, sw=2)
    d.text(554, 192, 'Healthy app', size=12, anchor='start', weight='600')
    d.text(554, 208, 'memory comes back after\ngarbage collection', size=11.5, anchor='start', fill=INK2)
    d.text(554, 108, 'App with a leak', size=12, anchor='start', weight='600')
    d.text(554, 124, 'memory only grows until\nthe OS kills the app', size=11.5, anchor='start', fill=INK2)
    d.text(300, 248, 'time spent using the app', size=11.5, fill=MUTED)
    d.text(x0, 66, '', size=1)
    d.line(250, 62, 274, 62, blue, 2)
    d.text(280, 66, 'healthy', size=11.5, anchor='start', fill=INK2)
    d.line(350, 62, 374, 62, org, 2)
    d.text(380, 66, 'leaking', size=11.5, anchor='start', fill=INK2)
    d.save()


def b3_batching():
    d = D('b3-batching', 244, 'Batch network calls: wake the radio once, not ten times')
    strong, soft = C['orange'][1], '#f6c9b3'
    for y, name, hint, n in [(72, 'One request per record', 'the radio wakes 10 times', 10),
                             (150, 'One batched sync', 'the radio wakes once', 1)]:
        d.text(24, y + 16, name, size=13, anchor='start', weight='700')
        d.text(24, y + 34, hint, size=11.5, anchor='start', fill=INK2)
        d.line(216, y + 40, 736, y + 40, '#b9b7b0', 1)
        for i in range(n):
            x = 224 + i * 51
            w = 12 if n > 1 else 30
            d.rect(x, y + 6, w, 34, strong, rx=2)
            d.rect(x + w + 2, y + 28, 30, 12, soft, rx=2)
    d.rect(224, 214, 11, 11, strong, rx=3)
    d.text(241, 224, 'sending data', size=11.5, anchor='start', fill=INK2)
    d.rect(350, 214, 11, 11, soft, rx=3)
    d.text(367, 224, 'radio stays awake for a while after each request', size=11.5, anchor='start', fill=INK2)
    d.save()


# ------------------------------------------------------------------ B4
def b4_push_flow():
    d = D('b4-push-flow', 392, 'How a push notification reaches the phone')
    d.box(30, 162, 150, 64, 'Your app', 'blue', sub='on the phone', size=13.5)
    d.box(300, 62, 170, 60, 'FCM', 'yellow', sub='Firebase Cloud Messaging', size=13.5)
    d.box(300, 258, 170, 60, 'Your backend', 'violet', sub='stores token + user ID', size=13.5)
    d.box(590, 52, 146, 48, 'Android phone', 'green')
    d.box(590, 136, 146, 48, 'APNs', 'orange', sub='Apple')
    d.box(590, 226, 146, 48, 'iPhone', 'green')
    d.path([(80, 162), (80, 78), (300, 78)])
    d.num(92, 96, '1')
    d.text(190, 72, 'register', size=11.5, fill=INK2)
    d.path([(300, 106), (130, 106), (130, 162)])
    d.num(142, 124, '2')
    d.text(215, 122, 'device token', size=11.5, fill=INK2)
    d.path([(105, 226), (105, 288), (300, 288)])
    d.num(117, 262, '3')
    d.text(204, 306, 'send token + user ID (HTTPS)', size=11.5, fill=INK2)
    d.arrow(385, 258, 385, 122)
    d.num(385, 190, '4')
    d.text(402, 186, 'event happens:\ncall the FCM HTTP v1 API', size=11.5, anchor='start', fill=INK2)
    d.arrow(470, 82, 590, 76)
    d.num(530, 66, '5')
    d.arrow(470, 104, 590, 156)
    d.text(520, 152, 'iOS goes\nthrough APNs', size=11, anchor='end', fill=INK2)
    d.arrow(663, 184, 663, 226)
    d.box(30, 340, 706, 36, 'The app never sends pushes itself. The FCM server key stays on your backend.', 'red', weight='600')
    d.save()


def b4_crash_free():
    d = D('b4-crash-free', 240, 'Crash-free users', 'Each dot is one active user in the period')
    blue, red = C['blue'][1], C['red'][1]
    for r in range(5):
        for c in range(20):
            bad = (r == 2 and c == 13)
            d.circle(46 + c * 22, 84 + r * 22, 7, red if bad else blue)
    d.text(620, 118, '99%', size=38, weight='700')
    d.text(620, 142, 'crash-free users', size=12.5, fill=INK2)
    d.text(620, 170, '(1 − 1 ÷ 100) × 100', size=12, mono=True)
    d.circle(46, 208, 6, blue)
    d.text(60, 212, 'no crash: 99 users', size=11.5, anchor='start', fill=INK2)
    d.circle(206, 208, 6, red)
    d.text(220, 212, 'crashed at least once: 1 user', size=11.5, anchor='start', fill=INK2)
    d.save()


def b4_monitoring_loop():
    d = D('b4-monitoring-loop', 326, 'The monitoring loop after every release')
    B = [d.box(295, 62, 170, 46, 'Staged rollout', 'green'),
         d.box(511, 112, 190, 50, 'Watch crash-free users', 'blue', sub='and new issues'),
         d.box(511, 208, 190, 50, 'Triage', 'blue', sub='sort by users affected'),
         d.box(295, 262, 170, 46, 'Reproduce', 'yellow', sub='device, OS, breadcrumbs'),
         d.box(59, 208, 190, 50, 'Fix + regression test', 'violet'),
         d.box(59, 112, 190, 50, 'Hotfix release', 'green', sub='higher build number')]
    d.path([(465, 85), (606, 85), (606, 112)])
    d.arrow(606, 162, 606, 208)
    d.path([(606, 258), (606, 285), (465, 285)])
    d.path([(295, 285), (154, 285), (154, 258)])
    d.arrow(154, 208, 154, 162)
    d.path([(154, 112), (154, 85), (295, 85)])
    d.text(380, 180, 'Repeat for', size=12, fill=INK2)
    d.text(380, 197, 'every release', size=12, fill=INK2)
    d.save()


ALL_B = [b1_status_codes, b1_rest_anatomy, b1_layers, b1_sdk_vs_api,
         b2_encoding_hashing_encryption, b2_symmetric_asymmetric, b2_jwt, b2_token_refresh, b2_pkce_flow, b2_google_oidc, b2_sso,
         b2_biometric_flow, b2_db_encryption, b2_defence_in_depth,
         b3_frame_budget, b3_render_pipeline, b3_lazy_list, b3_memory_leak, b3_batching,
         b4_push_flow, b4_crash_free, b4_monitoring_loop]
