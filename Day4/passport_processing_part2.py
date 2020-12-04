def passport_processing(input_file):
	file = open(input_file, "r")
	currentInfo = ""
	validPassports = 0
	valid = 1 #true
	#0 = byr, 1 = iyr, 2 = eyr, 3 = hgt, 4 = hcl, 5 = ecl, 6 = pid
	#all start as false
	infoStash = [0] * 7
	validEyeColors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
	for x in file:
		if not x == '\n':
			currentInfo += x
		else:
			currentInfo = currentInfo.split()
			for info in currentInfo:
				temp = info.split(':')
				if temp[0] == "byr" and int(temp[1]) >= 1920 and int(temp[1]) <= 2002 and len(temp[1]) == 4:
					infoStash[0] = 1
				elif temp[0] == "iyr" and int(temp[1]) >= 2010 and int(temp[1]) <= 2020 and len(temp[1]) == 4:
					infoStash[1] = 1
				elif temp[0] == "eyr" and int(temp[1]) >= 2020 and int(temp[1]) <= 2030 and len(temp[1]) == 4:
					infoStash[2] = 1
				elif temp[0] == "hgt":
					if "cm" in temp[1]:
						val = temp[1].split("cm")[0]
						if int(val) >= 150 and int(val) <= 193:
							infoStash[3] = 1
					elif "in" in temp[1]:
						val = temp[1].split("in")[0]
						if int(val) >= 59 and int(val) <= 76:
							infoStash[3] = 1
				elif temp[0] == "hcl" and temp[1][0] == '#':
					val = temp[1].split("#")[1]
					for x in val:
						if x.isalpha():
							if ord(x) >= 97 and ord(x) <= 102:
								infoStash[4] = 1
						elif x.isdigit():
							if int(x) >= 0 and int(x) <= 9:
								infoStash[4] = 1
				elif temp[0] == "ecl" and temp[1] in validEyeColors:
					infoStash[5] = 1
				elif temp[0] == "pid" and temp[1].isdigit() and len(temp[1]) == 9:
					infoStash[6] = 1
			for b in infoStash:
				if b == 0:
					valid = 0
			if valid == 1:
				validPassports += 1
			infoStash.clear()
			infoStash = [0] * 7
			currentInfo = ""
			valid = 1

	print(validPassports)
passport_processing("input.txt")