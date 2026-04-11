import sqlite3

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

cur.execute('''
SELECT User.name, Course.title, Member.role 
FROM User JOIN Member JOIN Course 
ON User.id = Member.user_id AND Member.course_id = Course.id 
ORDER BY User.name DESC, Course.title DESC, Member.role DESC 
LIMIT 2;
''')

rows = cur.fetchall()
for row in rows:
    print(row)