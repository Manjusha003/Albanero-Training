#Dictionaries
#dictionaries are indexed by keys, which can be any immutable type
#strings and numbers can always be keys. Tuples can be used as keys if they contain only strings, numbers, or tuples; if a tuple contains any mutable object either directly or indirectly, it cannot be used as a key. 
#dictionary as a set of key: value pairs, with the requirement that the keys are unique (within one dictionary).

# dictionary={
#     'name':"manjusha",
#     'clas':'bcs',
#     'age':22
# }
# print(dictionary)

# print(list(dictionary))  # returns all the keys in array

# print(sorted(dictionary)) # returns all the keys in sorted array

# print('age' in dictionary) # return boolean value

# dictionary['roll']=10001 # add new key:value pair in dictionary
# print(dictionary)


#The dict() constructor builds dictionaries directly from sequences of key-value pairs:

# dictionary=dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
# print(dictionary)


# l1={x:x**2 for x in (2,3,4,6)}
# print(l1)

# dictionary=dict(shape="circular",color="red",roll="5646")
# print(dictionary)

# items()
# for key,value in dictionary.items():
#     print(key,value)


# keys=["name","age","roll","hobby"]
# values=['Ravi',21,234,'coding']

# for key, value in zip(keys,values):
#     print('this is key {0}? it is value {1}'.format(key,value))
#     print('{0}:{1}'.format(key,value),end=',')


# for i in range(1,10,2):
#     print(i)

# for i in reversed(range(1,10,2)):
#     print(i)


# comaparing
print((1, 2, 4)==(1, 2, 4))
print([1,2,3]==[1,2,3])
print({"name":"manju"}=={"name":"manju"})
