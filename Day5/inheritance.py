# single level inheritance:


# subclass can access all the features of the super class but super class can not access the properties of subclass
class A:
    def firstA(self):
        print("class A of method firstA")
    def secondA(self):
        print("class A of method secondA")
    def thirdA(self):
        print("Class A of method thirdA")

class B(A):
    def firstB(self):
        print("class B of method firstB")
    def secondB(self):
        print("class B of method secondB")



b1=B()
b1.firstA()
b1.firstB()
b1.secondA()
b1.secondB()



# multi level inheritance

class A:
    def firstA(self):
        print("class A of method firstA")
    def secondA(self):
        print("class A of method secondA")
    def thirdA(self):
        print("Class A of method thirdA")

class B(A):
    def firstB(self):
        print("class B of method firstB")
    def secondB(self):
        print("class B of method secondB")


class C(B):
    def firstC(self):
        print("class C of method firstC")
    def secondC(self):
        print("class C of method secondC")


c1=C()
c1.firstC()
c1.firstA()
c1.secondC()
c1.firstB()


# multiple inheritance
class A:
    def firstA(self):
        print("class A of method firstA")
    def secondA(self):
        print("class A of method secondA")
    def thirdA(self):
        print("Class A of method thirdA")

class B:
    def firstB(self):
        print("class B of method firstB")
    def secondB(self):
        print("class B of method secondB")


class C(A,B):
    def firstC(self):
        print("class C of method firstC")
    def secondC(self):
        print("class C of method secondC")


c1=C()
c1.firstC()
c1.firstA()
c1.secondC()
c1.firstB()



