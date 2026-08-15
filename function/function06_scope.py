def sum(a,b): 
# a,b are local variables
# variable are not store in memory,after function return ,variable are wiped out
# acces variable with in the function ,we can not access it from anywhere -:>print(a)    
    c = a+b
    z = 1 # creates local variable->z,which is destroy bafter return
    return c
z = 7  #z is global variable,out side function,acces from every where
print(sum(4,8))
print(z)
