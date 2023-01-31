# Generators are a simple and powerful tool for creating iterators. They are written like regular functions but use the yield statement whenever they want to return data.
#Each time next() is called on it, the generator resumes where it left off (it remembers all the data values and which statement was last executed)
#Anything that can be done with generators can also be done with class-based iterators 
#What makes generators so compact is that the __iter__() and __next__() methods are created automatically.

#Some simple generators can be coded succinctly as expressions using a syntax similar to list comprehensions but with parentheses instead of square brackets

def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]


for char in reverse('golf'):
    print(char)




square_sum=sum(i*i for i in range(10))
print(square_sum)


keys=["name","class","age"]
values=["Manjusha","Bcs",22]
res = dict(map(lambda i,j : (i,j) , keys,values))
print(res)