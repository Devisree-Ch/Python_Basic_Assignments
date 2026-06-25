# Exercise 1: Class for a Book
# Create a Python class called Book with an __init__ method that takes title and author as arguments. 
# The class should have a method get_description() that returns a string like "[Title] by [Author]".
# class Book:
# 	def __init__(self,title,author):
# 		self.title=title
# 		self.author=author
# 	def get_description(self):
# 		# return self.title + " by " + self.author
# 		return f"{self.title} by {self.author}"
# b=Book("[Epic shit]","[Ankur Warikoo]")
# a=b.get_description()
# print(a)
# ====================================================================================================
# ====================================================================================================
# Exercise 2: List Comprehension Filter
# Given a list of numbers, use list comprehension to create a new list containing only the even numbers.
# COMPREHENSION QT[expression for item in iterable if condition]
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# a=[x for x in numbers if x%2==0]
# print(a)
# ====================================================================================================
# ====================================================================================================
# Exercise 3: Lambda Function Sort
# Given a list of tuples,
# students = [(\'Alice\', 25), (\'Bob\', 20), (\'Charlie\', 23)], 
# use a lambda function with sort() to sort the list by age (the second element of the tuple) in ascending order.
# students = [('Alice', 25), ('Bob', 20), ('Charlie', 23)]
# students.sort(key=lambda x:x[1])
# print(students)
# ====================================================================================================
# ====================================================================================================
# Exercise 4: Simple API Request (using requests library)
# Write a Python function called get_joke() that makes a GET request to 
# https://api.chucknorris.io/jokes/random and returns the 'value' of the joke from the JSON response.
# You will need to install the requests library (pip install requests).
# import requests
# def get_joke():
# 	response=requests.get("https://api.chucknorris.io/jokes/random")
# 	return response.json().get('value')
# print(get_joke())
# ====================================================================================================
# ====================================================================================================
# Exercise 4: Object-Oriented Design for a Library System
# Difficulty Level: Beginner-Intermediate
# Problem Statement: Design a basic object-oriented structure for a library management system. The system should be able to manage books and library members.
# Requirements:
# • Create a Book class with attributes like title, author, isbn, and is_available.
# • Create a Member class with attributes like member_id, name, and a list of borrowed_books.
# • Implement methods in the Book class to borrow() and return_book(), updating its availability status.
# • Implement methods in the Member class to borrow_book(book) and return_book(book), managing their borrowed_books list.
# ==========================================PENDINGGG==============================================
# ==========================================PENDINGGG=================================================

# Exercise 2: Simple Iterator for a Custom Range
# Difficulty Level: Beginner-Intermediate
# Problem Statement: Create a custom iterator that behaves like Python's built-in range() function but allows for floating-point step values.
# Requirements:
class FloatRange(start,stop,step=1.0):
	


# • Implement a class FloatRange that takes start, stop, and step (defaulting to 1.0) as arguments.
# • The class should be iterable, meaning it can be used in a for loop.
# • It should yield numbers starting from start, incrementing by step, until stop is reached (exclusive).
# • Handle cases where step is zero or negative appropriately.
# Expected Learning Outcomes:
# • Understanding of the iterator protocol (__iter__ and __next__).
# • Managing internal state for iteration.
# • Handling edge cases in custom iterators.
# ====================================================================================================
# ====================================================================================================
# Exercise 6: Context Manager for File Handling
# Difficulty Level: Beginner-Intermediate
# Problem Statement: Implement a custom context manager for safely handling file operations, ensuring the file is always closed, even if errors occur.
# Requirements:
# class ManagedFile():
# 	def __init__(self,filename,mode):
# 		self.filename=filename
# 		self.mode=mode
# 	def __enter__(self):
# 		self.filename=open(self.filename,self.mode)
# 		return self.filename
# 	def __exit__(self):
# 		self.filename.close()
# 		return False
# • Create a class ManagedFile that takes a filename and mode as arguments.
# • Implement the context manager protocol (__enter__ and __exit__).
# • The __enter__ method should open the file and return the file object.
# • The __exit__ method should ensure the file is closed, regardless of whether an exception occurred within the with block.
# Expected Learning Outcomes:
# • Understanding of the context manager protocol.
# • Ensuring resource cleanup in the presence of exceptions.
# • Practical application of with statements.