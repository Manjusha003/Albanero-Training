# Multithredaing
# we can break down one task into multiple process and again this process break down into into small parts and this parts known as tread.
# Multithreading is a system in which multiple threads are created of a process for increasing the computing speed of the system. In multithreading, many threads of a process are executed simultaneously and process creation in multithreading is done according to economical


# threading.active_count()
# Return the number of Thread objects currently alive. The returned count is equal to the length of the list returned by enumerate().

# threading.current_thread()
# Return the current Thread object, corresponding to the caller’s thread of control. If the caller’s thread of control was not created through the threading module, a dummy thread object with limited functionality is returned.


# threading.excepthook(args, /)
# Handle uncaught exception raised by Thread.run().
# The args argument has the following attributes:

# exc_type: Exception type.
# exc_value: Exception value, can be None.
# exc_traceback: Exception traceback, can be None.
# thread: Thread which raised the exception, can be None.

# threading.get_native_id()
# Return the native integral Thread ID of the current thread assigned by the kernel. This is a non-negative integer. Its value may be used to uniquely identify this particular thread system-wide (until the thread terminates, after which the value may be recycled by the OS).


# threading.enumerate()
# Return a list of all Thread objects currently active. The list includes daemonic threads and dummy thread objects created by current_thread(). It excludes terminated threads and threads that have not yet been started. However, the main thread is always part of the result, even when terminated.


# threading.main_thread()
# Return the main Thread object. In normal conditions, the main thread is the thread from which the Python interpreter was started.

# threading.settrace(func)
# Set a trace function for all threads started from the threading module. The func will be passed to sys.settrace() for each thread, before its run() method is called.

# threading.gettrace()
# Get the trace function as set by settrace().



from time import sleep
from threading import *

class School(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)


class Student(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)

print("Bye1")
s1 = School()
s2 = Student()
s1.start()
s2.start()
s1.join()
s2.join()
print("Bye2")




import threading

def calc_square(num):
    print("calculate the squares of the numbers")
    for i in num:
        print("square:", i*i)
        sleep(0.2)


def calc_cube(num):
    print("calculate the cubes of the numbers")
    for i in num:
        print("cube:", i*i*i)
        sleep(0.2)
    

arr=[2,3,4,5,6]
# calc_cube(arr)
# calc_square(arr)

t1=threading.Thread(target=calc_square,args=(arr,))


t2=threading.Thread(target=calc_cube,args=(arr,))
print("Current Threads is",str(threading.current_thread()))
print("Threads count before starting t1 and t2 thread is ",threading.active_count())
print("Threads",threading.enumerate())
print("settrace ",threading.settrace(calc_square(arr,)))

t1.start()
t2.start()
print("Threads count is ",threading.active_count())
print("Current Threads is",str(threading.current_thread()))
print("the netive id is",threading.get_native_id())
print("Threads",threading.enumerate())
print("main thread",threading.main_thread())
print("gettrace method",threading.gettrace())

t1.join()
t2.join()
print("Task is Done")



sum=[]
def calc_sum(num):
    global sum
    s=0
    print("Sum of the numbers in given range")
    for i in num:
      s+=i
      sum.append(s)
    

if __name__=='__main__':
   num=[6,3,4,5,4,3]
   p1=threading.Thread(target=calc_sum,args=(num,))
   p1.start()
   p1.join()

print(sum)




# start()
# Start the thread’s activity.
# It must be called at most once per thread object. It arranges for the object’s run() method to be invoked in a separate thread of control.
# This method will raise a RuntimeError if called more than once on the same thread object.



# run()
# Method representing the thread’s activity.
# You may override this method in a subclass. The standard run() method invokes the callable object passed to the object’s constructor as the target argument, if any, with positional and keyword arguments taken from the args and kwargs arguments, respectively.


# Using list or tuple as the args argument which passed to the Thread could achieve the same effect.
from threading import Thread
t = Thread(target=print, args=[1,6,7])
t1 = Thread(target=print, args=(1,6,7))
t1.run()
t.run()


