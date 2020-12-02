def password_philosophy(input_file):
	file = open(input_file, "r")
	valid_codes = 0
	for x in file:
		lower = ""
		upper = ""
		count = 0
		y = x[count]
		while not y == '-':
			lower += y
			count+=1
			y = x[count]
		lower = int(lower)

		count+=1
		y = x[count]
		while not y == ' ':
			upper += y
			count+=1
			y = x[count]
		upper = int(upper)

		count+=1
		target_letter = x[count]
		total_letter = -1
		for y in x:
			if y == target_letter:
				total_letter+=1
		if total_letter >= lower and total_letter <= upper:
			valid_codes+=1
	print(valid_codes)

password_philosophy("input.txt")