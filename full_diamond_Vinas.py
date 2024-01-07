x = 7
y = int(7)

for i in range(0,7):
    for x in range(y-i):
        print(' ', end='')
    

    for x in range(2*i-1):
        print('*',end='')
    print()
for i in range(y,0,-1):
    for x in range(y-i):
        print(' ', end='')
    
    for x in range(2*i-1):
        print('*',end='')
    print()