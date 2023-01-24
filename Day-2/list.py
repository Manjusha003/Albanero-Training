# methods of list

# list=[1,2,3,4,6,8]
# #print(list)
# list.append(9)
# #print(list)
# list[len(list):]=[11,12,13,14,2]
#print(list)

# list1=[6,8,9,0]
# list.extend(list1)
# print(list)


# list.insert(4,100) # list.insert(index,value)
# # print(list)
# list.remove(100)
# # print(list)

# #list.pop()  # remove last element
# #list.clear() # similar to del list[:]
# count=list.count(2)
# print(count)
# # list.reverse()
# list.copy()
# print(list)



# fruits=['apple', 'banana', 'banana', 'grape', 'apple', 'kiwi', 'orange', 'pear']
# ind=fruits.index('apple',2)
# count=fruits.count('banana')
# last=fruits.pop()
# fruits.sort()
# fruits.insert(3,'pineapple') 
# print(fruits)
# print(last)
# print(count)
# print(ind)



#Using Lists as Stacks

# stack=[5,0,2,4,7]
# stack.append(8) # insert element at end or top
# stack.append(88) 
# print(stack)

# stack.pop() # remove element from last or top
# print(stack)



#Using Lists as Queues

# from collections import deque

# queue = deque(["Eric", "John", "Michael","Rony","Stark"])
# queue.append("Tony")
# queue.append("Iron")
# queue.popleft()
# print(queue)


#List Comprehensions
#List comprehensions provide a concise way to create lists.

# squares=[]
# for i in range(10):
#     squares.append(i**2)
# print(squares)


# squares = list(map(lambda x: x**2, range(10)))
# squares = [x**2 for x in range(10)]

# print(squares)

# squares=[(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
# print(squares)


#num=[1,-2,3,-4,5]
# pw=[i**2 for i in num]
# print(pw)

# abs=[abs(i) for i in num]
# print(abs)


# freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
# list=[weapon.strip() for weapon in freshfruit]
# print(list)

# list=[(x, x**2) for x in range(6)]
# print(list)


# flatten a list using a listcomp with two 'for'
# list=[[1,2,3],[3,4,5,6],[6,7,4]]
# list=[num for elem in list for num in elem]
# print(list)


# from math import pi
# list=[float(round(pi,i)) for i in range(1,6)]
# print(list)


matrix=[[1,2,3,4,5],[4,7,8,9,3],[6,8,3,1,9]]
# list=[[row[i] for row in matrix] for i in range(5)]
# print(list)


# transepose=[]
# for i in range(5):
#     transepose.append([row[i] for row in matrix])
# print(transepose)

# transepose=[]
# for i in range(5):
#     transrow=[]
#     for row in matrix:
#        transrow.append(row[i])
#     transepose.append(transrow)

# print(transepose)


# list=list(zip(*matrix))
# print(list)



#del statement
# list=[1,3,-9,3,1,5,6,48]
# del list[0]
# print(list)

# del list[2:4]
# print(list)

# del list[:]
# print(list)


# enumerate()
list=["manju","megha","vaishu"]

for i,value in enumerate(list):
    print(i,value)


