"""
**********QT**********
var="python program"
output="program python"
"""
var="python program"
opt = var.split(" ")
# print(opt)
final=(opt[1],opt[0])
print(str(final))
print("----------------")
#-----------------------------------------------
name="Sri"
for i in name:
	print(i)
print("----------------")
# ------------------------------------------------
name = "Elephant"
vowels ="aeiouAEIOU"
count=0
for i in name:
	if i in vowels:
		# print(i)
		count=count+1
print(count)
print("----------------")
# ----------------------------------------------------
name="DevisREE"
uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
count=0
for i in name:
	if i in uppercase:
		count=count+1
print("upper case count is ",count)
print("----------------")
# -------------------------------------------------------
for i in range(1,11):
	print(i)
print("----------------")
# ---------------------------------------------------------
val=(1,7,4,-5)
count=0
for i in val:
	print("Tuple elements", i)
for i in val:
	if i>0:
		count=count+1
	else:
		print("Negative number ",i)
print("Total elements in tuple are", count)
print("----------------")		
# ------------------------------------------------------------
fruits = ["apple","banana","grapes"]
for i in fruits:
	print(i)
print("----------------")
# ------------------------------------------------------------	
num=[1,2,3,4,5,6,7,8]
for i in num:
	if i%2==0:
		print("even number:",i)
print("----------------")
sum=0
for i in num:
	sum=sum+i
print("Sum of all numbers in the given list is ",sum)
print("----------------")
# ------------------------------------------------------------
num=9
for i in range(1,11):
	print(num ,"*", i ,"=" ,i*num)
print("----------------")
# ------------------------------------------------------------
# Print the string in reverse using a for loop.
a="Birthday"
rev_strig=""
for i in a:
	rev_strig=i+rev_strig
print(rev_strig)
# Find the smallest number in a tuple
tup=(100,2,4,5,90,23)
tup1=tup[0]
for i in tup:
	if tup1<i:
		continue
	else:
		tup1=i
print("Smallest number",tup1)

