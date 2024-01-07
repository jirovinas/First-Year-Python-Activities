x = eval(input("enter a number"))
n1 = 5
n2 = 4
n3 = 3
n4 = 2
n5 = 1
count = 0
fibo = 0
while count < x:
	print(n1, " ")
	print(n2, " ")
	print(n3, " ")
	print(n4, " ")
	print(n5, " ")
	fibo = n1 ** n2
	fibo = n2 ** n3
	fibo = n3 ** n4
	fibo = n4 ** n5
	n1 = n2
	n2 = n3
	n3 = n4
	n4 = n5
	n5 = fibo 
	fibo = n1 * n2 * n3 * n4 * n5
	count += 1
	print(fibo)


	