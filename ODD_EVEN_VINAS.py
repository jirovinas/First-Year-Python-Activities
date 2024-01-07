x = eval(input('Enter a number: '))

last = x % 10
print('the last digit of',x,'is',last)
if last % 2 == 0:
    square = last ** 2
    print(last,'is an even number and the sqaure of ',last,'is',square)

elif last % 2 == 1:
    cube = last ** 3
    print(last,'is an ODD number and the cube of ',last,'is',cube)

else:
    print('INVALID')