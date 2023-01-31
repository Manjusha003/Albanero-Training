#An iterator is an object that contains a countable number of values.
#an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().

#Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.
# The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.

# The __next__() method also allows you to do operations, and must return the next item in the sequence.



#All these objects have a iter() method which is used to get an iterator



class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        print(self.index)
        return self.data[self.index]
    def hello(self):
        print("Hello")


r1= Reverse("Hello")
r1.hello()
print(r1.__iter__())
print(r1.__next__())

#list
for element in [1, 2, 3]:
    print(element)

#tuple
for element in (1,2,3):
    print(element*2)


str="hello"
p=iter(str)
# print(p)
print(next(p))




class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))



#To prevent the iteration to go on forever, we can use the StopIteration statement.
#In the __next__() method, we can add a terminating condition to raise an error if the iteration is done a specified number of times:



class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)
