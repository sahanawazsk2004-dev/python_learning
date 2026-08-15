#LIST
"""
list order mutable collection of item
list ->write->[    ]
list include int,string,float,boolean --> multiple data types

"""
marks = [45.5,34,23.7,90.6,67]
mixed = ["sk",81,63.5,False]   # includes multiple data types

print(marks,type(marks))
print(mixed)

print(mixed[2])
print(marks[-2])

print(marks[2:4])
print(mixed[5]) #ti show error,error index out of bound