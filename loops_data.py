salaries = [10000, 20000, 15000, 8000, 25000]
#  Using a loop, filter salaries greater than 10000
#  Add a 10% increment to each of these salaries
#  Calculate the total of updated salaries
newsal=[]
total=0
for i in salaries:
	if i>=10000:
		hike=(10/100)*i
		i=i+hike
	newsal.append(i)
for i in newsal:
	total=total+i
print("new salaries",newsal)
print("old salaries",salaries)
print("total salaries",total)
prices = [100, 250, 300, 150, 80]
# Using a loop, select items with price greater than 100
# Apply a 20% discount to each selected item
# Calculate the final total bill
newprices=[]
totalbill=0
for i in prices:
	if i>100:
		disc_price=(20/100)*i
		i=i-disc_price
	newprices.append(i)
for i in newprices:
	totalbill=totalbill+i
print("Oldprices",prices)
print("newprices",newprices)
print("total bill",totalbill)
names = ["Ali", "", "Sara", " ", "John", ""]
new_names=[]
# Using a loop, remove empty or blank names
# Convert valid names to uppercase
for i in names:
	i=i.upper()
	if i.strip()!="":
		new_names.append(i)
print(new_names)