def report_repair(input_file):
	file = open(input_file, "r")
	loop = []
	for x in file:
		loop.append(int(x))
	outcome = 0
	for i in loop:
		for j in loop:
			num = i + j
			if num == 2020:
				outcome = i * j
	print(outcome)

report_repair("input.txt")