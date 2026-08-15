#set operation
a = {23,14,56,17}
b = {12,23,17,18,30}

c = a.union(b) #union--add both set element but no duplicate
print(c)
print()

d = a.intersection(b) #only common element
print(d)

e = a.difference(b) #element that present in a but not in b
print(e)

#set best for removing duplicate value means we use set where duplicate value not required