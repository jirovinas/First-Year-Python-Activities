sum = 0
count = 0
odd = ""
isContinue = True

while isContinue:
	num = eval(input("enter a number: "))

	if num % 3 == 0:
		count += 1
		sum += num
		odd = odd + str(num) + " ,"
	
	if num == 0:
	
		print("Zero has been pressed")
		print("there is", count, "numbers that are disivible to 3 and those number were ", odd, "the average is",sum/count)
		break
		isContinue = False