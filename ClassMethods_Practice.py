import math
# 1. Write a Python program to create a class and object.
# class P:
# 	def p1(self):
# 		print("hi")
# o=P()
# o.p1()
# 2. Create a class Student with attributes name and marks.
# 3. Write a program to create a class with a method to display student details.
# class Student:
# 	def __init__(self,name,marks):
# 		self.name=name
# 		self.marks=marks
# 	def display(self,name,marks):
# 		print(f'Hi {name}, your marks are {marks}')
# s=Student("sameera",54)
# s.display("sameera",54)
# # 4. Create a class Car and print car details using an object.
# class Car:
# 	def details(self,name,version,color):
# 		print(f'car details are name:{name}, version:{version}, color:{color}')
# c=Car()
# c.details("BMW",2.0,"Blue")
# 5. Write a program using the _init_() constructor.
# class Student:
# 	def __init__(self,name,age,standard,section):
# 		self.name=name
# 		self.age=age
# 		self.standard=standard
# 		self.section=section
# 	def Stu_PersonalDetails(self):
# 		print(f'StudentName:{self.name} Age:{self.age}')
# 	def Stu_CareerDetails(self):
# 		print(f'class:{self.standard},section:{self.section}')
# s=Student("Saranya",12,"5th","B")
# s.Stu_PersonalDetails()
# s.Stu_CareerDetails()

# 6. Create a class Employee with employee id and salary.
# class Employee:
# 	def Details(self,empID,salary):
# 		print(f'The employee id is {empID} and their salary is {salary}')
# e=Employee()
# e.Details("180100",50000)
# 7. Write a program to demonstrate instance variables.
# class InstV:
# 	def __init__(self,var1,var2):
# 		self.var1=var1
# 		self.var2=var2
# 		print(f'{var1} & {var2} are instancce variables')
# i=InstV("a","b")
# 8. Write a program to demonstrate class variables.
# class ClasV:
# 	a=12
# 	b="Nemisha"
# 	def view(self):
# 		print(f'{self.a} and {self.b} are Class variables')
# c=ClasV()
# c.view()
# 9. Create a class with multiple methods.
# class MulMethods:
# 	def m1(self):
# 		print("method1")
# 	def m2(self):
# 		print("method2")
# 	def m3(self):
# 		print("method3")
# m=MulMethods()
# m.m1()
# m.m2()
# m.m3()
# 10. Write a program for single inheritance.
# class Car:
# 	def P_Details(self,length,width,breadth):
# 		print(f'the length width and breadth of the car are {length} {width} {breadth} respectively')
# class Car2(Car):
# 	def I_Details(self,feature,transmission):
# 		print(f'the features present are {feature} and transmission is {transmission}')
# c1=Car2()
# c1.I_Details("LCD-Display","Automatic")
# c1.P_Details("15","20","10")
# 11. Write a program for multilevel inheritance.
# class Dog:
# 	def origin(self,country):
# 		print(f"This dog belongs to {country}")
# class Dog2(Dog):
# 	def color(self,color):
# 		print(f'This dogs color is {color}')
# class Dog3(Dog2):
# 	def noise(self,bark_capacity):
# 		print(f'This dogs barking capacity is {bark_capacity}')
# d=Dog3()
# d.origin("USA")
# d.color("Gray")
# d.noise("HIGH")
# 12. Write a Python program for multiple inheritance.
# class Bikes:
# 	def types(self,t1,t2):
# 		print(f'The diff types of bikes are {t1} and {t2}')
# class Cars:
# 	def typeC(self,t3,t4):
# 		print(f'the diff types of cars are {t3} and {t4}')
# class Vehicles(Bikes,Cars):
# 	print(f'These are the vehicles i know')
# v=Vehicles()
# v.types("Pulsar","Bullet")
# v.typeC("BMW","Benz")
# =================================================================================
# 13. Create a program to demonstrate method overriding.
# class parent:
# 	def s1(self):
# 		print("Parent Method")
# class Child(parent):
# 	def s1(self):
# 		print("Child Method")
# P=parent()
# P.s1()
# C=Child()
# C.s1()
# 20. Write a real-time OOP program for a Bank Account system with deposit and withdrawal methods.
# class Account:
# 	def __init__(self,A_no,Balance,withdrawAmount=0):
# 		self.A_no=A_no
# 		self.withdrawAmount=withdrawAmount
# 		self.Balance=Balance
# 	def deposited(self,deposit):
# 		if self.A_no:
# 			self.Balance=self.Balance+deposit
# 			print(f'amount deposited is {deposit} the current balance is {self.Balance}')
# 		else:
# 			print("please create an account before depositing")
# 	def withdrawal(self):
# 		if self.A_no:
# 			if self.Balance>=self.withdrawAmount:
# 				self.Balance=self.Balance-self.withdrawAmount
# 				print(f'the amount withdrawn is {self.withdrawAmount} current balance is {self.Balance}')
# 			else:
# 				print(f'Please recheck\nCurrent balance is {self.Balance}\nwithdrawal amount is {self.withdrawAmount}')
# 		else:
# 			print("Account is not existing")
# A1=Account(1223,100,20)
# A1.withdrawal()
# A1.deposited(100)
# 21. Create a class Laptop with brand and price attributes.
# class Laptop:
# 	def __init__(self,brand,price):
# 		self.brand=brand
# 		self.price=price
# 	def Attri(self):
# 		print(f'The laptop brand is {self.brand} and price is {self.price}')
# # 	def Attri(self,brand,price):
# # 		print(f'The laptop brand is {brand} and price is {price}')
# L1=Laptop('Lenovo',65000)
# L2=Laptop('Asus',100000)
# L1.Attri()
# L2.Attri()
# 22. Write a program to calculate the area of a rectangle using a class.
# class Area:
# 	def RectArea(self,width,length):
# 		Area=width*length
# 		print(f"Area of rectangle is {Area}")
# A=Area()
# A.RectArea(3,5)
# 23. Create a class Mobile with methods to make calls and send messages.
# class Mobile:
# 	def __init__(self,number,message_content=None):
# 		self.number=number
# 		self.message_content=message_content
# 	def calls(self):
# 		print(f'calling {self.number}')
# 	def messages(self):
# 		if self.message_content:
# 			print(f'message-->> {self.message_content}')
# 			print(f'sending message to {self.number}')
# 		else:
# 			pass
# # m=Mobile(8000870654,"Hi, How are you")
# # m.calls()
# # m.messages()
# m1=Mobile(1234567890)
# m1.calls()
# m1.messages()
# 24. Write a Python program to create two objects of the same class.
# class TwoObject:
# 	def m1(self):
# 		print("hi")
# 	def m2(self):
# 		print("hi 2")
# O=TwoObject()
# O.m1()
# O1=TwoObject()
# O1.m2()
# 25. Create a class Book and display book details.
# class Book:
# 	def __init__(self,title,author):
# 		self.title=title
# 		self.author=author
# 	def bookdetails(self):
# 		print(f'Title : {self.title}\nAuthor : {self.author}')
# b=Book("Gulliver Travels","Gulliver")
# b.bookdetails()
# 27. Create a class Circle with a method to calculate area.
# class Circle:
# 	def __init__(self,radius):
# 		self.radius=radius
# 	def areaC(self):
# 		Area=math.pi*(self.radius**2)
# 		print(f'area of circle is {Area}')
# c=Circle(20)
# c.areaC()
# 29. Create a class Animal and inherit it into Dog.
# class animal:
# 	def __init__(self,species,food):
# 		self.species=species
# 		self.food=food
# 		print(f'the animal is {self.species} and eats {self.food}')
# class Dog(animal):
# 	def dog1(self):
# 		print("It barks")
# d=Dog("Dog","bones")
# d.dog1()
# 30. Write a program to demonstrate hierarchical inheritance.
# class C1:
# 	def m1(self):
# 		print("parent")
# class C2(C1):
# 	def m2(self):
# 		print("child")
# class C3(C1):
# 	def m3(self):
# 		print("Grand children")
# obj1=C3()
# obj2=C2()
# obj1.m3()
# obj2.m2()
# obj1.m1()
# 31. Create a parent class Person and child class Teacher.
# class Person:
# 	def m1(self):
# 		print("Hi I am the student")
# class Teacher(Person):
# 	def m2(self):
# 		print("Hi I am the teacher")
# t=Teacher()
# t.m2()
# t.m1()
# 33. Create a class Vehicle and override its method in Bike.
# class Vehicle:
# 	def veh(self):
# 		print("hi, i am vehicle")
# class Bike(Vehicle):
# 	def veh(self):
# 		print("hi i am two wheeler")
# b=Bike()
# b.veh()
# v=Vehicle()
# v.veh()
# 32. Write a program to access parent class methods from child class.
# class Parent:
# 	def m1(self):
# 		print("method1")
# 	def m2(self):
# 		print("method2")
# class Child(Parent):
# 	def c1(self):
# 		self.m1()
# 		self.m2()
# c=Child()
# c.c1()
# 41. Create a class Bank with account holder name and balance.
# class Bank:
# 	def __init__(self,name,balance):
# 		self.name=name
# 		self.balance=balance
# 		print(f'Account Holder name : {name}\nBalance : {balance}')
# c=Bank("Devisree",10000)
# 39. Create a class ATM with balance check, deposit, and withdraw methods.
# class ATM:
# 	def __init__(self,A_no,balance=0):
# 		self.A_no=A_no
# 		self.balance=balance
# 	def choice(self):
# 		if self.A_no:
# 			while True:
# 				print("1.Check balance\n2.Account Deposit\n3.Withdrawal\n4.Exit")
# 				Ch1=int(input("Enter the choice"))
# 				if Ch1==1:
# 					self.balance_check()
# 				elif Ch1==2:
# 					self.deposit_account(deposit=0)
# 				elif Ch1==3:
# 					self.withdraw_Account()
# 				elif Ch1==4:
# 					print("Thankyou for choosing ATM")
# 					break
# 				else:
# 					print("Choose only from the options provided")
# 		else:
# 			print("invalid account")
# 	def deposit_account(self,deposit):
# 		Dep1=int(input('Enter the deposit amount'))
# 		self.balance+=Dep1
# 		print(f'Amount deposited {Dep1}')
# 	def balance_check(self):
# 		print(f'Available balance is {self.balance}')
# 	def withdraw_Account(self):
# 		wd=int(input("enter the amount to be withdrawn"))
# 		if wd<=self.balance:
# 			print("Withdrawal successful")
# 			self.balance=self.balance-wd
# 			print("available balance is",{self.balance})
# 		else:
# 			print("Insufficient balance, current balance is ", {self.balance})
# a=ATM(1234)
# a.choice()
# 42. Write a class Calculator with add, subtract, multiply, and divide methods.
# class Calculator:
# 	def __init__(self,a,b):
# 		self.a=a
# 		self.b=b
# 	def add(self):
# 		result=self.a+self.b
# 		print("addition of two",{result})
# 	def subt(self):
# 		result=self.a-self.b
# 		print("subtraction of two",{result})
# 	def multi(self):
# 		result=self.a*self.b
# 		print("multiplication of two",{result})
# 	def div(self):
# 		result=self.a/self.b
# 		print("division of two",{result})
# c=Calculator(5,5)
# c.add()
# c.multi()
# c.subt()
# c.div()
# 43. Create a class StudentResult to calculate total and percentage.
# class StudentResult:
# 	def marks(self):
# 		m1=int(input("Enter the maths marks"))
# 		p=int(input("Enter the physics marks"))
# 		soc=int(input("enter social marks "))
# 		total=m1+p+soc
# 		print("Total marks are", total)
# 		percentage = total/300*100
# 		print("Percentage is ", percentage)
# sr=StudentResult()
# sr.marks()
# class StudentResult:
# 	def __init__(self,m1,p,soc):
# 		self.m1=m1
# 		self.p=p
# 		self.soc=soc
# 	def total(self):
# 		marks=self.m1+self.p+self.soc
# 		percentage=marks/300 * 100
# 		print("Total marks are ",marks)
# 		print("percentage is ",percentage)
# sr=StudentResult(90,90,99)
# sr.total()

# 26. Write a program to demonstrate constructor overloading using default arguments.

# 28. Write a program to count the number of objects created for a class.

# 34. Write a program using method overriding with super().

# 35. Create a class with getter and setter methods.

# 36. Write a program using private methods in Python.

# 37. Create a program for runtime polymorphism.

# 38. Write a Python program using abstract base classes.

# 40. Write a mini project using OOP for Library Management System.

# 44. Write a program for employee salary calculation using inheritance.

# 45. Create a shopping cart program using classes and objects.

# 46. Write a Python program to store and display customer details.

# 47. Create a class Movie with movie name, rating, and release year.

# 48. Write a program to demonstrate encapsulation in a student management system.

# 49. Create a railway ticket booking system using OOP concepts.

# 50. Write a food ordering system program using classes and objects.

# 51. Create a banking system using OOP with deposit, withdraw, and transaction history features.

# 52. Build a Library Management System using classes for books, users, and transactions.

# 53. Create an Employee Management System using inheritance and polymorphism.

# 54. Design an Online Shopping Cart system using multiple classes.

# 55. Implement a Student Management System with file handling and OOP.

# 56. Create a Hotel Room Booking system using classes and objects.

# 57. Build a Railway Reservation System using OOP concepts.

# 58. Create an ATM simulation program with PIN verification and balance management.

# 59. Design a Vehicle Management System using abstraction and inheritance.

# 60. Build a Hospital Management System with doctor and patient classes.

# 61. Create a Python program to demonstrate operator overloading.

# 62. Implement method overloading using default arguments.

# 63. Create a custom exception class and use exception handling in OOP.

# 64. Design a payroll system using inheritance and encapsulation.

# 65. Create a class decorator example in Python.

# 66. Build a school management system using aggregation and composition.

# 67. Implement a singleton design pattern in Python.

# 68. Create a logger class using static methods and class methods.

# 69. Build an inventory management system using OOP.

# 70. Create a movie ticket booking application using classes.

# 71. Implement a real-time chat user model using OOP.

# 72. Design a food delivery application structure using abstraction.

# 73. Create a program using multilevel and multiple inheritance together.

# 74. Build a quiz application using classes and objects.

# 75. Create a Python class for handling database-like CRUD operations.

# 76. Design a cab booking system using OOP concepts.

# 77. Create a class-based authentication and login system.

# 78. Implement encapsulation in a real-time employee salary system.

# 79. Build a simple e-commerce product management system.

# 80. Create a Python project using all four OOP pillars:
# - Encapsulation
# - Inheritance
# - Polymorphism
# - Abstraction
# 14. Write a program to show polymorphism using different classes.

# 15. Create a class with private variables and access them using methods.

# 16. Write a program using protected members in Python.

# 17. Create an abstract class and implement its methods.

# 18. Write a program using super() function.

# 19. Create a class using @staticmethod.
