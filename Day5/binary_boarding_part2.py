def binary_boarding_part2(input_file):
	file = open(input_file, "r")
	highestID = 0
	seats = []
	row = 0
	column = 0
	for x in file:
		lowerBound = 0
		upperBound = 127
		columnLower = 0
		columnUpper = 7
		count = 0
		for y in x:
			if count <= 6:
				if y == 'F':
					upperBound = (upperBound + lowerBound - 1)/2
				else:
					lowerBound = (upperBound + lowerBound + 1)/2
			elif count <= 9:
				if y == 'R':
					columnLower = (columnUpper + columnLower + 1)/2
				else:
					columnUpper = (columnUpper + columnLower - 1)/2
			count+=1
		row = upperBound
		column = columnUpper	
		ID = row * 8 + column
		seats.append(ID)
		if ID > highestID:
			highestID = ID

	print("highestID: ", highestID)
	for i in range(1024):
		if not i in seats and (i - 1) in seats and (i + 1) in seats:
			ID = i
	print("myID: ", ID)
binary_boarding_part2("input.txt")