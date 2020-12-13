f = open("input.txt")
direction_strings = f.read().strip().split("\n")

x, y = 0, 0
heading = 0

for direction_string in direction_strings:
	type = direction_string[0]
	arg = int(direction_string[1:])

	if type == "N":
		y += arg
	elif type == "E":
		x += arg
	elif type == "S":
		y -= arg
	elif type == "W":
		x -= arg
	elif type == "L":
		heading += arg
		heading %= 360
	elif type == "R":
		heading -= arg
		heading %= 360
	elif type == "F":
		if heading == 0:
			x += arg
		elif heading == 90:
			y += arg
		elif heading == 180:
			x -= arg
		elif heading == 270:
			y -= arg
		else:
			print("UhOh")
			exit()
	else:
		print("UhOh")
		exit()

print(f"x={x},y={y}")
print(abs(x) + abs(y))