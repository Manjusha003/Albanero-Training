#Python is an object oriented programming language.Almost everything in Python is an object, with its properties and methods.
#A Class is like an object constructor, or a "blueprint" for creating objects

# create class

class myClass:
    a=20

#create Object
obj1=myClass()
print(obj1.a)

#assigning values to the attributes
obj1.name="Manjusha"
obj1.age=21

print(obj1.name)
print(dir(obj1))

#The __init__() Function
#instance method or dunder method or magic method
# it wil call automatically for every object once. 
#To understand the meaning of classes we have to understand the built-in __init__() function.

#All classes have a function called __init__(), which is always executed when the class is being initiated.

#Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

#The __init__() function is called automatically every time the class is being used to create a new object.

class Student:
  def __init__(self):
    self.color=None
    self.brand=None


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)


class Student:
  def __init__(self,name,roll):
    self.name=name
    self.roll=None   # by default None
    self.age=None

s1=Student("Manjusha",100)
print(s1.name,s1.roll,s1.age)



# default attribute name
class Student:
  def __init__(self,age,name="Manjusha Raut"):
    self.age=age
    self.name=name


s1=Student(30)
print(s1.name,s1.age)


   


#The __str__() Function
#The string representation of an object WITH the __str__() function
# The __str__() function controls what should be returned when the class object is represented as a string.

# If the __str__() function is not set, the string representation of the object is returned:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)

# The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.

# Object Methods
# Objects can also contain methods. Methods in objects are functions that belong to the object.

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    self.isPresent=False

  def myfunc(self):
    print("Hello my name is " + self.name)

  def student_presenty(self):
    if self.isPresent:
      print("Student is present in the class")
    else:
      print("Student is absent")


p1 = Person("John", 36)
p2=Person("Ruhii",21)
p2.isPresent=True
p2.student_presenty()
p1.myfunc()


#Namespaces are created at different moments and have different lifetimes. The namespace containing the built-in names is created when the Python interpreter starts up, and is never deleted. The global namespace for a module is created when the module definition is read in; normally, module namespaces also last until the interpreter quits.
#namespaces
#A namespace is a mapping from names to objects.
# namespace is the area where you create and store the object/variables
# 1. class namespace
# 2.object/isinstance namespace

#The local namespace for a function is created when the function is called, and deleted when the function returns or raises an exception that is not handled within the function.

#Scopes and Namespaces Example
#This is an example demonstrating how to reference the different scopes and namespaces, and how global and nonlocal affect variable binding



def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)


#Delete Object Properties
#You can delete properties on objects by using the del keyword:


# Delete Objects
# You can delete objects by using the del keyword:

# del p1


# The pass Statement
# class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.

class myFisrtClass:
   pass


#the class inheritance mechanism allows multiple base classes, a derived class can override any methods of its base class or classes, and a method can call the method of a base class with the same name





#scope
#if we really want to modify a global variable from inside a function? We can use the global keyword:
#A scope is a textual region of a Python program where a namespace is directly accessible
a = 0 #global
def my_function():
    global a # used to change the value of global variable
    a = 3  #local or functionl scope
    print(a)

my_function()

print(a)


#We may not refer to both a global variable and a local variable by the same name inside the same function



#There is also a nonlocal keyword in Python – when we nest a function inside another function, it allows us to modify a variable in the outer function from inside the inner function (or, if the function is nested multiple times, a variable in one of the outer functions).  If we use the nonlocal keyword, however, the variable must be defined, because it is impossible for Python to determine in which scope it should be created.



#If we use the global keyword, the assignment statement will create the variable in the global scope if it does not exist already.

a=80
def myfun():
   global d
   d=30
   print(d)

myfun()
print(d)





 #Class Objects
 #Class objects support two kinds of operations: attribute references and instantiation.
 #Class instantiation uses function notation. Just pretend that the class object is a parameterless function that returns a new instance of the class. For example (assuming the above class):
 #x = MyClass()

 #The instantiation operation (“calling” a class object) creates an empty object. Many classes like to create objects with instances customized to a specific initial state. Therefore a class may define a special method named __init__(), like this:
# class instantiation automatically invokes __init__() for the newly-created class instance.



# Instance Objects
#The only operations understood by instance objects are attribute references. There are two kinds of valid attribute names: data attributes and methods.
#Data attributes need not be declared; like local variables, they spring into existence when they are first assigned to.

class MyClass:
   pass

a=MyClass()

a.counter=1
while a.counter<10:
   a.counter=a.counter*2
   print(a.counter)


#The other kind of instance attribute reference is a method


# Class and Instance Variables
# instance varibale are diffrent for diffrent classes
# the varibales which we define inside the __init__() is called instance variable.
#instance variables are for data unique to each instance and 
# class variables(static variables) are for attributes and methods shared by all instances of the class:


class Dog:
  kind = 'canine'            # class variable shared by all instances
  def __init__(self, name):
        self.name = name    # instance variable unique to each instance

d1=Dog("Fido")
d2=Dog("Robin")
print(d1.kind)
print(d2.name)

Dog.kind="pet"  # To change the class variable value we can use the class name

print(d1.kind)


class Dog:
    tricks = []             # mistaken use of a class variable
    def __init__(self, name):
        self.name = name
    def add_trick(self, trick):
        self.tricks.append(trick)

d=Dog("Tomy") 
print(d.name)
m=d.add_trick("roll over")
print(m) # None
print(d.tricks)  #['roll over']



# methods
# 1. class method : when we want to work with the class variables we use the class methods.
# 2. static method -> If we want to do some extra things at that time we use static methods
# 3. instance method ->used for instance variables
    # 1. accessor ->Fetching the values
    # 2. mutator -> Modifying the values


class Marks:
   total_marks=200
   name="Manjusha"

   def __init__(self,m1,m2,m3):
      self.m1=m1
      self.m2=m2
      self.m3=m3

   def totalMarks(self):             # instance method
      return(self.m1+self.m2+self.m3)
   
   def get_m1(self):       # get the value(Accessor)
      return self.m1
   
   def set_m1(self,val):  # set the value (Mutator)
      self.m1=val
  
   @classmethod  # if we want to use method as a class method 
   def student_info(cls):
      return cls.name
   
   @staticmethod
   def info():
      print("Hello, I'm Staic method")

s1=Marks(20,20,30)
print(s1.totalMarks())

print("Hello I'm  class method",Marks.student_info())  # class method
Marks.info()



# Private varibales


class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)
    
    __update = update   # private copy of original update() method


class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)

