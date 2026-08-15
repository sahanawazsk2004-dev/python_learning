#list method
Grocery = ["rice","dal","wheat","egg","maggie"]
print(Grocery)
Grocery.append("salt") #append -> add new element at last of list
print(Grocery)
Grocery.pop() #pop ->remove last element of list
print(Grocery)
Grocery.remove("egg") #remove ->delete the element in list,work on value not index
print(Grocery)
Grocery.reverse() #reverse the element of list
print(Grocery)
Grocery.insert(4,"oil") #inser new element in list
print(Grocery)
extra_Grocery = ["sauce","milk","masala"]
Grocery.extend(extra_Grocery) # add two list
print(Grocery)
Grocery.sort()  #sort -> rearange ,string- alphabatically ,integer--increasing order
print(Grocery)
print(Grocery.count("oil")) #count-- show repetation
