# COMPREHENSION QT[expression for item in iterable if condition]
# Qt 1] How can you find all the even numbers in a given list of integers using Python?
[print("Even numbers are", i) for i in range(10) if i%2==0]

# Qt 2] How can you find all the odd numbers in a given list of integers using Python?
[print("Odd numbers are", i) for i in range(10) if i%2!=0]

# Qt 3] How can you compress a string in Python by counting consecutive repeated
# characters and appending the character followed by its count? (e.g., "aaabbc" ->
# "a3b2c1")
a="aaabbc"
b=a[0]
count_str=""
count=1
for i in a[1:]:
	if i==b:
		count=count+1
	else:
		count_str=count_str+b+str(count)
		b=i
		count=1
count_str=count_str+b+str(count)
print(count_str)


# Qt 4] How can you output a string in Python with the first letter capitalized?
inputstr="priya"
a=inputstr[0].upper()
print(a)
# Qt 5] How can you create a list using list comprehension with a nested for loop in
# Python?
string2="abcdef"
str3="cef"
list1=[j for i in string2 for j in str3 if i==j]
print(list1)

# Qt 6] How can you create a list using multiple conditionals in list comprehensions in
# Python?
# list2=[true expression if condition else condition for item in iterable]

# Qt 7] list1 = [1, -12, 34, -4, 25, -16, 19], write a Python program to
# create a new list list2 that contains the string " +ve " for each positive number and
# " -ve " for each negative number using list comprehension with if-else
# conditionals. Print the resulting list2.
list1 = [1, -12, 34, -4, 25, -16, 19]
list2=[str(i)+"+ve" if i>0 else str(i)+"-ve" for i in list1]
print(list2)

# Qt 8] string = 'AbcDeFG', write a Python program to create a new list list1 that
# contains each character of the string converted to uppercase using list
# comprehension. Print the resulting list1.
string1 = 'AbcDeFG'
list1=[i.upper() for i in string1]
print(list1)

# QT 9] Create a dictionary using dictionary comprehension
# Convert the numbers squares to cubes by using dict comprehension
my_squares={1:1,2:4,3:9,4:16,5:25}
cubes={i:i*j for i,j in my_squares.items()}
print(cubes)

# QT 10] family_id = {'richerd': 44, 'mary': 7, 'lucy': 40, 'William': 60, 'wick': 10}
# QT 11]Given a dictionary family_id representing the ages of family members,
# write a Python program to create a new dictionary voters_id that includes only
# those family members who are eligible to vote (i.e., age 18 and above). Use
# dictionary comprehension to achieve this and print the resulting voters_id.
print("duplicate")
# QT 12] family_id = {'richerd': 44, 'mary': 7, 'lucy': 40, 'William': 60, 'wick': 10}
# Given a dictionary family_id representing the ages of family members, write a
# Python program to create a new dictionary voters_id that includes only those
# family members who are eligible to vote (i.e., age 18 and above) and who are
# senior citizens (i.e., age 60 and above). Use dictionary comprehension with
# multiple conditionals to achieve this and print the resulting voters_id.
family_id = {'richerd': 44, 'mary': 7, 'lucy': 40, 'William': 60, 'wick': 10}
voters_id = {i:j for i,j in family_id.items() if j>=18 or j>=60}
print(voters_id)

# QT 13] Given a list list = ['java', 'python', 'pandas'], write a Python program to
# create a dictionary my_dict using dictionary comprehension and enumerate()
# that maps each element of the list to its corresponding index. Print the
# resulting my_dict.
list1 = ['java', 'python', 'pandas']
my_dict=[{i:j} for i,j in enumerate(list1)]
print(my_dict)

# QT 14] Given a dictionary my_squares={1:1,2:4,3:9,4:16,5:25} containing
# squares of numbers, write a Python program to create a new dictionary
# my_cubes using dictionary comprehension that maps each key-value pair
# from my_squares to its cube. Print the resulting my_cubes.
my_cubes=[{i:i**3} for i in range(1,6)]
print(my_cubes)