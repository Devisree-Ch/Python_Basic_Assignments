# Write a program to open a text file and print its contents line by line.
# file=open("Demotxt.txt",'r')
# content=file.read()
# print(content)
# Create a script that writes “Hello, World!” into a new file.
# nfile=open("Runtime.txt","w")
# nfile.write("Hello, World!")
# nfile.close()
# nfile=open("Runtime.txt","r")
# content=nfile.read()
# print(content)
# Write code to count the number of lines in a text file.
# file=open("Demotxt.txt",'r')
# content=file.readlines()
# count=0
# for i in content:
# 	count=count+1
# print(count,"lines are present in the file")
# Make a program that copies the contents of one file into another.
# file=open("Demotxt.txt",'r')
# content=file.read()
# file2=open("Demo2.txt",'w')
# file2.write(content)
# file2.close()
# file3=open("Demo2.txt",'r')
# content2=file3.read()
# print(content2)
# Write a script that appends user input to an existing file.
# f=open("Demo2.txt",'a')
# app=input("Enter the content\n")
# f.write(app)
# f.close()
# f1=open("Demo2.txt",'r')
# opt=f1.read()
# print(opt)
# Create a program that reads a file and counts how many times the word “Python” appears.
# f=open("Demo2.txt",'r')
# count=0
# for i in f:
# 	count=count+i.count("python")
# print(count)

# Make a program that reads a file and prints only the first 10 characters.
# f=open("Demo2.txt",'r')
# for i in f:
# 	for j in i:
# 		count=count+1
# 		if count<11:
# 			print(j)
# ==========Simpler method====
# print(f.read(10))

# Write a script that deletes the contents of a file without deleting the file itself.
# f=open("Demo2.txt",'w')
# f.truncate()

# Create a program that reads a file and prints the longest line.
# f=open("Demotxt.txt",'r')
# a=f.readlines()
# longest_line=max(a,key=len)
# print(longest_line)
# count=0
# for i in a:
# 	if count<len(i):
# 		count=len(i)
# 		print("longest line-->",i)
# 	else:
# 		continue
# print("length of longest line-->",count)

# Write a Python program that reads a text file and prints the total number of characters (including spaces and newlines) in it.
# f=open("Demotxt.txt",'r')
# a=f.read()
# print(len(a))
# f.close()
# Write a Python program that reads a text file and prints only the lines that contain the word “Python”.
# with open("Demotxt.txt",'r') as f:
# 	a=f.readlines()
# 	for i in a:
# 		if "Python" in i:
# 			print(i)
# with open("Demotxt.txt",'r') as f:
# 	for i in f:
# 		if "Python" in i:
# 			print(i)
# Write a generator that yields even numbers up to n.
# def even_gen():
# 	n=20
# 	for i in range(1,n+1):
# 		if i%2==0:
# 			yield i
# gen=even_gen()
# for i in gen:
# 	print(i)
# Create a generator that yields characters of a string one by one.
# str1="HI i am a generator to yield characs of string 1 by 1"
# def str_gen(n):
# 	for i in n:
# 		yield i
# gen=str_gen(str1)
# for i in gen:
# 	print(i)
# def str_gen(s):
# 	yield from s
# for i in str_gen(str1):
# 	print(i)

# Write a generator that produces an infinite stream of random numbers between 1–100.
# import random
# def inf_gen():
# 	while False:
# 		for i in range(1,101):
# 			yield random.randint(1,100)
# for i in inf_gen():
# 	print(i)

# Use a generator to flatten a nested list ([[1,2],[3,4]] → 1,2,3,4).
# n_list=[[1,2],[3,4]]
# def flatgen(nested_list):
# 	for i in nested_list:
# 		for j in i:
# 			yield j
# gen=flatgen(n_list)
# for i in gen:
# 	print(i)
# ===========Shorter version==============
# def flatgen(nested_list):
# 	for i in nested_list:
# 		yield from i
# gen=flatgen(n_list)
# for i in gen:
# 	print(i)
# Write a decorator that prints the arguments and return value of a function.
# def decorator(add):
# 	def wrapper(*args):
# 		print("arguments are -->",*args)
# 		a=add(*args)
# 		print("value of the function-->",a)
# 		return a
# 	return wrapper
# @decorator
# def add(a,b):
# 	sum=a+b
# 	return sum
# x=add(60,70)
# print(x)
# # Create a decorator that restricts a function to run only once.
# def once_dec(only_once):
# 	called=False
# 	def wrapper():
# 		nonlocal called
# 		if not called:
# 			called=True
# 			a=only_once()
# 			return a
# 		else:
# 			print("Function already called")
# 	return wrapper
# @once_dec
# def only_once():
# 	return "hey once"
# print(only_once())
# print(only_once())
# Build a decorator that validates if all arguments passed to a function are integers.
# def decor(add):
# 	def int_check(*args):
# 		for i in args:
# 			if type(i)!=int:
# 				return "All arguments should be integers"
# 		return add(*args)
# 	return int_check

# @decor
# def add(a,b):
# 	sum=a+b
# 	return sum
# print(add(1,2))
# print(add(2,'v'))
# Write a decorator that converts the output of a function to uppercase.
# def uppercase(str1):
# 	def convert(*args):
# 		a=str1(*args)
# 		return a.upper()
# 	return convert
# @uppercase
# def str1(input):
# 	return input
# print(str1("elephant"))
# Implement a decorator that retries a function up to 3 times if it raises an exception.
# def decor(zero_exept):
# 	def wrapper():
# 		for i in range(3):
# 			try:
# 				a=zero_exept()
# 				return a
# 			except ZeroDivisionError:
# 				print("Zerodivisionerror")
# 				return "3 exceptions exceeded"
# 	return wrapper
# @decor
# def zero_exept():
# 	a=10/0
# 	return a
# print(zero_exept())

# Write a function that removes duplicates from a list while preserving order.
# l1=[2,2,2,33,44,33,6,7,7,9]
# l2=[]
# def dupli(l1,l2):
# 	for i in l1:
# 		if i not in l2:
# 			l2.append(i)
# 		else:
# 			continue
# 	return l2
# print(dupli(l1,l2))

# Write a function to check if a given list is a palindrome.
# l1=[1,2,3,3,2,1]
# def palindrome(l1):
# 	l2=[]
# 	length=len(l1)
# 	index=round(length/2)
# 	l2=l1[index:length]
# 	l1=l1[0:index]
# 	if l2==l1[::-1]:
# 		return "Yes, palindrome"
# 	else:
# 		return "Not palindrome"
# print(palindrome(l1))

# Implement a function to merge two sorted lists without using built-in functions.
# l1=[1,2,3,4,5]
# l2=[6,7,8,9,10]
# def merge_list(l1,l2):
# 	for i in l2:
# 		l1.append(i)
# 	return l1
# print(merge_list(l1,l2))
# Write code to demonstrate shallow vs deep copy in Python.

# Implement a context manager that times how long a block of code takes.




# Write code to check if a file exists before opening it.
# Implement a generator that yields prime numbers below n.
