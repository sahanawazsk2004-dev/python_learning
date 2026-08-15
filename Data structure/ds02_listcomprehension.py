# list comprehension
# create a list containing table of 5
table = []
for i in range(1,11):
    table.append(5*i)

print(table)
print()
#shortcut method/way
table = [5*i for i in range(1,11)]
print(table)
print()

squared = [x**2 for x in range(5) ]
print(squared)