def custom_customs(input_file):
	file = open(input_file, "r")
	sum = 0
	groupAnswered = [0] * 26
	for x in file:
		if x == '\n':
			for z in groupAnswered:
				if z == 1:
					sum += 1
			groupAnswered = [0] * 26
			print("sum: ", sum, '\n')
		else:
			for y in x:
				if not y == '\n':
					print(ord(y) - 97, y)
					currentLetter = ord(y) - 97
					groupAnswered[currentLetter] = 1
	print(sum)

custom_customs("input.txt")


