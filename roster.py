import json
import sqlite3

# Se conectează la baza de date (sau o creează)
conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

# Șterge tabelele dacă există deja
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Member;
''')

# Creează noile tabele
cur.executescript('''
CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

# Deschide fișierul JSON
fname = 'roster_data.json'
with open(fname) as f:
    data = json.load(f)

# Exemplu de format: [ [ "Charley", "si110", 1 ], ... ]
for entry in data:
    name = entry[0]
    title = entry[1]
    role = entry[2]

    cur.execute('INSERT OR IGNORE INTO User (name) VALUES ( ? )', (name,))
    cur.execute('SELECT id FROM User WHERE name = ? ', (name,))
    user_id = cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Course (title) VALUES ( ? )', (title,))
    cur.execute('SELECT id FROM Course WHERE title = ? ', (title,))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member (user_id, course_id, role)
        VALUES ( ?, ?, ? )''', (user_id, course_id, role))

conn.commit()