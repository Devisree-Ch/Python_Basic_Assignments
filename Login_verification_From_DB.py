import sqlite3
import hashlib
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    age INTEGER CHECK(age >= 18),
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
""")

conn.commit()

def encoding(password):
  return hashlib.sha256(password.encode()).hexdigest()


def register():
  username = input("Enter username: ")
  email = input("Enter email: ")
  password = input("Enter password: ")
  encodedpwd=encoding(password)
  age = int(input("Enter age: "))
  try:
    cursor.execute("""
    insert into Users (username,email,password,age)
    values(?,?,?,?)
    """,(username,email,encodedpwd,age))
    conn.commit()
    login()
  except:
    print("ERROR")
register()

def login():
  cursor.execute("SELECT * FROM Users")
  data=cursor.fetchall()
  print(data)
  cursor.execute("SELECT username,password FROM Users")
  data1=cursor.fetchall()
  print(data1)
  user = input("Enter username: ")
  pass1 = input("Enter password: ")
  # for i in data1:
  #   userfound=cursor.execute("SELECT username,password FROM Users where username=? and password=?",(user,pass1))
  #   if userfound:
  #     print("logged in")
  #   else:
  #     print("invalid")
  if user==data1[0][0] and pass1==data1[0][1]:
    print("login done",pass1)
  else:
    print("invalid creds")
login()

# [(1, 'sam', 'sam@gmail.com', 'sam123!', 25, '2026-04-21 15:24:38')]