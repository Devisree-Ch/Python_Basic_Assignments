#Print statement
print("Hello Python")
print('Devisree')
print('Welcome to Coding '*3)
print(5+10)

#Variables
age = 20
a=10
b=5
print(a+b)
myname = 'Devisree'
print(myname)
x=5
x=10
print(x)
print(type(x))

#DataTypes
a=10
print(type(a))
b=10.20
print(type(b))
c='Stringtype'
print(type(c))
d=True
print(type(d))
e= None
print(type(e))

#List
fruits = ['apple','banana','grapes','papaya']
print(fruits[0])
fruits.append('watermelon')
print(fruits)
fruits.remove('apple')
print(fruits)
print(len(fruits))

#Tuple
fruitup = ('apple','banana','grapes','papaya')
print(fruitup[0])
singletup = (1)
print(len(fruitup))

#Set
dupli_set = {1,4,5,6,6,90,70,70}
print(dupli_set)
dupli_set.add(88)
print(dupli_set)
dupli_set.remove(90)
print(dupli_set)
print("Duplicate list to set conversion")
dupli_list = [1,4,5,6,6,90,70,70]
converted_set = set(dupli_list)
print(converted_set)
a1={2,3,4,5,6,7}
a2={1,5,6,7,8,9,10}
print(a1.union(a2))


#Dictionary
People = {'name': 'Devisree', 'age':27}
print(type(People))
print(People.get('name'))
People['School']='DPS'
print(People)
print(People.keys())
print(People.values())
