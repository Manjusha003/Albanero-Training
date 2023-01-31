## 
# An interface is an abstract class which contain only abtartct methods not the concrete methods/normal methods.
# all methods of an interface are abstract.
# we can not create the object of interface
# If a class is implementing  an interface it has to define all the methods given in that interface

# if class does not implement all the methods declared in the interfaces the calss must be declared as the abstartct class.

# we use interface when all the features need to be implemented differenlty for different object

from abc import ABC,abstractmethod
class School(ABC):
    @abstractmethod
    def name(self):
        pass

class ClassS(School):
    def name(self):
        print("My name is Manjusha")


c1=ClassS()
c1.name()


# inheritance +interfaces

from abc import ABC,abstractmethod
class School(ABC):
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def roll(self):
        pass

class ClassS(School):
    def name(self):
        print("My name is Manjusha")

class Roll(ClassS):
    def roll(self):
       print("My roll is 1000")

c1=Roll()
c1.name()
c1.roll()
