
# A module is a file containing Python definitions and statements
# function classes varibales can be imported from one module to another module


#import demo
#This does not enter the names of the functions defined in fibo directly in the current symbol table; it only enters the module name fibo there. Using the module name you can access the functions:
#demo.check_prime()
#demo.check_num()
#demo._sum(9,8)

#There is a variant of the import statement that imports names from a module directly into the importing module’s symbol table. For example:

# from demo import check_num,check_prime,_sum  #using this we can import only thoes functions or classes or varibales which you want and use it directly

# check_prime()
# check_num()
# _sum()


#from demo import *
#This imports all names except those beginning with an underscore (_). In most cases Python programmers do not use this facility since it introduces an unknown set of names into the interpreter, possibly hiding some things you have already defined.

# check_num()
# check_prime()
##_sum()  It is not able to access this function


#import demo as d
#If the module name is followed by as, then the name following as is bound directly to the imported module
# d.check_num()
# d.check_prime()

# from demo import check_prime as isPrime
# isPrime()

# __name__ it will change the value where it is used.

# import calc
# print(__name__)


# To speed up loading of the modules, Python caches the compiled version of each module in the folder __pycache__ under the name <module_name>.version.pyc where the version encodes the format of the compiled file; and it generally contains the python version number. This naming convention allows compiled modules from different releases and different versions to co-exist.

# Python checks the modification date of the source against the compiled version to see if it’s out of date and needs to be recompiled. This is a completely automatic process. Also, the compiled modules are platform-independent, so the same library can be shared among systems with different architectures.

# import sys
# print(dir(sys.path))

# import builtins
# print(dir(builtins))


#The Module Search Path

# import sys
# from pprint import pprint 
# pprint(sys.path)

# import sys
# print(sys.path)
#


# Packages are a way of structuring Python’s module namespace by using “dotted module names”.
#Packages are collections of modules and we can access modules inside them using the dot(.) notation.




