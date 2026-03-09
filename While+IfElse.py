# Print numbers 1 to 10 and print "Even" or "Odd" for each number.
i=0
while i<=9:
	i=i+1
	if i%2==0:
		print("Even-", i)
	else:
		print("Odd - ", i)
print("--------------------------------")
# Take a number from user and print its multiplication table using while loop.
num=int(input("Enter the number:"))
i=1
while i<=10:
		print(num ,"*", i ,"=" ,i*num)
		i=i+1
print("---------------Took help online-----------------")
# Count how many even numbers are between 1 to 20 using while loop.
count=0
i=1
while i<=20:
	i=i+1
	if i%2==0:
		count=count+1
print("Count of Even numbers between 1 to 20 are ", count)
print("--------------------------------")
# Ask user to enter password until correct password is entered.
password="12ABC"
passw=input("Enter password:")
while passw!=password:
	print("Invalid password,please enter password again")
	passw=input("Enter password Again:")
print("Password match")
print("--------------------------------")
# Print numbers from 1 to 50 and display only numbers divisible by 5.
i=1
while i<=50:
	i=i+1
	if i%5==0:
		print("Divisble by 5", i)
# ------------------------------------------------------------------------------------------------------------
# For Loop + If-Else Questions
# 1] Print numbers from 1 to 20 and check whether each number is even or odd
for i in range(1,11):
	if i%2==0:
		print("Even-", i)
	else:
		print("Odd - ", i)
# 2] Print all elements of a list and display whether the number is positive or negative
val_list=[1,2,-3,9,8,-2,-4,-5,0]
for i in val_list:
	if i==0:
		print("Neither negative nor positive", i)
	elif i<0:
		print("Negative number", i)
	else:
		print("positive", i)
# 3] Count vowels in a string using for loop
name = "Elephant"
vowels ="aeiouAEIOU"
count=0
for i in name:
	if i in vowels:
		# print(i)
		count=count+1
print(count)
print("----------------")
# 4] Print only numbers greater than 50 from a list
val_list = [10,20,20,40,50,60,70,80,90,100]
for i in val_list:
	if i>50:
		print(i,"Greater than 50")
	else:
		print(i, "Not greater than 50")
print("----------------")
# 5] Print multiplication table of a number using for loop
num=9
for i in range(1,11):
	print(num ,"*", i ,"=" ,i*num)
print("----------------")