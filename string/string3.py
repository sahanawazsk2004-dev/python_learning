
"""
name = 'sahanawaz'  # string are immutabable
#name[0] = 'R' # we can ot do this -> this is A  runtime error

a = len(name)
print(a)
"""
#string method
k = 'sharuk khan'
print(k.upper())
print(k.lower())
print(k.capitalize())
print(k.title())
print()
s = '  hrithik roshan  '
print(s.strip())
print(s.lstrip())
print(s.rstrip())
print()
j = 'python is amazing'
print(j.find("is"))   #return index of first occurence
print(j.replace("amazing","outstanding"))
print()
text = 'apple,banana,strawberry'
print(text.split(","))
print(",".join(['apple,banana,strawberry']))
print()
g = 'kdj143'
print(g.isalpha())
print(g.isdigit())
print(g.isalnum())
print(g.isspace())