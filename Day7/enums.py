#Enumerations in Python are implemented by using the module named “enum“.Enumerations are created using classes. Enums have names and values associated with them.

from enum import Enum

class Season(Enum):
	SPRING = 1
	SUMMER = 2
	AUTUMN = 3
	WINTER = 4

# printing enum member as string
print(Season.SPRING)

# printing name of enum member using "name" keyword
print(Season.SPRING.name)


# printing value of enum member using "value" keyword
print(Season.SPRING.value)
 

 # printing the type of enum member using type()
print(type(Season.SPRING))
 
# printing enum member as repr
print(repr(Season.SPRING))
 
# printing all enum member using "list" keyword
print(list(Season))








# Enum members can be accessed in two ways:

# By value:- In this method, the value of enum member is passed.
# By name:- In this method, the name of the enum member is passed.

from enum import Enum

class Season(Enum):
	SPRING = 1
	SUMMER = 2
	AUTUMN = 3
	WINTER = 4

# Accessing enum member using value
print("The enum member associated with value 2 is : ", Season(2).name)

# Accessing enum member using name
print("The enum member associated with name AUTUMN is : ", Season['AUTUMN'].value)



#Enumerations are iterable. They can be iterated using loops

from enum import Enum

class Season(Enum):
	SPRING = 1
	SUMMER = 2
	AUTUMN = 3
	WINTER = 4

for animals in (Season):
	print(animals.value,"-",animals.name)


#Enumerations support hashing


import enum

# creating enumerations using class
class Animal(enum.Enum):
	dog = 1
	cat = 2
	lion = 3

# Hashing enum member as dictionary
di = {}
di[Animal.dog] = 'bark'
di[Animal.lion] = 'roar'

print(di)
# checking if enum values are hashed successfully
if di == {Animal.dog: 'bark', Animal.lion: 'roar'}:
	print("Enum is hashed")
else:
	print("Enum is not hashed")






#Enumerations support two types of comparisons
# Identity:- These are checked using keywords “is” and “is not“.
# Equality :- Equality comparisons of “==” and “!=” types are also supported.


# importing enum for enumerations
import enum

# creating enumerations using class
class Animal(enum.Enum):
	dog = 1
	cat = 2
	lion = 3

# Comparison using "is"
if Animal.dog is Animal.cat:
	print("Dog and cat are same animals")
else:
	print("Dog and cat are different animals")

# Comparison using "!="
if Animal.lion != Animal.cat:
	print("Lions and cat are different")
else:
	print("Lions and cat are same")



import enum
# Using enum class create enumerations
class Days(enum.Enum):
   Sun = 1
   Mon = 2
   Tue = 3
# printing all enum members using loop
print ("The enum members are : ")
for weekday in Days:
   print(weekday)


# We can access the enum members by using the name or value of the member items#

import enum
# Using enum class create enumerations
class Days(enum.Enum):
   Sun = 1
   Mon = 2
print('enum member accessed by name: ')
print (Days['Mon'])
print('enum member accessed by Value: ')
print (Days(1))
