
#Contructor: It will automatically called when we create the object of the class.
# This __init__() automatically called depends on which class object you are calling.
# If you want to call the another/super class __init__() then we have to write super().__init__()
# inside the __init__() of called class object




class School:
    def __init__(self):  # contructor 
       print("init of School class")
    
    def school_name(self):
        print("YMIT")


class Teacher(School):
    def __init__(self):  # contructor 
       super().__init__()
       print("init of Teacher class")
    

class Student(Teacher):
    def __init__(self) :
        super().__init__()
        
        print("init of Student class")

    def myName(self):
        print("My name is Manjusha")
        

s1=Student()
s1.myName()

