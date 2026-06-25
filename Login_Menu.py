# Add Menu System 
# 1. Register
# 2. Login
# 3. Show Users
# 4. Show Logs
# 5. Reset Password
# 6. Exit
import sqlite3
import hashlib
conn=sqlite3.connect("Login.db")
cur=conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS Login(
    username TEXT PRIMARY KEY,
    password TEXT NOT NULL,
    mailid TEXT UNIQUE NOT NULL,
    role TEXT NOT NULL
    )
""")

conn.commit()
def menu():
    while True:
        print("Welcome to the website")
        print("Here's the menu")
        print("1.Register\n2.Login\n3.Show Users\n4.Show Logs\n5.Reset Paassword\n6.Admins\n7.Delete user\n8.Exit")
        Choice=int(input("Enter your choice of menu"))
        if Choice==1:
            Register()
        elif Choice==2:
            Login()
        elif Choice==3:
            Show_Users()
        elif Choice==4:
            Show_Logs()
        elif Choice==5:
            Reset_Password()
        elif Choice==6:
            Admins()
        elif Choice==7:
            Delete_user()
        elif Choice==8:
            print("Thankyou for choosing this website")
            break
        else:
            print("please enter valid choice from 1-6")
def Register():
    for i in range(1,2):
        # Insert Multiple Users
#          Use a loop to insert at least 20 users automatically
        while i!=2:
            username=input("Enter username")
            password=(input("Enter password"))
            mailid=input("Enter email id")
            role=input("enter your role")
            cur.execute("""INSERT INTO Login (username,password,mailid,role) VALUES (?,?,?,?)""",(username,password,mailid,role))
            conn.commit()
def Login():
    name=input("Enter the username")
    pasw=input("Enter the password")
    cur.execute("SELECT * FROM Login WHERE username=? AND password=?",(name,pasw))
    loggin=cur.fetchone()
    print(loggin)
    if loggin:
        print("Login succesful")
    else:
        print("Invalid username or password")

def Show_Users():
    cur.execute("SELECT * FROM Login")
    users=cur.fetchall()
    print(users)
    if not users:
        print("No users found")
# Search User Feature
#Take username input
#Display user details if found 
    # name1=input("Enter the username")
    # cur.execute("SELECT * FROM Login WHERE username=?",(name1,))
    # users=cur.fetchall()
    # print(users)
    # if not users:
    #     print("No users found try with different username")
# Count Total Users
    # cur.execute('SELECT COUNT(*) FROM Login')
    # total=cur.fetchall()
    # print('total users found are',total)
def Show_Logs():
    pass
def Reset_Password():
    nameuser=input("Enter the username")
    wordpass=input("Enter the password")
    cur.execute("SELECT * FROM Login WHERE username=? AND password=?",(nameuser,wordpass))
    Reset_Password=cur.fetchall()
    print(Reset_Password)
    if Reset_Password:
        wp=input("Enter new password")
        cur.execute("UPDATE Login SET password=? WHERE username=?",(wp,nameuser))
        conn.commit()
        print("Password updated successfully")
    else:
        print("User not found")

# Filter Admin Users
def Admins():
    adminrole="Admin"
    cur.execute("SELECT username,role FROM Login WHERE role=?",(adminrole,))
    admin=cur.fetchall()
    print(admin)
    if not admin:
        print("No Admin roles found")
def Delete_user():
    # Delete a user using username
    del_user=input("Enter the user to delete")
    cur.execute("DELETE FROM Login WHERE username=?",(del_user,))
    conn.commit()
    print("Delete successful")
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
menu()

# Add Email Validation
#          Use import re
#          Validate email before inserting into database
#          Invalid email should not be accepted 


 

