# 1. Print the following pattern
# *
# * *
# * * *
# * * * *
a="*"
count=0
for i in range(1,5):
	count=count+1
	print(count*a)
print("-------------------------------------")
# 2. Print the following pattern
# * * * *
# * * *
# * *
# *
count=5
for i in range(1,5):
	count=count-1
	print(count*a)
print("-------------------------------------")
# 3. Print the following square pattern
# * * * *
# * * * *
# * * * *
# * * * *
for i in range(4):
	print(a*4)
print("-------------------------------------")
# 4. Print the following pattern
# 1
# 1 2
# 1 2 3
# 1 2 3 4
count=1
count2=1
for i in range(1,5):
	print(count)
print("-------------------------------------")
# 5. Print the following pattern
# 1
# 2 2
# 3 3 3
# 4 4 4 4
count=0
for i in range(1,5):
	count=count+1
	print(count)
print("-------------------------------------")
# 6. Print the following pattern
# A
# A B
# A B C
# A B C D
print("-------------------------------------")
# 7. Print the following pattern
# 1
# 2 3
# 4 5 6
# 7 8 9 10
print("-------------------------------------")
# 8. Print the following pattern
# 1 1 1 1
# 2 2 2 2
# 3 3 3 3
# 4 4 4 4
print("-------------------------------------")
# 9. Print the following pattern
# *
# **
# ***
# ****
# *****
count=0
for i in range(1,6):
	count=count+1
	print(a*count)
print("-------------------------------------")
# 10. Print the following pattern
# *****
# ****
# ***
# **
# *
count=5
for i in range(1,6):
	print(a*count)
	count=count-1
print("-------------------------------------")
# 11. Print the following pyramid
# *
# ***
# *****
# *******
for i in range(1,8):
	if i%2!=0:
		print(a*i)
print("-------------------------------------")
# 12. Print the following reverse pyramid
# *******
# *****
# ***
# *
for i in range(8,0,-1):
	if i%2!=0:
		print(a*i)
print("-------------------------------------")
# 13. Print the following diamond pattern
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
for i in range(1,8):
	if i%2!=0:
		print(" ",a*i," ")
for i in range(6,0,-1):
	if i%2!=0:
		print(" ",a*i," ")

print("-------------------------------------")
# 14. Print the following pattern
# 1
# 1 0
# 1 0 1
# 1 0 1 0
print("-------------------------------------")
# 15. Print the following pattern
# 1
# 2 1
# 3 2 1
# 4 3 2 1
print("-------------------------------------")
# 16. Print the following pattern
# A
# B C
# D E F
# G H I J
print("-------------------------------------")
# 17. Print the following pattern
# * *
# * *
# *
# * *
# * *
print("-------------------------------------")
# 18. Print the following hollow square
# * * * *
# * *
# * *
# * * * *
count=4
for i in range(1,5):
	print(a*count)
	count=count-2
print("-------------------------------------")
# 19. Print the following pattern
# 1
# 2 3
# 3 4 5
# 4 5 6 7
print("-------------------------------------")