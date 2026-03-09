# Print all prime numbers between 1 to 100.
is_prime=True
for i in range(1,101):
	for j in range(2,i):
		if i%j==0:
			is_prime=False
	if is_prime==True:
		print("prime number",i)

# Find the factorial of a number using for loop.
num= 9
fact=1
for i in range(1,num+1):
	fact=fact*i
print("Factorial of 9 is ",fact)

# Reverse a number using for loop.
num=12345678910
rev_num=0
temp=num
count=0
while temp>0:
	temp=temp//10
	count=count+1
temp=num
for i in range(count):
	digit=temp%10
	rev_num=rev_num*10+digit
	temp = temp // 10
print(rev_num)


# Count frequency of each character in a string.
name="elephaantt"
dicti={}
for i in name:
	if i in dicti:
		dicti[i]=dicti[i]+1
	else:
		dicti[i]=1
print(dicti)


#  Find second largest number in a list.
num_list=[80,8,900,18,8,2001]
largest_num=num_list[0]
second_largest=num_list[1]
if largest_num<second_largest and second_largest<largest_num:
	largest_num=second_largest
for i in num_list[2:]:
	if i>largest_num:
		second_largest=largest_num
		largest_num=i
	elif i<largest_num and i>second_largest:
		second_largest=i
print(second_largest)
print(largest_num)

numbers = [10, 20, 444, 45, 99]
larg=numbers[0]

for i in numbers:
	if i>larg:
		larg=i
print(larg)

second=numbers[0]

for i in numbers:
	if i>second and i!=larg:
		second=i
print(second)


# 6️
# ] Remove duplicates from a list using loop.
lis1=[1,2,3,4,4,4,5]
nondup_list=[]
for i in lis1:
	if i not in nondup_list:
		nondup_list.append(i)
	else:
		continue
print("Removed duplicates from the list",nondup_list)
# 7️
# ] Check whether a number is Armstrong number.
n=153
temp=n
count=0
arm_check=0
while temp>0:
	temp=temp//10
	count=count+1
temp=n
for i in range(count):
	digit=temp%10
	arm_check=arm_check+digit**count
	temp=temp//10
if arm_check==n:
	print("Armstrong number")
else:
	print("Not Armstrong")



# 8️
# ] Check whether a number is palindrome.
pal_num=1201
numstr=str(pal_num)
if numstr==numstr[::-1]:
	print(pal_num,"is palindrome")
else:
	print(pal_num,"is not palindrome")

# 9️
# ] Count how many words are in a sentence using for loop.
strinput="Hi Hello How are you"
count=0
strinput=strinput.split()
for i in strinput:
	count=count+1
print("count of the words in sentence is",count)

# 10] Find common elements between two lists.
list1=[1,2,3,4,6]
list2=[2,4,6,8]
common=[]
for i in list1:
	if i in list2:
		common.append(i)
print(common)


