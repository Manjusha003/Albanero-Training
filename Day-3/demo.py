
def check_num():
    num=int(input("Enter any number :"))

    if num%2==0:
        print(num, "is even")
    else:
        print(num, "is odd")


if __name__=='__main__':
   check_num()



# program to check prime

def check_prime():
    num=int(input("Enter any number :"))
    flag=True
    for i in range(2,num):
        if num%i==0:
            flag=False
            break
    if flag:
      print(num, "is prime")
    else:
        print(num," is not prime")

if __name__=='__main__':

    check_prime()


def _sum(a,b):
    print(a+b)


if __name__=='__main__':

   _sum(7,9)



