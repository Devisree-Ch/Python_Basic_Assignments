# You have a table named students with the following columns:
# * id
# * student_name
# * marks
# Write an SQL query to display:
# * student id
# * marks
# * grade
# Conditions:
# * Marks between 90 and 100 → A+
# * Marks between 75 and 89 → A
# * Marks between 60 and 74 → B
# * Marks between 40 and 59 → C
# * Below 40 → Fail
# Note:
# The grade column is not available in the table. Generate it using SQL.

import sqlite3
conn=sqlite3.connect("Students.db")
cur=conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS Students(
	ID INTEGER PRIMARY KEY,
	NAME VARCHAR NOT NULL,
	MARKS INTEGER NOT NULL) """)
conn.commit()
# def grades():
# 	cur.execute("ALTER TABLE Students ADD GRADE TEXT")
# 	conn.commit()
# grades()
def upload():
	for i in range(1,7):
		s_id=input("Enter student id:")
		name=input("Enter the name of the student")
		marks=input("Enter the marks")
		cur.execute("INSERT INTO Students (ID,NAME,MARKS) VALUES (?,?,?)",(s_id,name,marks))
		conn.commit()
	print("Upload successful")
# upload()
# def map_grades():
# 	A_PLUS='A+'
# 	FAIL='Fail'
# 	cur.execute("UPDATE Students SET GRADE=? WHERE MARKS BETWEEN 90 AND 100",(A_PLUS,))
# 	conn.commit()
# 	cur.execute("UPDATE Students SET GRADE=? WHERE MARKS BETWEEN 75 AND 89",('A'))
# 	conn.commit()
# 	cur.execute("UPDATE Students SET GRADE=? WHERE MARKS BETWEEN 60 AND 74",('B'))
# 	conn.commit()
# 	cur.execute("UPDATE Students SET GRADE=? WHERE MARKS BETWEEN 40 AND 59",('C'))
# 	conn.commit()
# 	cur.execute("UPDATE Students SET GRADE=? WHERE MARKS<40",(FAIL,))
# 	conn.commit()
# map_grades()
def display():
	cur.execute("""SELECT ID,NAME,MARKS,
		CASE
			WHEN MARKS BETWEEN 90 AND 100 THEN 'A+'
			WHEN MARKS BETWEEN 75 AND 89 THEN 'A'
			WHEN MARKS BETWEEN 60 AND 74 THEN 'B'
			WHEN MARKS BETWEEN 40 AND 59 THEN 'C'
			ELSE 'FAIL'
		END AS GRADE
	 FROM Students""")
	details=cur.fetchall()
	print(details)
display()