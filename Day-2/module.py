#A module is a file containing Python definitions and statements

def fibo(n):
    a,b=0,1
    while a<n:
        print(a,end=",")
        a,b=b,a+b
    print()



def fib(n):
    res=[]
    a,b=0,1
    while a<n:
        res.append(a)
        a,b=b,a+b
    return res

# print(fib(10))
