#A set is an unordered collection with no duplicate elements

#set() function can be used to create sets. 
#to create an empty set you have to use set(), not {}

# set=set()
# print(set)

# set={"apple","banana","orange","pineapple"}
# print(set)

# set={"apple","banana","orange","pineapple","apple","grapes","kiwi","banana"} #remove duplicate values
# print(set)

# check="apple" in set
# print(check)
# check1="Pineapple" in set
# print(check1)


# a=set("abhdfsghatwaj") # remove duplicate letters
# b=set("abdsghhdhsry")
# print(a)
# print(b)
# print(a-b) # print those which are not present in b
# print(b-a) # print those which are not present in a

# print(a|b) # letters in a or b or both
# print(a & b) # letters in  both a and b
# print(a^b)   #letters in a or b but not both



# a = {x for x in 'abracadabra' if x not in 'abc'}
# print(a)

for x in 'abracadabra':
    if x not in 'abc':
        print(x,end=",")