<div class="cover">
<div class="cover-kicker">A practical book for Flutter and mobile developers</div>

# Learn Mobile App Development

<div class="cover-sub">Flutter · Dart · Android · iOS · DevOps · Teamwork</div>
<div class="cover-line">14 chapters · lessons, pictures, quick checks, practice questions and model answers</div>
</div>

**Who it is for:** anyone who wants to become a professional mobile developer with Flutter, or prepare for a **job interview** or a **written exam** for a mobile developer post. It covers what job adverts ask for: Flutter and Dart, a little native Android and iOS, offline data, APIs, security, performance, publishing, CI/CD, architecture, testing and teamwork.

**The running example.** Most examples use one imaginary app: **a field app for a microfinance NGO**. Field officers visit members in villages with a weak network. They register members, record visits with photos and GPS, and collect loan installments, and the app syncs when the network returns. The data is financial, so it must be safe. This one app touches almost every topic in the book. When a question names a different app, use the same ideas with its words.

<div class="box exam">

**How to open the book.** Open any chapter file and press `Ctrl+Shift+V`. The preview shows the book design: paper page, coloured lesson boxes, pictures, and answers that open when you click them. In the plain editor you see the same text with a few `<div>` tags.

</div>

## Contents

| Part | Chapter | What you learn | Size |
|---|---|---|---|
| **A. Mobile Application Feature Development** | [A1 — Flutter, Dart and Native](A1%20-%20Flutter,%20Dart%20and%20Native.md) | Cross-Platform & Native Coding | Large |
| | [A2 — UI-UX Implementation](A2%20-%20UI-UX%20Implementation.md) | Material Design, iOS HIG, responsive UI | Medium |
| | [A3 — Offline Storage and Data Sync](A3%20-%20Offline%20Storage%20and%20Data%20Sync.md) | SQLite, Room, Core Data, Hive, Realm, background sync | Large ⭐ |
| **B. API Integration, Security & Performance** | [B1 — Backend API Integration](B1%20-%20Backend%20API%20Integration.md) | REST, JSON/XML, third-party SDKs | Medium |
| | [B2 — Mobile Security and Identity](B2%20-%20Mobile%20Security%20and%20Identity.md) | OAuth2, JWT, Keycloak SSO, biometrics, encryption | Large ⭐ |
| | [B3 — Performance Optimization](B3%20-%20Performance%20Optimization.md) | Memory, rendering speed, battery, Doze and App Standby | Medium |
| | [B4 — Push Notifications and Crash Monitoring](B4%20-%20Push%20Notifications%20and%20Crash%20Monitoring.md) | FCM, APNs, Crashlytics, Sentry | Medium |
| **C. App Store Deployment & DevOps** | [C1 — Store Publishing and Code Signing](C1%20-%20Store%20Publishing%20and%20Code%20Signing.md) | Play Store, App Store, versioning, signing, ASO | Medium |
| | [C2 — CI-CD and Build Automation](C2%20-%20CI-CD%20and%20Build%20Automation.md) | Fastlane, GitHub Actions, GitLab CI, Bitrise, cloud | Medium |
| **D. Testing, Maintenance & Collaboration** | [D1 — Architecture Patterns and Testing](D1%20-%20Architecture%20Patterns%20and%20Testing.md) | BLoC, MVVM, MVP, Clean Architecture, unit and widget tests | Large ⭐ |
| | [D2 — Post-Deployment Support](D2%20-%20Post-Deployment%20Support.md) | Crash logs, bug fixing, refactoring, backward compatibility | Small |
| | [D3 — Documentation and Agile Teamwork](D3%20-%20Documentation%20and%20Agile%20Teamwork.md) | Technical docs, Agile/Scrum, SDLC, collaboration | Medium |
| **E. Revision** | [E — Revision Sheet and Long-Answer Templates](E%20-%20Revision%20Sheet%20and%20Long-Answer%20Templates.md) | Everything on a few pages, all the diagrams, and 6 ready long answers | Read last |
| **F. Core maths** | [F — Probability](F%20-%20Probability.md) | Probability and counting: often asked in written exams for IT posts | Medium |

⭐ = the three chapters most likely to carry a long interview or exam question. Give them the most time.

**Foundations:** [OOP and DSA](../Notes/Foundations%201%20-%20OOP%20and%20DSA.md) and [Database and SQL](../Notes/Foundations%202%20-%20Database%20and%20SQL.md). Interviews and written exams often add a few core CS questions, so read these too. SDLC, testing and Git theory are inside D1, D3 and C2. Networking and security theory is inside B1 and B2.

## How each topic is taught

Every topic follows the same path, so you first **understand** it and then **memorise** it. Each step has its own colour.

<div class="box def">

**Definition.** One or two plain sentences: what the thing is and what it is for.

</div>

<div class="box story">

**Example scenario.** A small story from daily life or from a field app, in numbered steps, followed by "what happens?".

</div>

<div class="box q">

**A common question, written as a heading?**

The short answer comes first, then the reason. These are the points where people usually get confused.

</div>

<div class="box dev">

**What this means for a Flutter developer.** How the idea changes the code you write.

</div>

After these boxes comes the label **EXAM NOTES**. Under it are the compact tables, lists and code to learn for the exam, with the lines to memorise <mark>highlighted</mark>.

<div class="box rule">

**Remember.** One or two lines to carry into the exam hall.

</div>

<div class="box check">

**Quick check**

Two or three short questions, most of them multiple choice. Answer in your head, then open the answers.

<details>
<summary>Show answers</summary>

The answers are hidden like this until you click.

</details>

</div>

## How each chapter is built

1. **The skill**, in one quoted line, so you know what the chapter makes you able to do.
2. **Numbered sections**, each taught as shown above, with pictures.
3. **"Link it to your own projects"** in a green box: questions that connect the chapter to your own work.
4. **Practice questions**: short ones (2–3 marks) and long ones (8–12 marks).
5. **Model answers.** Each one is closed. Write your own answer first, then click the question to open the model answer.

**The model answers are written for learning**, so they are fuller than what you would write in the exam hall. Every answer has the same parts:

| Part | Colour | What it is |
|---|---|---|
| **In short** | Green box | The direct answer in one or two sentences. In the exam, write this part first |
| **Table or points** | — | The details: a table for every comparison, numbered steps for every flow, a picture where it helps, code where it is asked |
| **Example** | Yellow box | A real situation, usually from a field app or from your own projects |
| **In the exam** | Brown box, long answers only | How to shorten the answer on paper, and what to draw |
| **From the book** | Green buttons at the end | The sections the answer comes from. Click one and the page jumps to that lesson; the heading lights up for a moment |

**<mark>Highlights</mark>:** the lines to learn by heart are highlighted: full forms, one-line definitions, the key point in each "X vs Y" difference, numbers (16.67 ms, 48 dp, 15 minutes, USD 25/99) and rule-style sentences. For a quick revision, read only the **Remember** boxes and the highlights.

**Pictures:** the book has two kinds. The 73 drawn diagrams and charts in [images](images/) use only boxes, arrows and labels, so you can redraw them by hand in the exam. The 42 pictures in [images/web](images/web/) come from official documentation (Android, Flutter, Dart, Firebase, GitHub, MDN) and a few well-known sources. Each has its source written under it, and [images/web/SOURCES.md](images/web/SOURCES.md) lists them all.

## How to study a chapter (about 2–3 hours)

| Step | Time | What |
|---|---|---|
| 1 | 60–75 min | Read the chapter once, section by section. Do each quick check before you move on. Copy each drawn diagram by hand once. |
| 2 | 45–60 min | Close the file. Write answers to the practice questions **on paper**, timed (2 marks ≈ 3 minutes, 10 marks ≈ 15 minutes). |
| 3 | 20–30 min | Open the model answers and compare, or send me your answers and I will mark them. |
| 4 | 5 min | Put every miss in the [Mistakes Log](../Practice/Mistakes%20Log.md). |

## How to write an answer that scores

- **Definition first**, in one sentence. Then points. Then an example.
- **Use a table** for every "difference between X and Y" question. Three or four rows are enough.
- **Draw a small diagram** for every flow (login, sync, push notification, CI/CD pipeline). Boxes and arrows take one minute and show understanding.
- **Name real tools** (Drift, WorkManager, flutter_secure_storage, Keycloak). Named tools read as experience.
- **Tie one line to the scenario** in the question: who the users are, their network, their data.
- **Tie one line to your own work** where it fits: "In my app, I used...".
- Length guide: 2 marks = 3–4 lines. 5 marks = half a page. 10 marks = one to one and a half pages with a diagram.

## Using this book with Claude

This folder is a Claude Code project. Ask Claude to:
- **quiz you** on a chapter, then mark your answers and add your misses to the Mistakes Log;
- **write a mock paper** for a job you are applying for (paste the job advert or ToR);
- **explain a topic again** in the book's style, with a diagram;
- **add a new chapter** when you meet a topic the book does not cover.

<div class="book-nav"><span></span><span></span><span><a href="A1%20-%20Flutter,%20Dart%20and%20Native.md">A1 - Flutter, Dart and Native</a> →</span></div>
