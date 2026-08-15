#GLOBAL KEYWORD
# excesive use is discourage and debugging harder
def sum(a,b):
    print("i like you")
    c = a+b
    global z # please modify global z
    z = 0      # this will refers to global z and not create  a lovcal variable 
    return c

z = 12
print(sum(34,65))
print(z)