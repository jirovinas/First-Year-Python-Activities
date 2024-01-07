b = 10
o = ""

for i in range(b):
    if i < (b / 2):
        for j in  range(i):
            o += " * " 
    else:
        for j in range(b - i):
            o += " * "
    o += "\n"
print(o)

c = 5
d = 1

for h in range(0,2*c):
 if h<4:
    print(('*' *d))
    d = d+1
else:
    print(('*' *d))
    d = d-1

for i in range (1,6):
    for j in range(1,6-i+1):
        print ("*" , end="")
    print()