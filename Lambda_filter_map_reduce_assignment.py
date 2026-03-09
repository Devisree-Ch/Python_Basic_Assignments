"""
var=lambda args:logic
print(var(args_values)) 
"""
# 1] Write a lambda function to add two numbers.
sum = lambda a,b:a+b
print("Sum of two numbers is : ",sum(15,10))
# 2] Write a lambda function to find the square of a number.
sqr = lambda a:a*a
print("Square root is", sqr(3))
# 3] Write a lambda function to check if a number is even or odd.
EorO = lambda a:"Even" if a%2==0 else "Odd"
print("This number is", EorO(5))
# 4] Write a lambda function to get the last character of a string.
LastCharString = lambda str1:str1[-1]
print("The last character of the string:", LastCharString("Python"))
# 5] Write a lambda function to multiply three numbers.
MultiThree = lambda a,b,c:a*b*c
print("Multiplication of three numbers is : ", MultiThree(2,1,3))
# 6] Write a lambda function to find the maximum of two numbers.
MaxofTwo = lambda a,b: b if b>a else a
print("The largest of two elements is :", MaxofTwo(8,10))
# 7] Write a lambda function to reverse a string.
RevString = lambda str2 : str2[::-1]
print("Reverse of string is ", RevString("Amazing"))
# 8] Write a lambda function to calculate simple interest.
SI = lambda p,t,r:(p*t*r)/100
print("Simple interest is : ", SI(10000,3,6))
# 9] Write a lambda function to return "Pass" if marks ≥ 40 else "Fail".
Student = lambda marks: "Pass" if marks>=40 else "Fail"
print("Student result is ", Student(35))
# 10] Write a lambda function to check whether a number is divisible by 5 or not.
Divby5 = lambda a: "Is divisible" if a%5==0 else "Not Divisble"
print(Divby5(6), "--> To Check is div by 5")
# 11] Write a lambda function to calculate 10% discount on a product price.
Disc = lambda normal_price : normal_price*10/100
print("Discount of 10% applied", Disc(500))
# To return the discounted price
Disc = lambda normal_price : normal_price-normal_price*10/100
print("Total price after Discount of 10% applied", Disc(500))
# 12] Write a lambda function to check if a word starts with the letter ‘A’.
StartwithA = lambda word : "Starts with A" if word[0]=="A" else "Doesn't start with A"
print("Starting A validation---->", StartwithA("mogha"))
# 13] Use map() to square all numbers in the list [1, 2, 3, 4, 5].

inpList = [1, 2, 3, 4, 5]
empList = []
# map(function, iterable)
emptyList = list(map(lambda inpList:inpList*inpList, inpList))
print("Squares of each element in list using map",emptyList)

def sqrlist(inpList):
	for i in inpList:
		sqrs = i*i
		empList.append(sqrs)
	return empList
squares = sqrlist(inpList)
print("Squares of each element in list using function",squares)
# 14] Use map() and lambda to convert a list of strings to uppercase.
str1 = ['a','b','c']
uppperstr1 = list(map(lambda str1:str1.upper(),str1))
print("converted the list to upppercase using map",uppperstr1)
emp1=[]
def converttoUpper(str1):
	for i in str1:
		emp1.append(i.upper())
	return emp1
upperlist = converttoUpper(str1)
print("converted the list to upppercase using function",upperlist)
# 15] Use map() to add 10 to every number in [5, 10, 15, 20].
inp1=[5, 10, 15, 20]
plus10s = list(map(lambda inp1:inp1+10, inp1))
print("Added 10 to each element in list using map",plus10s)
emp2=[]
def add10to(inp1):
	for i in inp1:
		emp2.append(i+10)
	return emp2
newlist=add10to(inp1)
print("Added 10 to each element in list using function",newlist)
# 16] Use map() to find the length of each word in ["python", "sql", "django"].
lenlis=["python", "sql", "django"]
length=[]
findlen = list(map(lambda lenlis:len(lenlis), lenlis))
print("Finding length of each element in the list using map",findlen)

def findlenth(lenlis):
	for i in lenlis:
		length.append(len(i))
	return length
lenli=findlenth(lenlis)
print("Finding length of each element in the list using function",lenli)

# 17] Given two lists [1, 2, 3] and [4, 5, 6], use map() and lambda to add them element-wise.
# list1=[1, 2, 3]
# list2=[4, 5, 6]
# res = list(map(lambda list2:list1.append(list2),list1,list2))
# print("Adding 2 lists using map", res())
# 18] Use map() to extract the first letter of each word in a list.
list_words = ['Apple','Zebra','Mango']
res=list(map(lambda list_words:list_words[0],list_words))
print(res,"----First letters using map")

def first_letter(list_words):
	for i in list_words:
		print(i[0], "first letter of ", i, "------using function")
first_letter(list_words)

# 19] Use filter() to get only even numbers from a list [1, 2, 3, 4, 5, 6].
Listnum=[1, 2, 3, 4, 5, 6]
emp=[]
res = list(filter(lambda Listnum:Listnum%2==0,Listnum))
print(res,"Even numbers in the list using filter")

def even_number(Listnum):
	for i in Listnum:
		if i%2==0:
			emp.append(i)
	print(emp,"Even numbers in the list using function")
even_number(Listnum)
# 20 ] Use filter() to get only numbers greater than 10 from [5, 15, 20, 25, 2, 7].
listgreat=[5, 15, 20, 25, 2, 7]
emplist=[]
res=list(filter(lambda listgreat:listgreat>10,listgreat))
print(res,"Numbers greater than 10 using filter")

def numbgreat(listgreat):
	for i in listgreat:
		if i>10:
			emplist.append(i)
	print(emplist,"Numbers greater than 10 using function")
numbgreat(listgreat)
# 21] Use filter() and lambda to get names starting with "A" from ["Afsha", "Faizan", "Rafay", "Ali"].
names=["Afshaaaaa", "Faizan", "Rafay", "Ali"]
res=list(filter(lambda names:names[0]=='A',names))
print(res,"names starting with A using filter")
empnames=[]
def names_start(names):
	for i in names:
		if i[0]=='A':
			empnames.append(i)
	print(empnames,"Names starting with A using function")
names_start(names)
# 22] Use filter() to get words longer than 4 characters from a list.
res=list(filter(lambda names:len(names)>4,names))
print(res,"are the words longer than 4 characters using filter")

def longerthan4(names):
	empnames=[]
	for i in names:
		if len(i)>4:
			empnames.append(i)
	print(empnames,"are the words longer than 4 characters using function")
longerthan4(names)
 # 23] Use filter() to get all prime numbers from [2, 3, 4, 5, 6, 7, 8, 9]. 
listprimes=[2, 3, 4, 5, 6, 7, 8, 9]
 # res=list(filter(lambda listprimes:))


def primeornot(listprimes):
	count=0
	for i in listprimes:
		for j in range(2,i+1):
			if i%j==0:
				count=count+1
		if count>1:
			print(i,"it is prime")
		else:
			print(i,"not prime")
primeornot(listprimes)
 # 24] Use filter() to find all positive numbers from [-5, -2, 0, 3, 7, -1]. 
posneg=[-5, -2, 0, 3, 7, -1]
res=list(filter(lambda posneg:posneg>=0,posneg))
print(res,"finding positive numbers using filter")

emplist=[]
def find_positive(posneg):
	for i in posneg:
		if i>=0:
			emplist.append(i)
	print(emplist,"finding positive numbers using function")
find_positive(posneg)

 # 25] Use reduce() to find the sum of numbers [10, 20, 30, 40].
from functools import reduce
sumnum=[10, 20, 30, 40]
res=reduce(lambda sum,num:sum+num,sumnum)
print(res,"sum of numbers in the list using reduce")

def sum_num(sumnum):
	sum=0
	for i in sumnum:
		sum=sum+i
	print(sum,"sum of numbers in the list using function")
sum_num(sumnum)

#  26] Use reduce() to find the product of numbers [1, 2, 3, 4, 5].
prod= [1, 2, 3, 4, 5]
res = reduce(lambda x,y:x*y,prod)
print(res,"Product of numbers in the list using reduce")

def product_numbers(prod):
	product=1
	for i in prod:
		product=product*i
	print(product,"Product of numbers in the list using Function")
product_numbers(prod)

#  27] Use reduce() to find the maximum number in [5, 8, 12, 3, 9].
max_num=[5, 8, 12, 3, 9]
# res=reduce(lambda max_num:max_num,max_num)
print(res,"maximum number in the list using reduce")

def maximum(max_num):
	max=max_num[0]
	for i in max_num:
		if i>max:
			max=i
	print(max,"maximum number in the list using function")
maximum(max_num)

#  28] Use reduce() to concatenate all strings in a list ["Python", "is", "fun"]. 
strlist=["Python", "is", "fun"]
res=reduce(lambda x,y:x+y,strlist)
print(res,"Concatenate all strings using reduce")
#  29] Use reduce() to find the longest word in a list ["apple", "banana", "kiwi", "strawberry"]. 
#  30] Given a list [1, 2, 3, 4, 5, 6, 7, 8, 9],
# ● use filter() + lambda to get even numbers
# ● then use map() + lambda to square those even numbers.
list_mapfil_combo=[1, 2, 3, 4, 5, 6, 7, 8, 9]
res=list(filter(lambda list_mapfil_combo:list_mapfil_combo%2==0,list_mapfil_combo))
print(res,"Found even numbers, next is to square them")
res1 = list(map(lambda res:res*res,res))
print(res1,"Squared all the filtered even numbers")

def findeven_andsquare(list_mapfil_combo):
	emplist=[]
	for i in list_mapfil_combo:
		if i%2==0:
			emplist.append(i*i)
	print(emplist,"Squared all the filtered even numbers-----using function")
findeven_andsquare(list_mapfil_combo)

# 31] Use reduce() to find the total salary of employees in the list [25000, 30000, 40000, 50000].
sal_list=[25000, 30000, 40000, 50000]
res=reduce(lambda x,y:x+y,sal_list)
print(res,"Total salaries using reduce")

def totalsal(sal_list):
	emplist=0
	for i in sal_list:
		emplist=emplist+i
	print(emplist,"Total salaries using function")
totalsal(sal_list)
# 32] Given a list of student marks [40, 55, 65, 30, 80, 90],
# ● use filter() to select marks ≥ 50
# ● use map() to increase each passing mark by 5
# ● use reduce() to find the total of all increased marks.
marks =[40, 55, 65, 30, 80, 90]
res=list(filter(lambda marks:marks>=50,marks))
print(res,"Marks greater than 50 using filter")
res1=list(map(lambda res:res+5,res))
print(res1,"Adding 5 marks to each pass marks using map")
res2=reduce(lambda x,y:x+y,res1)
print(res2,"Total of all marks increased")

def marks_calc(marks):
	emplist=[]
	for i in marks:
		if i>=50:
			emplist.append(i+5)
	print(emplist,"Filtered pass marks and Adding 5 marks to each pass marks using Function")
	total=0
	for i in emplist:
		total=total+i
	print(total,"Total of all marks increased using function")
marks_calc(marks)
# 33] Create a lambda-based function that takes a list of employee dictionaries and filters those with salary > 50000.
# empdict=[{"Swetha":10000},{"Ramya":20000},{"Anitha":50000},{"Varun":100000}]
# res=list(filter(lambda empdict:empdict[items]>50000,empdict))
# print(res,"Returning salaries greater than 50000")
# # 34] Use map() and lambda to format employee names in uppercase and filter() to select only employees from "IT" department.

