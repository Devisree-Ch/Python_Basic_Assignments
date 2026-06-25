#Your task is to create Employee and Department tables by referring to the above example.

import sqlite3

class DepDB:
	def __init__(self):
		self.conn=sqlite3.connect("DepDB")
		self.cur=self.conn.cursor()
		print("DB Connected/Created")
	def close_conn(self):
		self.conn.close()
		print("DB Closed")
class Employee(DepDB):
	def create_Employee(self):
		self.cur.execute("""CREATE TABLE IF NOT EXISTS Employees(empid INTEGER PRIMARY KEY, empname TEXT)""")
		self.conn.commit()
		print("Table created")
	def insert_data_to_Employees(self,empid,empname):
		self.cur.execute("""INSERT INTO Employees (empid,empname) VALUES (?,?)""",(empid,empname))
		self.conn.commit()
	def view_Employees(self):
		a=self.cur.execute("""SELECT * FROM Employees""")
		for i in a:
			print(i)
class Department(Employee):
	def Create_Department(self):
		self.cur.execute("""CREATE TABLE IF NOT EXISTS Department(empid INTEGER PRIMARY KEY, Deptname TEXT, Deptid INTEGER)""")
		self.conn.commit()
		print("Dept Table Created")
	def insert_data_to_Department(self,empid,Deptname,Deptid):
		self.cur.execute("""INSERT INTO Department(empid,Deptname,Deptid) VALUES (?,?,?)""",(empid,Deptname,Deptid))
		self.conn.commit()
	def View_Department(self):	
		b=self.cur.execute("""SELECT * FROM Department""")	
		for j in b:
			print(j)
class DeptEmp(Department):
	def view(self):
		C=self.cur.execute("""SELECT * FROM Employees INNER JOIN Department ON Employees.empid=Department.empid""")
		for k in C:
			print(k)
s1=Employee()
# s1.view_Employees()
# s1.create_Employee()
# s1.insert_data_to_Employees(4,"Kranthi")
s2=Department()
# s2.View_Department()
# s2.Create_Department()
# s2.insert_data_to_Department(5,"IT",20)
s3=DeptEmp()
s3.view()
    