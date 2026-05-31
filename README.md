# 🎓 Relational Academic Roster System

> **Python for Everybody — University of Michigan** | SQLite, JSON ETL, Many-to-Many Relational Design

---

## 📌 Project Overview

A complete **relational database pipeline** that ingests a JSON course roster dataset (313 entries, 10 courses) and loads it into a normalized 3-table SQLite schema. The system models a **Many-to-Many relationship** between students and courses via a junction table, with role-based membership (0 = student, 1 = instructor). Includes multi-table JOIN queries and a cryptographic hash verification query for data integrity checking.

Built as part of the *Python for Everybody* specialization (University of Michigan / Coursera), specifically the *Using Databases with Python* course.

---

## ✨ Key Features

| Feature | Implementation |
|---|---|
| 🏗️ **3NF Schema Design** | `User`, `Course`, `Member` — normalized to eliminate redundancy |
| 🔗 **Many-to-Many Junction Table** | `Member(user_id, course_id, role)` with composite PRIMARY KEY |
| 📥 **JSON ETL Pipeline** | Parses `roster_data.json` (313 entries, 10 courses) → inserts with referential integrity |
| 🔄 **Idempotent Inserts** | `INSERT OR IGNORE` for User/Course, `INSERT OR REPLACE` for Member — safe re-runs |
| 🔍 **Multi-table JOIN Query** | `User JOIN Member JOIN Course` with `ORDER BY` and `LIMIT` |
| 🔐 **Hash Verification Query** | `hex(name \|\| title \|\| role)` with `XYZZY` prefix — course grading integrity check |

---

## 🗄️ Database Schema

```sql
CREATE TABLE User (
    id    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name  TEXT UNIQUE
);

CREATE TABLE Course (
    id    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT UNIQUE
);

CREATE TABLE Member (
    user_id    INTEGER,
    course_id  INTEGER,
    role       INTEGER,       -- 0 = student, 1 = instructor
    PRIMARY KEY (user_id, course_id)
);
```

---

## 🛠️ Tech Stack

- **Language:** Python 3.x
- **Database:** SQLite3 (standard library)
- **Data Format:** JSON (313 entries across 10 courses: si106, si110, si206, si301, si310, si334, si363, si364, si422, si430)
- **Course:** Python for Everybody — University of Michigan (Coursera)

---

## 📁 Repository Structure

```
├── roster.py           # ETL pipeline: JSON → schema creation → data ingestion
├── roster_data.json    # Source dataset: 313 [name, course, role] entries
├── query1.py           # Multi-table JOIN: User ↔ Member ↔ Course, ordered + limited
├── final_code.py       # Hash verification: hex(name || title || role) integrity check
└── rosterdb.sqlite     # Generated database: populated after running roster.py
```

---

## ⚙️ Pipeline Breakdown

**`roster.py` — ETL Script**
1. Drops and recreates `User`, `Course`, `Member` tables (idempotent)
2. Loads `roster_data.json` — format: `[name, course_title, role]`
3. For each entry: `INSERT OR IGNORE` into User → fetch `user_id` → `INSERT OR IGNORE` into Course → fetch `course_id` → `INSERT OR REPLACE` into Member with role
4. Commits transaction

**`query1.py` — Analytical Query**
```sql
SELECT User.name, Course.title, Member.role
FROM User JOIN Member JOIN Course
ON User.id = Member.user_id AND Member.course_id = Course.id
ORDER BY User.name DESC, Course.title DESC, Member.role DESC
LIMIT 2;
```

**`final_code.py` — Integrity Verification**
```sql
SELECT 'XYZZY' || hex(User.name || Course.title || Member.role) AS X
FROM User JOIN Member JOIN Course
ON User.id = Member.user_id AND Member.course_id = Course.id
ORDER BY X LIMIT 1;
```

---

## ▶️ How to Run

```bash
# Step 1: Build the database
python3 roster.py

# Step 2: Query the roster
python3 query1.py

# Step 3: Run integrity check
python3 final_code.py
```

---

## 🧠 What I Learned

- Designing **normalized relational schemas** (3NF) for Many-to-Many relationships
- Implementing **junction tables** with composite primary keys in SQLite
- Building **JSON-to-SQL ETL pipelines** with referential integrity via `INSERT OR IGNORE` + SELECT ID pattern
- Writing **multi-table JOIN queries** with filtering, ordering, and limiting
- Using **SQL string functions** (`hex()`, concatenation) for data verification workflows

---

## 📜 Context

Part of the **Python for Everybody** specialization by Dr. Charles Severance (University of Michigan), specifically the *Using Databases with Python* course. The exercise simulates real database engineering work: schema design, data ingestion from external sources, and analytical querying — patterns found in every production data system.

---

## 👤 Author

**Mihai-Alexandru Andronescu**
Student — Computer Science & Economics, ASE Bucharest

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://www.linkedin.com/in/mihai-alexandru-andronescu-58792b33b/)
[![GitHub](https://img.shields.io/badge/GitHub-Profile-black?logo=github)](https://github.com/andronescumihai)
