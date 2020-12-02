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

		count+=3
		if target_letter == x[count + lower-1] and not target_letter == x[count + upper-1]:
			valid_codes+=1
		elif not target_letter == x[count + lower-1] and target_letter == x[count + upper-1]:
			valid_codes+=1
	print(valid_codes)

password_philosophy("input.txt")