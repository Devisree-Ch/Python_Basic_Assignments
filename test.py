# Write a Python program to reverse a number.
# num=1234
# rev_num=str(num)
# rev=rev_num[::-1]
# rev=int(rev)
# print(rev)
# rev=0
# while num>0:
# 	digit=num%10
# 	rev=rev*10+digit
# 	num=num//10
# print(rev)
# Write a Python program to find the first non-repeating character in a string.
# s1="aabbcdde"
'''for i in s1:
	if s1.count(i)==1:
		print(i)
		break'''
'''for i in s1:
	count=0
	for j in s1:
		if i==j:
			count=count+1
	if count==1:
		print(i)
		break'''
# Write a Python program to find the length of a list without using len().
# l1=[1,2,3,4,5]
# count=0
# for i in l1:
# 	count=count+1
# print(count)
# Write a Python program to merge two dictionaries.
# d1={'name':'devi'}
# d2={'age':'20'}
# d3={}
# for i in d1:
# 	d3[i]=d1[i]
# for j in d2:
# 	d3[j]=d2[j]
# print(d3)
# Write a Python program to find the sum of all numbers in a tuple.
# t1=(1,2,3)
# sum=0
# for i in t1:
# 	sum=sum+i
# print(sum)