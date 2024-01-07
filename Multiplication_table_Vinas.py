X = eval(input("Enter any number"))
o = ""

for a in range(1, (X + 3)):
	# Vertical
	for b in range(1, (X + 1)):
		
		# Horizontal
		o += str(a * b) + "\t"
	o += "\n"
print(o)
		