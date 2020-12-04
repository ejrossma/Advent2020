def passport_processing(input_file):
	file = open(input_file, "r")
	currentInfo = ""
	validPassports = 0
	valid = 1 #true
	#0 = byr, 1 = iyr, 2 = eyr, 3 = hgt, 4 = hcl, 5 = ecl, 6 = pid
	#all start as false
	infoStash = [0] * 7
	for x in file:
		if not x == '\n':
			currentInfo += x
		else:
			currentInfo = currentInfo.split()
			for info in currentInfo:
				temp = info.split(':')[0]
				if temp == "byr":
					infoStash[0] = 1
				elif temp == "iyr":
					infoStash[1] = 1
				elif temp == "eyr":
					infoStash[2] = 1
				elif temp == "hgt":
					infoStash[3] = 1
				elif temp == "hcl":
					infoStash[4] = 1
				elif temp == "ecl":
					infoStash[5] = 1
				elif temp == "pid":
					infoStash[6] = 1
			print(infoStash)
			for b in infoStash:
				if b == 0:
					valid = 0
			print(infoStash)
			print(valid)
			if valid == 1:
				validPassports += 1
			infoStash.clear()
			infoStash = [0] * 7
			currentInfo = ""
			valid = 1

	print(validPassports)
passport_processing("input.txt")