# Abstraction is the concept in object-oriented programming that is used to hide the internal functionality of the classes from the users. 
# Abstraction is implemented using the abstract classes. An abstract class in Python is typically created to declare a set of methods that must be created in any child class built on top of this abstract class. Similarly, an abstract method is one that doesn't have any implementation.
#abstraction helps us make everything more user-friendly and less complex.
#The module we can use to create an abstract class in Python is abc(abstract base class) module.
#A class containing one or more than one abstract method is called an abstract class.

# the function which having only declaration  not defination is known as abstract  method

# from abc import ABC,abstractmethod


# class Computer(ABC):
#     @abstractmethod
#     def process(self):
#         pass

# class Laptop(Computer):
#     def process(self):
#         print("Process is running")

#     def computer_name(self):
#         print("my name is Manju")

# c1=Laptop()
# c1.process()
# c1.computer_name()






# # from abc import ABC, abstractmethod
# from math import pi

# class Shape(ABC):
#     def __init__(self, shape_name):
#         self.shape_name = shape_name
    
#     @abstractmethod
#     def draw(self):
#         pass
#     @abstractmethod
#     def create(self):
#         pass

# class Circle(Shape):
#     def draw(self):
#         print("draw method")
#     def create(self):
#         return super().create()
#     def area_of_circle(self):
#         return pi*self.shape_name**2

# s1=Circle(8)
# a1=s1.area_of_circle()
# print(a1)





from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, shape_name):
        self.shape_name = shape_name
    
    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def __init__(self):
        super().__init__("circle")
 
    def draw(self):
        print("Drawing a Circle")


c1=Circle()
c1.draw()