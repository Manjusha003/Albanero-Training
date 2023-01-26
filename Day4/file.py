# f=open('inputoutput.py', 'w')

# with open('inputoutput') as f:
#     read_data = f.read()
#     f.closed

# f = open('Day4/first', 'w')
# print(f.write("Hello"))

#Methods of File Objects

# f=open('Day4/first.py','w')
# f.write("Welcome")
# print(f.read())


#The JSON format is commonly used by modern applications to allow for data exchange. Many programmers are already familiar with it, which makes it a good choice for interoperability.

import json
p=json.dumps([1,"hello","bye"])
print(p)


