# 1. Write a generator function that yields numbers from 1 to 10.
def gen_name():
	for i in range(1,11):
		yield i
a=gen_name()
print("Yielding numbers 1 to 10")
for i in a:
	print(i, end=" ")
print("\n=======================================================")


# 2. Create a generator that yields even numbers from 1 to 20.
def gen_name2():
	for i in range(1,21):
		if i%2==0:
			yield i
a1=gen_name2()
print("Even numbers using yield")
print(next(a1),next(a1),next(a1),next(a1),next(a1),next(a1),next(a1),next(a1),next(a1),next(a1))
print("=========================================================")


# 3. Write a generator that yields squares of numbers from 1 to n.
n=5
def gen_name3():
	for i in range(1,n+1):
		yield i*i
a2=gen_name3()
print("squares of integers upto n")
print(next(a2),next(a2),next(a2),next(a2),next(a2))
print("===========================================================")



# 4. Create a generator that yields characters of a given string one by one.
strname="Python"
def charac_gen():
	for i in strname:
		yield i
b=charac_gen()
print("Yielding characters of a given string")
print(next(b),next(b),next(b),next(b),next(b),next(b))
print("=================================================")



# 5. Write a generator that yields numbers divisible by 3 between 1 and 50.
def divby3():
	for i in range(1,51):
		if i%3==0:
			yield i
c=divby3()
print("Divisible by 3 from 1 to 50")
for i in c:
	print(i,end=" ")
print("\n=================================================")



# 9. Create a generator that yields numbers from a list that are greater than 10.
l=[15,20,19,13,9,13,2]
def numbers_list():
	for i in l:
		if i > 10:
			yield i
f=numbers_list()
print("Greater than 10 from a list")
print(next(f),next(f),next(f),next(f),next(f))
print("=================================================")



# 15. Write a generator that yields unique elements from a list.
l1=[1,2,"apple",5,5,2]
def unique_elem():
	a=set(l1)
	b=list(a)
	for i in b:
		yield b
j=unique_elem()
print("Unique elements from a list")
print(next(j))
print("=================================================")



# 16. Convert a list comprehension into a generator expression.
num=[1,2,3,4,5,6]
def gen(num):
	a=[x*x for x in num]
	for i in a:
		yield i
a=gen(num)
print("Converting list comprehension to generator")
for i in a:
	print(i,end=" ")
print("\n=================================================")



# 17. Write a generator that yields numbers until their sum becomes greater than 100.
def greaterthan100():
	count=0
	for i in range(1,51):
		while count<=100:
			count= count+i
			yield count
a=greaterthan100()
print("Below are the numbers whose sum is greater than 100")
print(next(a),next(a),next(a),next(a),next(a),next(a),next(a),next(a),next(a),next(a),next(a),next(a),next(a),next(a))
print("=================================================")



# 18. Create a generator that yields reversed characters of a string.
str1="Python"
def rev_string():
	for i in str1[::-1]:
		yield i
g=rev_string()
print("Reversed characs of string")
print(next(g),next(g),next(g),next(g),next(g),next(g))
print("=================================================")


# 19. Write a generator that yields common elements from two lists.
l1=[1,2,"apple",5,23]
l2=[5,"apple",23,11]
def common_elements():
	for i in l1:
		if i in l2:
			yield i
h=common_elements()
print("common elements from two lists")
for i in h:
	print(i,end=" ")
print("\n=================================================")



# 11. Write a generator that yields running sum of numbers in a list.
l1=[1,34,2,1,16,8,9]
from functools import reduce
def sumlist():
	a=reduce(lambda x,y:x+y,l1)
	yield a
print("Sum of numbers in the list using reduce")
a=sumlist()
print(next(a))
print("=================================================")



# 10. Write a generator that yields factorials of numbers from 1 to n.
n=5
fact_dict={}
def factorial():
	fact=1
	for i in range(1,n+1):
		fact=i*fact
		fact_dict[i]=fact
	yield fact_dict
j=factorial()
print("Factorial of numbers")
for i in j:
	print(i)
print("=================================================")


# 14. Create an infinite generator that yields natural numbers starting from 1.

def infinite_gen():
	i=-1
	# to be given i=1 for infinite loop
	while i>0:
		i=i+1
		yield i
a=infinite_gen()
print("Infinite generator starting from 1, gave negative number for rest of the execution to run properly")
for i in a:
	print(i,end=" ")
print("=================================================")



# 12. Create a generator that yields lines from a file one by one.
def readlinesfile():
	a=open("Demotxt.txt",'r')
	for i in a:
		yield i
c=readlinesfile()
print("Yielding lines one by one from a txt file")
print()
for i in c:
	print(i)
print("=================================================")	




# 8. Write a generator that yields each word from a sentence one by one.
def sentone():
	senten1="I like python"
	s1=senten1.split()
	for i in s1:
		yield i
a=sentone()
print("Each word from sentence one by one")
print()
for i in a:
	print(i)
print("=================================================")	



# 20. Write a generator that yields palindrome numbers between 1 and 200.
def palind():
	for i in range(1,201):
		i=str(i)
		if i==i[::-1]:
			yield i
a=palind()
print("Palindrome numbers between 1 to 100")
for i in a:
	print(i,end=" ")
print("\n=================================================")



# 7. Create a generator that yields prime numbers up to 100.
def prime_nos():
	count=0
	for i in range(1,101):
		for j in range(1,i+1):
			if i%j==0:
				count=count+1
		if count== 2:
			yield i
		count=0
d=prime_nos()
print("Prime numbers from 1 to 100")
for i in d:
	print(i,end=" ")
print("\n=================================================")



# 6. Write a generator to generate the Fibonacci sequence up to n terms.

# 13. Write a generator that yields pairs of elements from a list (like (1,2), (3,4)).

