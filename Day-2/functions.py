#function

# def fibo(n):
#     a,b=0,1
#     while a<n:
#         print(a,end=' ')
#         a,b=b,a+b

# fibo(10)



# # return

# def fib(n):
#    a,b=0,1
#    res=[]
#    while a<n:
#       res.append(a)
#       a,b=b,a+b
#    return res
# print(fib(20))


#4.7.1. Default Argument Values

# def sum(a,b=8,c="something went wrong"):
#     while True:
#         ok=input(a)
#         if ok in ('y','ye','yes'):
#             return True
#         if ok in('n','no','nop','nope'):
#             return False
#         b=b-1
#         if b<0:
#             raise ValueError('invalid user response')
#         print(c)
# sum("are you ok?",7)

## varibale

# i=10
# def fun(arg=i):
#     print(arg)

# i=20
# fun() #10


## list

# def fun(a,list=[]):
#     list.append(a)
#     return list

# print(fun(78)) #[78]
# print(fun(88)) #[78, 88]
# print(fun(8))  #[78, 88,8]



#If you don’t want the default to be shared between subsequent calls, you can write the function like this instead:


# def fun(a,list=None):
#     if list is None:
#         list=[]
#     list.append(a)
#     return list

# print(fun(66)) #[66]
# print(fun(77)) #[77]


#Keyword Arguments

# def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
#     print("-- This parrot wouldn't", action, end=' ')
#     print("if you put", voltage, "volts through it.")
#     print("-- Lovely plumage, the", type)
#     print("-- It's", state, "!")


# parrot(1000)                                          # 1 positional argument
# parrot(voltage=1000)                                  # 1 keyword argument
# parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
# parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
# parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
# parrot('a thousand', state='pushing up the daisies')  # 1 positional and 1 keyword arguments




# def fun(value,*arguments,**keywords):
#     print("Do you have ?", value)
#     print("can you give me that",value)
#     for arg in arguments:
#         print(arg)

#     print("-" * 40)

#     for key in keywords:
#         print(key,":",keywords[key])

# fun("Pen","happy","sad","good",
#     name="manjusha",
#     clas="BCS",
#     age=22)



 #Arbitrary Argument Lists

#Any formal parameters which occur after the *args parameter are ‘keyword-only’ arguments, meaning that they can only be used as keywords rather than positional arguments.

def fun(*value,separator="/"):
    return separator.join(value)

print(fun("welcome","Same","start","today"))



# def write_multiple_items(file, separator, *args):
#     file.write(separator.join(args))

# write_multiple_items("hello","/","bye","hello","help")


 #Unpacking Argument Lists

# args=[2,9]
# a=list(range(*args)) 
# print(a) #[2, 3, 4, 5, 6, 7, 8]


# p=list(range(2, 9)) 
# print(p)     #[2, 3, 4, 5, 6, 7, 8]

# d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
#print(d)



#lambda expression

 #Lambda functions can be used wherever function objects are required
pairs = [(1, 'one'), (6, 'two'), (7, 'three'), (3, 'four')]
pairs.sort(key=lambda pair: pair[0])
print(pairs)


def make_increment(n):
    return lambda x:x+n

res=make_increment(56)
print(res(1))

 #Documentation Strings

# def fun():
#     """ Welcome to albanero
#     This is python tutorial"""
#    

# print(fun.__doc__)