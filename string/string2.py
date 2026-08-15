# string slicing
name = 'sahanawaz'
print(name[0:5])#goes 0 to 5-1 i.e 0 to 4
print(name[2:6])

#print(name[0:7:n])  #skip n-1 character
print(name[0:8:1]) #no character skip
print(name[0:8:2]) #1 character skip
print(name[0:8:3]) # 2 character skip

print(name[:8])  # replace first empty number with zero
print(name[0:])  # replace second empty number with string length