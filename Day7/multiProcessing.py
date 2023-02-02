# Multiprocessing is a system that has more than one or two processors. In Multiprocessing, CPUs are added for increasing computing speed of the system.
 #Process ->start()=>process will started and return the output
# join() => It will terminate the process

#Lock




# from multiprocessing import Process

# def print_name():
#     print("Hello")

# if __name__ == '__main__':
#     proc=Process(target=print_name)
#     proc.start()
#     proc.join()

#     print("Bye")



# from multiprocessing import Process
# from time import sleep

# def find_square(num):
#     for i in num:
#         print("Square :",i*i)
#         sleep(3)


# def find_cube(num):
   
#     for i in num:
#         print("Cube :",i*i*i)
#         sleep(3)

# if __name__ == '__main__':
#   arr=[2,4,5,3,6]
#   p1=Process(target=find_square,args=(arr,))
#   p2=Process(target=find_cube,args=(arr,))

#   p1.start()
#   p2.start()
#   p1.join()
#   p2.join()
#   print("Process completed")


# The Process class

# from multiprocessing import Process

# def f(name):
#     print('hello', name)

# if __name__ == '__main__':
#     p = Process(target=f, args=('Rony',))
#     p.start()
#     p.join()


# from multiprocessing import Process
# sum=[]
# def calc_sum(num):
#     global sum
#     s=0
#     print("Sum of the numbers in given range")
#     for i in num:
#       s+=i
#       sum.append(s)
#     print(sum)

# if __name__=='__main__':
#    num=[6,3,4,5,4,3]
#    p1=Process(target=calc_sum,args=(num,))
#    p1.start()
#    p1.join()

# print("Sum of array elements Done")


# # whenever process gets called/created it gets its own memory space


#  pool

# from multiprocessing import Pool

# def f(x):
#     return x*x

# if __name__ == '__main__':
#     with Pool(1) as p:
#         print(p.map(f, [1, 2, 3]))








# from multiprocessing import Process
# import os
# from time import sleep

# def info(title):
#     print(title)
#     print('module name:', __name__)
#     print('parent process:', os.getppid())
#     print('process id:', os.getpid())

# def f(name):
#     info('function f')
#     sleep(5)
#     print('hello', name)


# if __name__ == '__main__':
#     info('main line')
#     p = Process(target=f, args=('bob',))
#     p.start()
#     # p.join()

#     print("Hello")



# # Exchanging objects between processes

# Queues
# The Queue class is a near clone of queue.Queue. For example:
# queue are thread and process safe

# from multiprocessing import Process, Queue

# def f(q):
#     q.put([42, None, 'hello'])

# if __name__ == '__main__':
#     q = Queue()
#     p = Process(target=f, args=(q,))
#     p.start()
#     print(q.get())    # prints "[42, None, 'hello']"



# Pipes

# The Pipe() function returns a pair of connection objects connected by a pipe which by default is duplex (two-way). For example:

# from multiprocessing import Process, Pipe

# def f(conn):
#     conn.send([42, None, 'hello'])
#     conn.close()

# if __name__ == '__main__':
#     parent_conn, child_conn = Pipe()
#     p = Process(target=f, args=(child_conn,))
#     p.start()
#     print(parent_conn.recv())   # prints "[42, None, 'hello']"
#     p.join()





# from multiprocessing import Process
# from time import sleep

# def CreateObj(obj):
#     sleep(3)
#     print(obj)
    

# if __name__ == '__main__':
#     person={'name':"Tony",'age':30,"roll":200}
#     p1=Process(target=CreateObj,args=(person,))
#     p1.start()
#     # p1.join()
#     print("Hello") 




# class MyObject:
#     def __init__(self, name):
#         self.name = name

#     def worker(self, num):
#         print("Object name:", self.name)
#         print("Process number:", num)

# if __name__ == "__main__":
#     obj = MyObject("MyObject")

#     processes = []
#     for i in range(5):
#         p = Process(target=obj.worker, args=(i,))
#         processes.append(p)
#         p.start()

#     for p in processes:
#         p.join()




import multiprocessing

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def worker(self, num):
        print("Person name:", self.name)
        print("Person age:", self.age)
        print("Process number:", num)

if __name__ == "__main__":
    person = Person("John Doe", 30)

    processes = []
    for i in range(5):
        p = multiprocessing.Process(target=person.worker, args=(i,))
        processes.append(p)
        p.start()

    # for p in processes:
    #     p.join()


    print("Hello")