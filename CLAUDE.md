# Learn Mobile App Development (Flutter)

A general study project for becoming a professional mobile developer with Flutter, and for preparing for **job interviews and written exams** for mobile developer posts. It is not tied to any one employer.

It started on 21 Nov 2026 as a copy of an exam-prep book written for one job application; everything specific to that employer was removed. Do not bring employer-specific content back. When the user applies for a new job, put that job's material in its own folder (see "New job applications" below) and keep the book general.

## The learner

The main learner is a working Flutter developer who wants to fill gaps and practise for interviews and exams. Answers and notes are in **English**. Keep personal details (CV, ID numbers, phone numbers, addresses) out of this project and never send them to outside services.

## Learn to understand, not to memorize (the learner's main rule)

The learner says they are bad at memorizing. They want to **understand** each topic well enough to **use it in real work**, not to cram facts for one exam. Everything in this project follows from that:

- **Start from the problem.** Before naming a tool or term, show the real problem it solves ("the network drops mid-upload, what now?"). The name comes after the need is clear.
- **Explain the why.** Every rule, step or formula comes with the reason it exists, so the learner could rebuild it from scratch instead of recalling it. Derive formulas (for example, why nCr = nPr ÷ r!) rather than just stating them.
- **Build up from what they already know.** Link new ideas to Flutter work they have done (state, APIs, local databases, offline sync) and to the running example app.
- **Learn by doing.** Prefer small hands-on tasks: write a snippet, trace a flow, debug a broken example, design a small feature, draw the diagram from understanding. Run code where possible.
- **Practise applying, not recalling.** Questions should be scenarios ("a field officer's token expires offline, what should the app do and why?") and "what goes wrong if…" questions. Avoid pure recall ("list the 7 layers") unless a recall question is explicitly asked for exam practice; even then, teach the reasoning so the list rebuilds itself.
- **Few facts to hold, many ideas to understand.** Keep "must remember" items to the true minimum. A **Remember** line should be a reasoning rule ("never trust the client; check on the server"), not a list to cram. No mnemonic tricks as the main method.
- **When marking**, check whether the learner understood *why*, not only whether they wrote the right words. If an answer is right but shows no reasoning, ask a follow-up "why" or "what if" question.

## Folder contents

| Folder / file | What it is |
|---|---|
| `Book/` | **The book.** `00 - Contents and How to Use.md` is the cover and index. Chapters `A1`–`A3`, `B1`–`B4`, `C1`–`C2`, `D1`–`D3` teach one skill each (feature development · APIs, security, performance, push · publishing and CI/CD · architecture, testing, support, teamwork). `E - Revision Sheet and Long-Answer Templates.md` is the revision sheet (importance tags, top lines, common mistakes, all diagrams with short explanations, six long-answer templates with model answers). `F - Probability.md` is core maths for written exams |
| `Book/images/` | 73 SVG diagrams named by chapter (`a3-sync-cycle.svg`, `b2-pkce-flow.svg`, `f-tree-diagram.svg`, …). To change or add one, edit the Python files in `images/_generator/` (`part_a.py` … `part_f.py`, helpers in `lib.py`) and run `python3 build.py` there; never hand-edit the SVGs. Check new pictures visually (for example `qlmanage -t -s 1000 -o <dir> file.svg` on macOS) |
| `Book/images/web/` | 42 pictures from official documentation (Android, Flutter, Dart, Firebase, GitHub, MDN) and a few well-known sources, for **private study only**; `SOURCES.md` lists them. Keep this repository private |
| `Notes/` | Foundations: `Foundations 1 - OOP and DSA.md`, `Foundations 2 - Database and SQL.md` |
| `Practice/` | `Mistakes Log.md` (every miss, with the correct answer). Put practice sets, mock papers and marking files here |
| `.vscode/book.css` | The **book design** for the Markdown preview (paper page, coloured lesson boxes, tables, dark code blocks, collapsible answers, importance tags), loaded by `markdown.styles` in `.vscode/settings.json` |

Keep this table up to date when files are added.

## The book's style (follow it for all new material)

**Teach, don't list.** Every topic goes: a plain **Definition** (`box def`) → a **picture** → an **Example scenario** (`box story`: "Imagine: 1, 2, 3…" then "What happens?") → a **common question** as a heading with a direct answer (`box q`) → **what it means for a Flutter developer** (`box dev`) → the compact **Exam notes** (`<p class="label">Exam notes</p>`, tables and lists, key lines in `<mark>`) → a one-line **Remember** rule (`box rule`) → a **Quick check** (`box check`, MCQs with answers in `<details>`). Short, simple sentences.

**Pictures.** The learner learns best from diagrams. Add a diagram wherever a flow, structure or comparison is explained, drawn with the generator in the same style as the existing ones.

**The running example.** Most examples use one imaginary app: a **field app for a microfinance NGO** (field officers, members, branches, loans, visits with photos and GPS, weak rural network, Bangla and English). Use it for new examples too, so the book stays consistent; call it "the NGO" or "a field app", never a real organisation.

**Model answers** (in each chapter's "Model answers" section, each inside `<details>` with the question as the `<summary>`):
1. a green **In short** box (`box def`): the direct answer, the part to write first;
2. a **table** for every comparison, **points** or numbered steps for everything else, a picture where a flow or structure is explained, code where it is asked;
3. a yellow **Example** box (`box story`);
4. for long questions, numbered `####` parts and a brown **In the exam** box (`box exam`: how to shorten it on paper and what to draw);
5. a **From the book** block (`<div class="ref">`) with links to the sections it comes from: same chapter `[5. Title](#5-title)`, other chapter `[B2 · 11. Title](B2%20-%20….md#11-title)`.

Anchors are the heading ids the VS Code preview makes (lower case, spaces to hyphens, punctuation removed), so renaming a `## N.` heading breaks its links; keep `<mark>` and HTML out of numbered headings. After big edits, run a link check over `Book/` and `Notes/`.

**HTML wrappers used by the design:** `<div class="box def|story|q|dev|rule|you|exam|check">`, `<p class="label">`, `<div class="pair">`, `<details>`, `<div class="chapter-head">` (add `note` for pages that are not skill chapters), `<div class="ref">`, `<div class="book-nav">`, and importance tags `<span class="imp must|likely|know">`. Leave a blank line after an opening `<div>` so the Markdown inside is parsed.

## How to work here

- **Understand, then apply** (see the rule above): short notes that explain the why, hands-on tasks and scenario questions, the learner answers (often as photos of handwritten pages), Claude marks strictly with part marks, writes model answers in the format above, and adds every miss to `Practice/Mistakes Log.md`.
- Written exams for IT posts in Bangladesh often mix descriptive questions, short questions and MCQs, and may add core CS (OOP, DSA, DBMS/SQL, OS, networking, SDLC) and maths/aptitude (probability, permutation and combination) even when the job description does not mention them. Cover those too.
- **New job applications:** when the learner shares a job advert or ToR, make a folder `Jobs/<Employer> - <Post>/` with the advert (as Markdown), a mapping of each requirement to the book's chapters, and job-specific mocks. Do not edit the general book for one employer.
- New topics the book lacks become new chapters (next letter: `G`), written in the book's style, added to the Contents table and to the `book-nav` links.

## Git

Commit directly on `main`; do not create branches.
