# Python Function QT
# Write a Python function that accepts a string and counts the number of upper and
# lower case letters
uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
str3="HYDeraBADI"

def stri_accept(inputstr,uppercase):
	uppercount=0
	lowercount=0
	for i in str3:
		if i in uppercase:
			uppercount=uppercount+1
		else:
			lowercount=lowercount+1
	return uppercount,lowercount
up1, lo1 = stri_accept(str3,uppercase)
print("uppercase letter count is", up1)
print("lowercase letter count is", lo1)
	


# 2] Write a Python function that takes a list and returns a new list with distinct
# elements from the first list.
input_list = [1, 2, 2, 3, 4, 4, 5]
# output_list: [1, 2, 3, 4, 5]
list2=[]
def dupli(input_list):
	for i in input_list:
		if i not in list2:
			list2.append(i)
		else:
			continue
	# output_list=set(input_list)
	# output_list = list(output_list)
	return list2
output_list = dupli(input_list)
print("Removed duplicates", output_list)



# 3] Write a Python function that takes a number as a parameter and checks whether the
# number is prime or not.
a=7
def primeornot(num):
	count=0
	for i in range(1,num+1):
		if num%i==0:
			count=count+1
	if count>2:
		print("not a prime number",num)
	else:
		print("it is a prime number",num)
primeornot(a)


# 4] Write a Python function that takes a list of numbers and prints the even numbers
# from the list.
num_list=[1,23,45,36,23,22,76,89,112,1,11,26,767,887,32]
def prime_numbers(numbers):
	for i in numbers:
		if i%2==0:
			print("even number is",i)
		else:
			pass
prime_numbers(num_list)


# 5] Write a Python function that checks whether a passed string is a palindrome or
# not.
str1="elle"
str2 = ""
def pali(inputstr,str2):
	for i in inputstr:
		str2=i+str2
	if str1==str2:
		print(str1, ": It is a palindrome")
	else:
		print(str1, "Not a palindrome")
pali(str1,str2)

# 6] Write a Python function that takes a string containing Python code and executes it.
py_code = """for i in range(3):
				print(i)"""
def exec_pycode(pycode):
	exec(pycode)
exec_pycode(py_code)

# 7] Write a Python function that takes a list and two indices, and swaps the elements
# at those indices.
inp_list = [15,25]
def swap_list(inputlist):
	# inputlist = inputlist[::-1]
	inputlist = inputlist[1],inputlist[0]
	inputlist = list(inputlist)
	return inputlist
swapoutput=swap_list(inp_list)
print("swap list is",swapoutput)


# 8] Write a Python function that calculates the length of a given list
def cal_len(numbers):
	count=0
	for i in num_list:
		count=count+1
	return count
count=cal_len(num_list)
print("Length of the list is ",count)

# 9] Write a Python function that takes two numbers as parameters and returns the
# maximum of the two.
a=200
b=2000
def maxof_two(num1,num2):
	if num1>num2:
		return num1
	else:
		return num2
max_num=maxof_two(a,b)
print(max_num,"max number")

# 10] Write a Python function that takes two numbers as parameters and returns the
# minimum of the two.
def minof_two(num1,num2):
	if num1<num2:
		return num1
	else:
		return num2
min_num=minof_two(a,b)
print(min_num,"min number")

# 11] Write a Python function that takes a string as input, splits the string into words,
# reverses the order of words, and returns the reversed string.
str2 = "Happy Birthday Girl"
rev_string = ""
check_rev= ""
def reverse_string(inputstr,rev_string,check_rev):
	for i in inputstr:
			if i!=" ":
				rev_string = rev_string + i
			else:
				check_rev= rev_string +" " + check_rev
				rev_string = ""
	check_rev= rev_string +" " + check_rev
	return check_rev
reversed_output=reverse_string(str2,rev_string,check_rev)
print("Reversed string is ", reversed_output)

# Find max and minimum of the list 
l=[10,20,100,40,99]
def min_max(inp_list):
	a=inp_list[0]
	for i in inp_list:
		if i>a:
			a=i
	print("Largest number in the list", a)
	for i in inp_list:	
		if i<a:
			a=i
	print("Smallest number in the list", a)
min_max(l)


