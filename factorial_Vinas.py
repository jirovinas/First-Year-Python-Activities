num = int(input("Enter a number: "))
a = 0
b = 1
sum = 0
while num <= 0:
	print('please enter number greater than 0')
else:
	print("\nthe serries of",num,"is")
	
	for x in range(0, num):
		print(sum, end=" ")
		a = b
		b = sum
		sum = a + b


num = 0

num = int(input("\n\nEnter a number: "))

factorial = 1

if num < 0:
   print("Invalid")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for x in range(1,num + 1):
       factorial = factorial*x
   print("The factorial of",num,"is",factorial)