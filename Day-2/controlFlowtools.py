# if statement
# age = int(input("Please enter your age: "))
# if age<18:
#     print("you can't vote")
# else:
#     print("you can vote")


# x = int(input("Please enter your age: "))
# if x<0:
#     print("number is negative")
# elif x==0:
#     print("number is zero")
# else:
#     print("number is positive")


#for Statements

# list=["cat","dog","bat","rat","mat"]
# for i in list:
#     print(i)


# list=["chatterbox","dog","batman","rat","mat"]
# for i in list:
#     print(i,end=',')    



# for i in list[:]:  # Loop over a slice copy of the entire list.
#      if len(i) >5 :
#         list.insert(0, i)
# print(list)
 


# range()
# for i in range(5):
#    print(i)
 

# for i in range(1,5): # 5 is excluding
#    print(i)
 
#even numbers
# for i in range(0,10,2):
#     print(i)


# for loop on string
# str="manjusha"
# for i in str:
#     print(i)



# a = ['Mary', 'had', 'a', 'little', 'lamb']
# for i in range(len(a)):
#     print(i, a[i],len(a[i]))

# print(range(10)) # output--->range(0, 10)



# print(list(range(5))) # it create the list


#break
#prime numbers

# for n in range(2, 10):
#    for x in range(2, n):
#       if n % x == 0:
#          print(n, 'equals', x, '*', n//x)
#          break
#    else:
#       print(n, 'is a prime number')


#continue
# print even and odd numbers
# for num in range(2, 10):
#    if num%2==0:
#       print("even number :",num)
#       continue
#    print("odd number ",num)


for num in range(10,20):
       if num==15:
         continue
       print(num)
      

# pass statement

#The pass statement does nothing. It can be used when a statement is required syntactically but the program requires no action.

# while True:
#     pass

#This is commonly used for creating minimal classes:

# class MyFirstClass:
#      pass

#pass can be used is as a place-holder for a function or conditional body when you are working on new code
# def initlog(*args):
#    pass   



