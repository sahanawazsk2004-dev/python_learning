'''
#set -- unordered and unique(no duplicate element)
#set ->write -> {}
s = {2,34,56,67}
print(s,type(s))
print(s[3]) #we access it --> bcz it is unorderedgh
'''

#set method 
my_set = {1,24,56,78}
my_set.add(10) #add element at any position
print(my_set)
print()
my_set.remove(24) #remove element,if element not present it throws error
print(my_set)
print()
my_set.pop()
print(my_set) #it removes any element
my_set.discard(43546)
print(my_set) #element not present it does not throw error