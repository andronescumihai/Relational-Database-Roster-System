import sqlite3

conn = sqlite3.connect('rosterdb.sqlite')
cur = conn.cursor()

cur.execute('''
SELECT 'XYZZY' || hex(User.name || Course.title || Member.role ) AS X 
FROM User JOIN Member JOIN Course 
ON User.id = Member.user_id AND Member.course_id = Course.id 
ORDER BY X LIMIT 1;
''')

row = cur.fetchone()
print(row[0])