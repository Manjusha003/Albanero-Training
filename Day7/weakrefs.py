#To create weak references in python, we need to use the weakref module. The weakref is not sufficient to keep the object alive. A basic use of the weak reference is to implement cache or mappings for a large object.



# Class weakref.ref(object[, callback])
# It will return a weak reference to the object. When the referent is still alive, the actual object can be retrieved by calling the reference object, but when the actual object is not present, it will return None.

# Method weakref.proxy(object[, callback])
# This method is used to return a proxy for the object, which are using weak reference. The returned object may be either ProxyType or CallableProxyType.

# Method weakref.getweakrefcount(object)
# This method is used to return the number of weak references and proxies of the objects.

# Method weakref.getweakrefs(object)
#This method is used to return a list of weak references and proxies objects.


import weakref
class my_list(list):
   pass
new_list = my_list('String') #Use my_list class to define a list
print(new_list)
weak_ref = weakref.ref(new_list)
new_weak_list = weak_ref()
print(new_weak_list)
new_proxy = weakref.proxy(new_list)
print(new_weak_list)
print('The object using proxy: ' + str(new_proxy))
if new_list is new_weak_list:
   print("There is a weak reference")
print('The Number of Weak references: ' + str(weakref.getweakrefcount(new_list)))
# del new_list, new_weak_list #Delete both objects
print("The weak reference is: " + str(weak_ref()))

print(weakref.getweakrefs(my_list))




# import weakref
# class myClass(list):
#    pass
# c1=myClass("Manjusha")
# print(c1)
# new_weak_list1 = weak_ref()
# print(new_weak_list1)
# print(str(weakref.getweakrefcount(c1)))
# print(str(weakref.getweakrefs(c1)))