name = (input("Enter a Name: "))
print("Hi!",name, "welcome to the python programming please select what you want to learn about python\n")

def menu():
	print("[1] Printing in Python")
	print("[2] Variable Declaration in Python")
	print("[3] Operation in Python")
	print("[4] Condition in Python")
	print("[5] Looping in Python")
	print("[6] Functions in Python")
	print("[7] Array")
	print("[8] Dictionary")
	print("[0] Exit")

menu()
Option = int(input("Select Your option: "))
while Option != 0:
	if Option == 1:
		print("\nHi" ,name, "you select the Printing in Python\nThe print() function prints the specified message to the screen, or other standard output device.\nThe message can be a string, or any other object, the object will be converted into a string before written to the screen.\nExample: you want to print hello world you can type hello world inside of this print()\nThe output will be\thello world")
	elif Option == 2:
		print("\nHi" ,name, "you select the Variable Declaration in Python\nIn those languages, a variable's type has to be specified before it may be assigned to a value.\nThis process is called variable declaration. But in Python, we don't declare variables, we simply assign them.\nIn short, we can think of a variable in Python as a name for an object.\nExample: x=27, x is the variable and 27 is the value")
	elif Option == 3:
		print("\nHi" ,name, "you select the Operation in Python\nIn Python, operators are special symbols that designate that some sort of computation should be performed.\nThe values that an operator acts on are called operands.\nThere are 4 types of Operators\n1.Arithmetic Operators - use for computation.\n\tThe operators that use are + addition, - subtraction, * multiplication, / division, % modulos, // floor division, ** exponent\n2.Assignment Operators - assign values to variables.\n\tThe operators that use are > greater that, < less than, == equal to, != not equal to, >= greater than or equal to, <= less than or equal to\n3.Logical Operators - comparison\n\tThe operators that use are and, or, not\n4.Relational Operators - combine conditions\n\tThe operators that use are & bitwise and, | bitwise or, ~ bitwise not, ^ bitwise xor, >> bitwise right shift, << bitwise left shift")
	elif Option == 4:
		print("\nHi" ,name, "you select the Condition in Python\nConditional Statements pertains to the way that it gives condition into a program whether it is True or False,\nit is when the decision is made whether the program will run or execute, or not\nThe keywords of conditional statements are: if - which tells when the program will run if the condition is True\nelif or else if - which tells the program a secondary option if the condition is True\nElse which tells when the program will run if the condition is False\nExample:\n\tYou want to determine a number that is odd or even you can use if for odd elif for even and else for invalid")
		x = eval(input('Enter a number: '))
		y = x % 2
		if y == 0:
			print(x,"is a EVEN number")
		elif y == 1:
			print(y, "is a ODD number")
		else:
			print('INVALID')

		x = eval(input('Enter a number: '))
		y = x % 1
		if y == 0:
			print(x,"is a EVEN number")
		elif y == 1:
			print(y, "is a ODD number")
		else:
			print("INVALID")
	
	elif Option == 5:
		print("\nHi" ,name, "you select the Looping in Python\nA loop is a sequence of instruction s that is continually repeated until a certain condition is reached.\nTypically, a certain process is done, such as getting an item of data and changing it,\nand then some condition is checked such as whether a counter has reached a prescribed number.\nThere are 3 types of looping\n1.For Loop - the keywords that need in For Loop are for,in.\nAnd the requirements is how many  times to repeat and when to start.\n2.While Loop - the keywords in While Loop are while, continue, break\n3.Do While Loop\nExample of For Loop:\nfor x in range(1,11):")
		for x in range(1,11):
			print(x)
	elif Option == 6:
		print("\nHi" ,name, "you select the Functions in Python\nA function is a block of code which only runs when it is called.\nYou can pass data, known as parameters, into a function. A function can return data as a result.\nTo call a function, use the function name followed by parenthesis\nThe keywords use in functions are def and return and the requirements are name of function, parameter and return statement\nExample: you want to print hello world 5 times you can use function to make it easy\nlike this:")
		def hel():
			print("hello world")
		hel()
		hel()
		hel()
		hel()
		hel()
	elif Option == 7:
		print("\nHi" ,name, "you select the Array\nAn array is a special variable, which can hold more than one value at a time.\nExample: If you have a list of items (a list of car names, for example), storing the cars in single variables\nYou can array for that like this cars=[Ford,Volvo,BMW]\n\tAnd you can print all of that using print() inside of open and close parenthesis are the variable(car)")
		cars = ["Ford", "Volvo", "BMW"]
		print(cars)
	elif Option == 8:
		print("\nHi" ,name, "you select the Dictionary\nDictionaries are used to store data values in key:value pairs.\nA dictionary is a collection which is ordered*, changeable and do not allow duplicates.\nDictionaries are written with {}curly brackets, and have keys and values.\nExample: car={brand : Ford}\n\tThe brand is the key and Ford is the value")
		car = {"brand": "FORD"}
		print(car)
	else:
		print("Invalid")
	print()
	menu()
	Option = int(input("Select Your option: "))

print("\nThank you" ,name, "for listening, I hope you learn about python programming and Goodbye")
