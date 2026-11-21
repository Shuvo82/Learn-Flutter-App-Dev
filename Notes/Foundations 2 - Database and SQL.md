# Foundations 2 — Database & SQL

PostgreSQL is a common backend database, and you use **SQLite/Drift** on mobile, so this topic is high-value for you. Read Part 1 (concepts), then Part 2 (SQL), then Part 3 (transactions and more), then do the **practice at the end** in writing.

---

# Part 1 — Database Concepts

## 1.1 Basic terms

<div class="box like">

**Like in daily life.**

| Daily life | In the app |
|---|---|
| An attendance register | A table |
| One student's line | A row (record, tuple) |
| The "Name" column | A column (attribute) |

</div>
- **Database**: an organized collection of related data.
- **DBMS** (Database Management System): software to create, store, query and manage databases (PostgreSQL, MySQL, Oracle, SQLite).
- **RDBMS**: a DBMS that stores data in **tables (relations)** of rows and columns, linked by keys.
- **Table / relation** = rows (**tuples/records**) + columns (**attributes/fields**).
- **Schema**: the structure (tables, columns, types, constraints). **Instance**: the data at a moment in time.

**Advantages of a DBMS over file systems:** less **redundancy**, **data integrity** (constraints), **security** (access control), **concurrent access**, **backup & recovery**, **data independence**.

## 1.2 Keys (very common question)

<div class="box like">

**Like in daily life.**

| Daily life | In the app |
|---|---|
| National ID number: one per person, never empty | Primary key |
| ID, passport number, phone: any could identify you | Candidate keys |
| Your NID written on a loan form to point to you | Foreign key |
| Roll number + class together (roll alone repeats across classes) | Composite key |

</div>
| Key | Meaning | Example (`students(student_id, nid, email, name, dept_id)`) |
|---|---|---|
| **Super key** | Any set of columns that **uniquely** identifies a row | `{student_id}`, `{student_id, name}`, `{nid}` |
| **Candidate key** | A **minimal** super key (nothing removable) | `student_id`, `nid`, `email` |
| **Primary key (PK)** | The candidate key **chosen**; **unique + NOT NULL**; one per table | `student_id` |
| **Alternate key** | Candidate keys **not** chosen as PK | `nid`, `email` |
| **Foreign key (FK)** | A column that **refers to the PK of another table**; enforces **referential integrity** | `dept_id → departments(dept_id)` |
| **Composite key** | A key made of **2+ columns** | `enrollments(student_id, course_id)` |
| **Surrogate key** | An artificial key with no business meaning | auto-increment `id`, **UUID** |

*Mobile link:* in an offline-first app you use **UUID** surrogate keys so device-created rows never clash with server rows.

## 1.3 ER Model (Entity–Relationship)

<div class="box like">

**Like in daily life.** Drawing who is who **before** building: members (entities), their details (attributes), and the links between them, like "a member takes many loans" (relationships, 1-to-many).

</div>
- **Entity**: a real-world object (Student, Member, Loan) → becomes a **table**.
- **Attribute**: a property of an entity → becomes a **column**. Types: simple, composite (address → road, city), **multivalued** (phones), **derived** (age from DOB), **key** attribute.
- **Relationship**: an association between entities (Student *enrolls in* Course).
- **Cardinality**: **1:1** (person–NID), **1:N** (department–employees), **M:N** (students–courses).
- **Weak entity**: can't be identified without its owner (Dependent of an Employee).

**ER-diagram symbols:** rectangle = entity, ellipse = attribute, diamond = relationship, double rectangle = weak entity, underlined = key.

**Mapping to tables:**
- **1:N** → put the **FK on the N side** (`employees.dept_id`).
- **M:N** → create a **junction (bridge) table** with both FKs: `enrollments(student_id, course_id)`.
- **1:1** → FK on either side (with UNIQUE).

## 1.4 Normalization (asked in almost every exam)

<div class="box like">

**Like in daily life.** A messy notebook where the branch address is written again on every member's line. Change the address and you must fix 500 lines, and you will miss some. Normalisation keeps **each fact in one place** and points to it.

</div>
**Goal:** reduce **redundancy** and remove **anomalies**:
- **Insertion anomaly**: you can't add data without other unrelated data (can't add a new course until a student enrolls).
- **Update anomaly**: the same data is stored in many rows, so updating it in one place leaves inconsistency.
- **Deletion anomaly**: deleting one row loses other useful data (deleting the last student loses the course info).

**Functional dependency (FD):** `A → B` means the value of A **determines** B (`student_id → name`).

| Normal form | Rule | Removes |
|---|---|---|
| **1NF** | Every cell is **atomic** (one value); no repeating groups; each row unique | Multi-valued cells |
| **2NF** | 1NF + **no partial dependency** (non-key columns depend on the **whole** composite key) | Partial dependency |
| **3NF** | 2NF + **no transitive dependency** (non-key → non-key) | Transitive dependency |
| **BCNF** | For every FD `X → Y`, **X must be a super key** (a stricter 3NF) | Remaining anomalies |

> Memory line: **"The key (1NF), the whole key (2NF), and nothing but the key (3NF)."**

### Worked example: normalize step by step
**Unnormalized:**
| order_id | customer | phone | products |
|---|---|---|---|
| 1 | Rahim | 017.. | Pen, Book |

**1NF**: split multi-valued `products` into rows:
| order_id | product_id | customer | phone | product_name | qty |

Key = `(order_id, product_id)`.

**2NF**: `product_name` depends only on `product_id` (**partial**), and `customer` only on `order_id` (**partial**). Split:
- `orders(order_id, customer, phone)`
- `products(product_id, product_name)`
- `order_items(order_id, product_id, qty)`

**3NF**: in `orders`, `phone` depends on `customer`, not on `order_id` (**transitive**). Split:
- `customers(customer_id, name, phone)`
- `orders(order_id, customer_id)`

**Denormalization:** adding redundancy **on purpose** for faster reads (reports, dashboards, data warehouses).

---

# Part 2 — SQL

## 2.1 SQL command categories

<div class="box like">

**Like in daily life.**

| Daily life | In the app |
|---|---|
| Building the cupboard and its drawers | DDL (`CREATE`, `ALTER`, `DROP`) |
| Putting things in, changing and taking them out | DML (`INSERT`, `UPDATE`, `DELETE`) |
| Giving or taking away the keys | DCL (`GRANT`, `REVOKE`) |
| "Save" or "undo" a set of changes | TCL (`COMMIT`, `ROLLBACK`) |

</div>
| Category | Full form | Commands |
|---|---|---|
| **DDL** | Data Definition Language | `CREATE`, `ALTER`, `DROP`, `TRUNCATE`, `RENAME` |
| **DML** | Data Manipulation Language | `INSERT`, `UPDATE`, `DELETE` (some include `SELECT`) |
| **DQL** | Data Query Language | `SELECT` |
| **DCL** | Data Control Language | `GRANT`, `REVOKE` |
| **TCL** | Transaction Control Language | `COMMIT`, `ROLLBACK`, `SAVEPOINT` |

## 2.2 DELETE vs TRUNCATE vs DROP

<div class="box like">

**Like in daily life.**

| Daily life | In the app |
|---|---|
| Tear out some pages, one by one, with a note of each | `DELETE` (can use `WHERE`, can roll back) |
| Rip out every page at once, keep the empty notebook | `TRUNCATE` |
| Throw away the whole notebook | `DROP` |

</div>
| | DELETE | TRUNCATE | DROP |
|---|---|---|---|
| Type | DML | DDL | DDL |
| Removes | Selected rows (`WHERE`) | **All rows** | **Whole table** (structure + data) |
| WHERE allowed | Yes | No | No |
| Rollback | Yes | Usually no (PostgreSQL: yes, inside a transaction) | Usually no |
| Speed | Slow (row by row, logged) | Fast | Fast |
| Triggers fire | Yes | No | No |

## 2.3 Creating tables with constraints

<div class="box like">

**Like in daily life.** Rules printed on a form: "this box must not be empty" (`NOT NULL`), "no two people may write the same NID" (`UNIQUE`), "age must be over 18" (`CHECK`).

</div>
```sql
CREATE TABLE departments (
  dept_id   SERIAL PRIMARY KEY,
  name      VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE employees (
  emp_id    SERIAL PRIMARY KEY,
  name      VARCHAR(100) NOT NULL,
  email     VARCHAR(150) UNIQUE,
  salary    NUMERIC(10,2) CHECK (salary > 0),
  join_date DATE DEFAULT CURRENT_DATE,
  dept_id   INT REFERENCES departments(dept_id) ON DELETE SET NULL
);
```
**Constraints:** `PRIMARY KEY`, `FOREIGN KEY` (`REFERENCES`), `UNIQUE`, `NOT NULL`, `CHECK`, `DEFAULT`.
**ON DELETE** options: `CASCADE` (delete children too), `SET NULL`, `RESTRICT` / `NO ACTION` (block the delete).

## 2.4 Basic queries
```sql
INSERT INTO employees (name, salary, dept_id) VALUES ('Rahim', 45000, 1);
UPDATE employees SET salary = salary * 1.10 WHERE dept_id = 1;
DELETE FROM employees WHERE emp_id = 5;

SELECT name, salary FROM employees
WHERE salary BETWEEN 30000 AND 60000
  AND name LIKE 'R%'            -- starts with R  (% = any chars, _ = one char)
  AND dept_id IN (1, 2)
  AND email IS NOT NULL         -- never "= NULL"
ORDER BY salary DESC
LIMIT 10 OFFSET 20;             -- pagination (page 3, 10 per page)

SELECT DISTINCT dept_id FROM employees;   -- unique values
```

## 2.5 Aggregates + GROUP BY + HAVING

<div class="box like">

**Like in daily life.** Sorting exam papers **into piles by class** (`GROUP BY`), then counting each pile (`COUNT`). `WHERE` throws away papers **before** making piles; `HAVING` throws away whole piles **after** counting.

</div>
Aggregate functions: `COUNT()`, `SUM()`, `AVG()`, `MIN()`, `MAX()`.
```sql
SELECT dept_id, COUNT(*) AS total, AVG(salary) AS avg_sal
FROM employees
WHERE salary > 0               -- filters ROWS before grouping
GROUP BY dept_id
HAVING COUNT(*) >= 5           -- filters GROUPS after grouping
ORDER BY avg_sal DESC;
```
**Logical execution order:** `FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT`
- **WHERE filters rows, HAVING filters groups.**
- Every column in `SELECT` must be either **in GROUP BY** or **inside an aggregate**.
- `COUNT(*)` counts all rows; `COUNT(col)` skips NULLs.

## 2.6 JOINs (draw the Venn diagrams in the exam)

<div class="box like">

**Like in daily life.**

| Daily life | In the app |
|---|---|
| Only the students who are in **both** the cricket and the football list | `INNER JOIN` |
| Every student in the class list, with their club if they have one | `LEFT JOIN` |
| Everyone from both lists | `FULL JOIN` |

</div>
```
employees: (1,Rahim,d1) (2,Karim,d2) (3,Salma,NULL)
departments: (d1,IT) (d2,HR) (d3,Finance)
```
| JOIN | Returns | Result here |
|---|---|---|
| **INNER JOIN** | Only **matching** rows in both | Rahim-IT, Karim-HR |
| **LEFT JOIN** | **All** left rows + matches (NULL if none) | Rahim-IT, Karim-HR, **Salma-NULL** |
| **RIGHT JOIN** | **All** right rows + matches | Rahim-IT, Karim-HR, **NULL-Finance** |
| **FULL OUTER JOIN** | All rows from **both** | all of the above (4 rows) |
| **CROSS JOIN** | **Cartesian product** (every combination) | 3 × 3 = 9 rows |
| **SELF JOIN** | A table joined **with itself** | employee → their manager |

```sql
-- Inner join
SELECT e.name, d.name AS dept
FROM employees e
INNER JOIN departments d ON e.dept_id = d.dept_id;

-- Departments with NO employees (LEFT JOIN + IS NULL pattern)
SELECT d.name FROM departments d
LEFT JOIN employees e ON e.dept_id = d.dept_id
WHERE e.emp_id IS NULL;

-- Self join: employee and manager
SELECT e.name AS employee, m.name AS manager
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.emp_id;
```

## 2.7 Subqueries

<div class="box like">

**Like in daily life.** A **question inside a question**: "who earns more than the average?" First you work out the average (the inner query), then you compare with it (the outer query).

</div>
```sql
-- Employees earning above the company average
SELECT name, salary FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

-- Employees in the 'IT' department (IN)
SELECT name FROM employees
WHERE dept_id IN (SELECT dept_id FROM departments WHERE name = 'IT');

-- Correlated subquery: earns above THEIR OWN department's average
SELECT e.name FROM employees e
WHERE e.salary > (SELECT AVG(x.salary) FROM employees x WHERE x.dept_id = e.dept_id);
```
- **Correlated subquery** = the inner query uses a column from the outer query and runs **once per outer row**.
- `EXISTS` returns true if the subquery returns any row (often faster than `IN` for big data).

## 2.8 The most-asked query: Nth highest salary
```sql
-- 2nd highest salary (method 1: subquery)
SELECT MAX(salary) FROM employees
WHERE salary < (SELECT MAX(salary) FROM employees);

-- Nth highest (method 2: LIMIT/OFFSET) — N=3
SELECT DISTINCT salary FROM employees
ORDER BY salary DESC
LIMIT 1 OFFSET 2;              -- OFFSET = N-1

-- Method 3: window function (handles ties)
SELECT name, salary FROM (
  SELECT name, salary, DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
  FROM employees
) t WHERE rnk = 2;
```

## 2.9 Window functions (basics)

<div class="box like">

**Like in daily life.** A **class rank** written next to each student's mark: every row stays, and each one gets an extra number computed from the rows around it. `GROUP BY` would squash the rows; a window function keeps them.

</div>
Calculate across rows **without collapsing** them (unlike GROUP BY).
```sql
SELECT name, dept_id, salary,
       RANK()       OVER (PARTITION BY dept_id ORDER BY salary DESC) AS rank_in_dept,
       SUM(salary)  OVER (PARTITION BY dept_id) AS dept_total
FROM employees;
```
`ROW_NUMBER()` = 1,2,3,4 · `RANK()` = 1,2,2,4 (gaps) · `DENSE_RANK()` = 1,2,2,3 (no gaps).

## 2.10 Other common queries
```sql
-- Find duplicate emails
SELECT email, COUNT(*) FROM employees
GROUP BY email HAVING COUNT(*) > 1;

-- UNION (removes duplicates) vs UNION ALL (keeps duplicates, faster)
SELECT name FROM employees UNION SELECT name FROM contractors;

-- CASE (if-else in SQL)
SELECT name, CASE WHEN salary >= 80000 THEN 'High'
                  WHEN salary >= 40000 THEN 'Medium'
                  ELSE 'Low' END AS band
FROM employees;
```

---

# Part 3 — Transactions, Indexes, Views & More

## 3.1 Transactions & ACID

<div class="box like">

**Like in daily life.** Sending money with mobile money: the amount leaves your account **and** reaches the shop, or neither happens. Never half. That all-or-nothing is a transaction.

| Daily life | In the app |
|---|---|
| All or nothing | Atomicity |
| The total money in the system is still correct | Consistency |
| Two payments at once do not mix | Isolation |
| Once "sent" is shown, a power cut does not undo it | Durability |

</div>
A **transaction** is a group of operations executed as **one logical unit**.
```sql
BEGIN;
UPDATE accounts SET balance = balance - 500 WHERE id = 1;
UPDATE accounts SET balance = balance + 500 WHERE id = 2;
COMMIT;            -- or ROLLBACK; if anything failed
```
- **A**tomicity: all or nothing (rollback on failure)
- **C**onsistency: valid state to valid state (constraints hold)
- **I**solation: concurrent transactions don't interfere
- **D**urability: committed data survives crashes (written to the WAL/log)

**Transaction states:** Active → Partially committed → Committed / Failed → Aborted.

## 3.2 Concurrency problems & isolation levels

<div class="box like">

**Like in daily life.** Two clerks working on the same passbook at the same moment. A **dirty read** is reading a line the other clerk has not finished writing yet; a **phantom read** is new lines appearing between two of your counts. Isolation levels decide how strictly the clerks must wait for each other.

</div>
| Problem | What happens |
|---|---|
| **Dirty read** | Reading data **not yet committed** by another transaction (it may roll back) |
| **Non-repeatable read** | Reading the same row twice gives **different values** (someone updated it in between) |
| **Phantom read** | Re-running a query returns **new/missing rows** (someone inserted/deleted) |
| **Lost update** | Two transactions update the same row; one overwrites the other |

| Isolation level | Dirty | Non-repeatable | Phantom |
|---|---|---|---|
| Read Uncommitted | possible | possible | possible |
| **Read Committed** (PostgreSQL default) | ✗ | possible | possible |
| Repeatable Read | ✗ | ✗ | possible* |
| **Serializable** (strictest) | ✗ | ✗ | ✗ |

\*PostgreSQL's Repeatable Read also prevents phantoms.
Higher isolation means **more correct but slower** (more locking).

**Locks:** **shared (read)** lock = many readers; **exclusive (write)** lock = one writer. **Deadlock** = two transactions each wait for a lock the other holds; the DB detects it and aborts one.

## 3.3 Indexes

<div class="box like">

**Like in daily life.** The **index at the back of a book**: instead of reading every page (a full scan), you look up the word and go to the page. But every new page means updating the index, so writes get a little slower.

</div>
An **index** is a data structure (usually a **B-tree** / B+ tree) that speeds up **searching**, like a book's index.
```sql
CREATE INDEX idx_emp_dept ON employees(dept_id);
CREATE UNIQUE INDEX idx_emp_email ON employees(email);
```
- ✅ Faster `SELECT`, `WHERE`, `JOIN`, `ORDER BY`
- ❌ Slower `INSERT/UPDATE/DELETE` (the index must be updated too) + extra storage
- **Clustered index**: sorts the **physical rows** (one per table; often the PK). **Non-clustered**: a separate structure with pointers (many allowed).
- Index columns that are **searched/joined often** and have **high selectivity**; don't index tiny tables or columns that are rarely filtered.
- `EXPLAIN ANALYZE <query>` (PostgreSQL) shows whether an index was used.

## 3.4 Views, stored procedures, triggers

<div class="box like">

**Like in daily life.**

| Daily life | In the app |
|---|---|
| A saved filter on a spreadsheet: a stored question, not new data | View |
| A recipe the kitchen keeps and runs on request | Stored procedure |
| A motion-sensor light: switches on by itself when something happens | Trigger |

</div>
- **View**: a **virtual table** from a saved SELECT. Uses: simplify complex queries, **security** (show only some columns).
  `CREATE VIEW it_staff AS SELECT name, email FROM employees WHERE dept_id = 1;`
  **Materialized view** = stores the result physically; refresh it periodically (good for **dashboards**).
- **Stored procedure / function**: saved SQL code with logic, executed on the DB server (reusable, less network traffic).
- **Trigger**: code that runs **automatically** on `INSERT/UPDATE/DELETE` (e.g. write an **audit log** row whenever a loan is updated).

## 3.5 SQL vs NoSQL

<div class="box like">

**Like in daily life.**

| Daily life | In the app |
|---|---|
| A filing cabinet with fixed forms and cross-references | SQL: fixed tables, relations, JOINs |
| A box of folders where each folder can hold different papers | NoSQL: flexible documents, key-value |

</div>
| SQL (Relational) | NoSQL |
|---|---|
| Tables with a **fixed schema** | Flexible / schema-less |
| **ACID** transactions | Often **BASE** (eventual consistency) |
| Scale **vertically** (bigger server) | Scale **horizontally** (more servers) |
| Complex JOINs, strong consistency | Fast, simple key-based access, big data |
| PostgreSQL, MySQL, Oracle, SQLite | MongoDB (document), Redis (key-value), Cassandra (column), Neo4j (graph), **Firebase Firestore** |
| Use: banking, **loans, accounts** | Use: caching, chat, logs, real-time feeds |

**CAP theorem:** a distributed system can guarantee only **2 of 3**: **C**onsistency, **A**vailability, **P**artition tolerance.

## 3.6 PostgreSQL quick facts 
- Open-source, **object-relational**, fully **ACID**, uses **MVCC** (Multi-Version Concurrency Control: readers don't block writers).
- Rich types: `JSONB`, arrays, `UUID`, **PostGIS** for GIS data.
- `SERIAL` / `IDENTITY` for auto-increment; default isolation **Read Committed**.

## 3.7 Mobile DB link (your strength, so use it in answers)
- **SQLite**: a serverless, file-based relational DB embedded in the app; supports SQL and transactions.
- **Drift**: a type-safe SQLite wrapper for Flutter (reactive streams, **migrations** via `schemaVersion`).
- **Isar / Hive**: NoSQL local stores for Flutter.
- **Migration** = changing the schema between app versions without losing user data.
- Wrap multi-row writes in a **transaction** (`db.transaction(() async {...})`): faster, and atomic.

---

# Practice — Foundations 2 (answer in writing, closed-book)

**Section A: short (2 marks each)**
1. Define primary key, foreign key, candidate key and composite key, with one example each.
2. What are insertion, update and deletion anomalies? Give one example.
3. Define 1NF, 2NF and 3NF. What is a transitive dependency?
4. DELETE vs TRUNCATE vs DROP (3 differences).
5. WHERE vs HAVING.
6. What is an index? Give one advantage and one disadvantage.
7. SQL vs NoSQL (3 differences + one example DB each).
8. Explain dirty read and phantom read.

**Section B: normalization (6 marks)**

9. Normalize this table up to **3NF**. Show each step and the final tables with keys:
   `loan(loan_id, member_nid, member_name, member_phone, branch_id, branch_name, branch_district, amount, issue_date)`
   (A member can have many loans; each loan belongs to one branch.)

**Section C: SQL (3 marks each)**

Tables: `branches(branch_id, name, district)`, `members(member_id, name, branch_id)`, `loans(loan_id, member_id, amount, issue_date, status)`

10. Show each branch's name and its **total loan amount**, highest first.
11. Find members who **have no loans**.
12. Find the **second highest** loan amount.
13. Show districts where the **number of branches is more than 3**.
14. Write the `CREATE TABLE` for `loans` with a PK, an FK to members, `amount > 0` and a `status` default of `'pending'`.

**Section D: ER (4 marks)**

15. Draw an ER diagram (text is fine) for: an **NGO** has many **Branches**; a **Branch** has many **Members**; **Members** take many **Loans**; a **Field Officer** visits many **Branches** and a branch is visited by many officers. Show cardinalities and say how you'd map the M:N relationship to tables.
