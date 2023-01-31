# import os

# print(os.getcwd())


# import shutil



#The glob module provides a function for making file lists from directory wildcard searches:

# import glob
# p=glob.glob('.py')
# print(p)


# import sys
# print(sys.argv)


# import argparse

# parser = argparse.ArgumentParser(prog = 'top',
#     description = 'Show top lines from each file')
# parser.add_argument('filenames', nargs='+')
# parser.add_argument('-l', '--lines', type=int, default=10)
# args = parser.parse_args()
# print(args)



# string pattern matching
#The re module provides regular expression tools for advanced string processing. For complex matching and manipulation, regular expressions offer succinct, optimized solutions

import re
regex=re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
print(regex)

r1=re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
print(r1)

#When only simple capabilities are needed, string methods are preferred because they are easier to read and debug:

str='tea for too'.replace('too', 'two')
print(str)



# random module

import random
r1=random.choice([1,2,3,4,5,6])
print(r1)


r2=random.sample(range(100), 5) # sampling without replacement
print(r2)

r3=random.random()    # random float
print(r3)

r4=random.randrange(6)  # random integer chosen from range(6)
print(r4)


#The statistics module calculates basic statistical properties (the mean, median, variance, etc.) of numeric data:
import statistics
data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
mean=statistics.mean(data)
print(mean)

median=statistics.median(data)
print(median)

variance=statistics.variance(data)
print(variance)




# dates are easily constructed and formatted
from datetime import date
now = date.today()
print(now)

d1=now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
print(d1)

birthday = date(1990,3,11)
print(birthday)
age = now.year - birthday.year
print(age)



# Data Compression

#Common data archiving and compression formats are directly supported by modules including: zlib, gzip, bz2, lzma, zipfile and tarfile.

import zlib
str=b'witch which has which witches wrist watch'
print(len(str))

t = zlib.compress(str)
print(len(t))



def average(values):
    """Computes the arithmetic mean of a list of numbers.

   print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
doctest.testmod()   # automatically validate the embedded tests
print(average([90,70,20]))