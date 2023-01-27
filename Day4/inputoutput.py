#two ways of writing values: expression statements and the print() function. (A third way is using the write() method of file objects


#To use formatted string literals, begin a string with f or F before the opening quotation mark or triple quotation mark.
#Inside this string, you can write a Python expression between { and } characters that can refer to variables or literal values.
year=1989
name="Tony"
print(f'my name is {name} and the year is {year}')
print(str(name))


# The str.format() method of strings requires more manual effort. You’ll still use { and } to mark where a variable will be substituted and can provide detailed formatting directives, but you’ll also need to provide the information to be formatted.

yes_votes = 42_572_654
no_votes = 43_132_495
percentage = yes_votes / (yes_votes + no_votes)
print('{:-2} YES votes  {:2.1%}'.format(yes_votes, percentage))

#The repr() of a string adds string quotes and backslashes:
print(repr(7438798))
print(repr(name))

a=29+56
b=89*10

print("The values of a is", repr(a),"and b is", repr(b)) # using , we can automatically add the space
print("The values of a is"+repr(a)+"and b is"+ repr(b)) # using + we need to add space by yourself


# The argument to repr() may be any Python object:
print(repr((a, b, ('spam', 'eggs'))))


import math
print(f'The value of pi is',math.pi)
print(F'The value of pi is',math.pi)
print('')


table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}

#Passing an integer after the ':' will cause that field to be a minimum number of characters wide. This is useful for making columns line up.
for name,phone in table.items():
    print(f'{name:10} ==> {phone:10}')


for name,phone in table.items():
    print(f'{name} ==> {phone}')


#'!a' applies ascii(), '!s' applies str(), and '!r' applies repr():

name="manjusha"
print(f'My Name is {name}.')
print(f'My Name is {name!r}.')
print(f'My Name is {name!s}.')




# str.format()

print("Hello {} , welcome to {}".format("Manjusha","Albanero"))

#The brackets and characters within them (called format fields) are replaced with the objects passed into the str.format() method. A number in the brackets can be used to refer to the position of the object passed into the str.format() method.
print("Hello,My name is {1} and my class is {0}".format("Manjusha","BCS"))


#If keyword arguments are used in the str.format() method, their values are referred to by using the name of the argument.

print("My hobby is {hobby} and i'm {age} old".format(hobby="coding",age="22"))


table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))


# for x in range(1, 11):
#     print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))


#The str.rjust() method of string objects right-justifies a string in a field of a given width by padding it with spaces on the left.
#There are similar methods str.ljust() and str.center(). These methods do not write anything, they just return a new string. If the input string is too long, they don’t truncate it, but return it unchanged; 

for x in range(1, 11):
    print(repr(x).rjust(4),repr(x*x).rjust(4),end=' ')
    print(repr(x*x*x).rjust(4))


#str.zfill(), which pads a numeric string on the left with zeros. It understands about plus and minus signs:

a='23' .zfill(4)
print(a)

b='-3.14'.zfill(7)
print(b)


#Old string formatting
#The % operator (modulo) can also be used for string formatting. Given 'string' % values, instances of % in string are replaced with zero or more elements of values. This operation is commonly known as string interpolation

import math
print('The value of pi is approximately %5.3f.' % math.pi)


#Reading and Writing Files
#open() returns a file object, and is most commonly used with two arguments: open(filename, mode).


#The first argument is a string containing the filename. The second argument is another string containing a few characters describing the way in which the file will be used


#mode can be 'r' when the file will only be read, 
# 'w' for only writing (an existing file with the same name will be erased), 
# 'a' opens the file for appending; 
# 'r+' opens the file for both reading and writing


#It is good practice to use the with keyword when dealing with file objects
#Using with is also much shorter than writing equivalent try-finally blocks:

#It is good practice to use the with keyword when dealing with file objects. The advantage is that the file is properly closed after its suite finishes, even if an exception is raised at some point. Using with is also much shorter than writing equivalent try-finally blocks:

with open('first.txt') as f:
    data=f.read()
    print(data)

# If you’re not using the with keyword, then you should call f.close() to close the file and immediately free up any system resources used by it. If you don’t explicitly close a file, Python’s garbage collector will eventually destroy the object and close the open file for you, but the file may stay open for a while. Another risk is that different Python implementations will do this clean-up at different times.



#Methods of File Objects
# file1=open("first.txt","r")
#f.read(size), which reads some quantity of data and returns it as a string (in text mode) or bytes object (in binary mode). size is an optional numeric argument.

# print(file1.read(12)) # return the first 12 char of the first.txt

#f.readline() reads a single line from the file; a newline character (\n) is left at the end of the string, and is only omitted on the last line of the file if the file doesn’t end in a newline

#print(file1.read())

# print(file1.readline()) # read single line
#if you want to read all the lines of a file in a list you can also use list(f) or f.readlines().
#print(file1.readlines()) #['Hello\n', 'welcome']

#By looping through the lines of the file, you can read the whole file, line by line
# for line in file1:
#     print(line)

# file1.close()

#To write to an existing file, you must add a parameter to the open() function
# file= open("first.txt","a")
# file.write("I am happy..!")
# file.close()


# Open the file "first.txt" and overwrite the content:
# f=open("first.txt",'w')
# f.write("this is my 4th day in albanero")
# f.close()


# json
# The standard module called json can take Python data hierarchies, and convert them to string representations; this process is called serializing.