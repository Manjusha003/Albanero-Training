# Multiprocessing is a system that has more than one or two processors. In Multiprocessing, CPUs are added for increasing computing speed of the system. Because of Multiprocessing, There are many processes are executed simultaneously. Multiprocessing are classified into two categories:

# 1. Symmetric Multiprocessing
# 2. Asymmetric Multiprocessing 



# import multiprocessing
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
#   p1=multiprocessing.Process(target=find_square,args=(arr,))
#   p2=multiprocessing.Process(target=find_cube,args=(arr,))

#   p1.start()
#   p2.start()




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
#    p1=multiprocessing.Process(target=calc_sum,args=(num,))
#    p1.start()
#    p1.join()



# whenever process gets called/created it gets its own memory space


#  pool

# from multiprocessing import Pool

# def f(x):
#     return x*x

# if __name__ == '__main__':
#     with Pool(1) as p:
#         print(p.map(f, [1, 2, 3]))



# The Process class

# from multiprocessing import Process

# def f(name):
#     print('hello', name)

# if __name__ == '__main__':
#     p = Process(target=f, args=('Rony',))
#     p.start()
#     p.join()





# from multiprocessing import Process
# import os

# def info(title):
#     print(title)
#     print('module name:', __name__)
#     print('parent process:', os.getppid())
#     print('process id:', os.getpid())

# def f(name):
#     info('function f')
#     print('hello', name)

# if __name__ == '__main__':
#     info('main line')
#     p = Process(target=f, args=('bob',))
#     p.start()
#     p.join()



# Exchanging objects between processes

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

from multiprocessing import Process, Pipe

def f(conn):
    conn.send([42, None, 'hello'])
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    p.start()
    print(parent_conn.recv())   # prints "[42, None, 'hello']"
    p.join()

