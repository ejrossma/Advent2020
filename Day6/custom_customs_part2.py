def custom_customs_part2(input_file):
	file = open(input_file, "r")
	sum = 0
	count = 0
	letIQ = ""
	for x in file:
		if x == '\n':
			for l in letIQ:
				sum+=1
			groupAnswered = [0] * 26
			count = 0
			letIQ = ""
			print("sum: ", sum, '\n')
		else:
			if count == 0:
				for y in x:
					if not y == '\n':
						letIQ += y
						count+=1
			else:
				print(letIQ)			
				for l in letIQ:
					if not l in x:
						letIQ = letIQ.replace(l, '')
						print(letIQ)						
		


	print(sum)

custom_customs_part2("input.txt")


