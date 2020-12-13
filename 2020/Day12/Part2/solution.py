f = open("input.txt")
direction_strings = f.read().strip().split("\n")

ship_x, ship_y = 0,0
way_x, way_y = 10,1 #offset from ship pos

for direction_string in direction_strings:
	type = direction_string[0]
	arg = int(direction_string[1:])

	if type == "N":
		way_y += arg
	elif type == "E":
		way_x += arg
	elif type == "S":
		way_y -= arg
	elif type == "W":
		way_x -= arg
	elif type == "L":
		turns = arg // 90
		for i in range(turns):
			temp = way_x
			way_x = -1 * way_y
			way_y = temp
	elif type == "R":
		turns = arg // 90
		for i in range(turns):
			temp = -1 * way_x
			way_x = way_y
			way_y = temp
	elif type == "F":
		for i in range(arg):
			ship_x += way_x
			ship_y += way_y
	else:
		print("UhOh")
		exit()

print(f"x={ship_x},y={ship_y}")
print(abs(ship_x) + abs(ship_y))