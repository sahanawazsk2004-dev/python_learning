# string formating
template = "dear {}, you are awesome. take this {}$  shoe "
a = 'snz'
a1 = 1000
b = 'kdj'
b1 = 10000
c = 'ajit'
c1 = 100

s1 = template.format(b,b1)
print(s1)
# best way
print(f" dear {a} you are awesome). take this {a1}$ shoe")