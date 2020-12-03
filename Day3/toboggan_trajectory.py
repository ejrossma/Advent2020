def toboggan_trajectory(input_file):
	
	#setup map
	file = open(input_file, "r")
	map = []
	bottom = 0
	for x in file:
		map.append(x)
		bottom += 1

	#flight path + map vars
	hor = 1
	curr_hor = 0
	vert = 2
	curr_vert = 0
	width = len(map[0])-1
	trees_hit = 0

	while curr_vert < bottom-1:
		#incrementing position values
		curr_vert += vert
		curr_hor += hor
		if curr_hor >= width:
			curr_hor = curr_hor - width
		#checking value at curr_vert/curr_hor
		checker = map[curr_vert]
		checker = checker[curr_hor]
		if (checker == '#'):
			trees_hit+=1
	print (trees_hit)


toboggan_trajectory("input.txt")