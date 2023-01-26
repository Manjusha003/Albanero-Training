#two ways of writing values: expression statements and the print() function. (A third way is using the write() method of file objects


#To use formatted string literals, begin a string with f or F before the opening quotation mark or triple quotation mark.
#Inside this string, you can write a Python expression between { and } characters that can refer to variables or literal values.
year=1989
name="Tony"
print(f'my name is {name} and the year is {year}')
print(str(name))


# The str.format() method of strings requires more manual effort. You’ll still use { and } to mark where a variable will be substituted and can provide detailed formatting directives, but you’ll also need to provide the information to be formatted.




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


def fun():
    print("hello")