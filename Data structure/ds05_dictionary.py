#dictionary -- key value pair
#Dictionary-->write-->{}

marks = {"sk":80,"kdj":52,"ajit":65}
print(marks,type(marks))
print(marks["sk"])
marks["kdj"] = 60
print(marks)
print()
print()
#DICTIONARY METHOD 
'''
print(marks.keys()) #show keys
print(marks.values()) #show value

marks.pop("kdj") #remove key value oair of kdj
print(marks)

#marks.clear() #it clears all key-value pair
#print(marks)

print(marks.get("kdj","not present")) #key value pair not present show not present

marks.update({"sk":92}) #update the value of sk (key value pair)
print(marks)

marks.popitem() #remove last key value pair
print(marks)
print()
marks.items() #show key value pair
print(marks)
'''
marks = marks.fromkeys(marks.keys(),30) #it create new dictionary where all key have same value
print(marks)

marks2 = {"sk":80,"kdj":52,"ajit":65} #copy the element of the dictionary
new_marks = marks2.copy()
print(new_marks)
new_marks.update({"sk":85})
print(new_marks)