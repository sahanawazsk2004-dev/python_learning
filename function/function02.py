# positional ARGUMENTS
def add(a,b):   #(a,b) -> here this are parameters ,it is also called as positional arguments
    return a+b

c = add(7,8) #  -> the technical values that are passed are called arguments
print(c)

print()

# default arguments
def add(a,b,plus=0):   # here plus is default argument,default argument write after positional value  
    return a+b+plus

c = add(7,8,9)
print(c)

#keywoprd arguments  -> here order are not neccessaryg
def student(name,age):
    print(f"Name:{name}, Age:{age}")

student(age=25,name="sahanawaz")    