# 🎓 Relational Academic Roster System

### 🏛️ Database Modeling & SQL Analytics
**Developed by Mihai-Alexandru Andronescu**

---

## 🚀 Overview
This project implements a relational database system designed to manage students, courses, and memberships. It focuses on the efficient representation of Many-to-Many relationships and demonstrates automated data ETL (Extract, Transform, Load) from JSON sources into a normalized SQLite architecture.

## ✨ Key Features
* **Relational Normalization:** Implements a 3-table structure (User, Course, Member) to eliminate data redundancy.
* **Many-to-Many Implementation:** Uses a junction table (Member) with composite keys to link users and courses effectively.
* **Automated Data Ingestion:** Python logic that parses JSON datasets and populates the relational schema while maintaining referential integrity.
* **Advanced SQL Querying:** Includes complex JOIN operations and analytical queries to extract specific insights from the roster.

## 🛠 Tech Stack
* **Language:** Python 3.x
* **Database:** SQLite (Relational SQL).
* **Data Format:** JSON.

## 📂 Project Structure
* `roster.py`: The main script that builds the schema and imports the JSON data.
* `roster_data.json`: The source dataset containing student and course assignments.
* `query1.py`: Demonstrates many-to-many JOIN queries for data retrieval.
* `final_code.py`: Advanced SQL logic for specialized data verification.
* `rosterdb.sqlite`: The persistent relational database file.

---
*Specialized in designing scalable data structures for Cloud and AI integration.*
