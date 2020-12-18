f = open("input.txt")

active_0 = set()
active_1 = set()

lines = f.read().strip().split("\n")
for x, line in enumerate(lines):
	for y, char in enumerate(line):
		if char == "#":
			active_0.add((x,y,0,0))

x_min, y_min, z_min, w_min = -1, -1, -1, -1
x_max = len(lines)
y_max = len(lines[0])
z_max = 1
w_max = 1

iterations = 6
active_sets = [active_0, active_1]
current_set_index = 0

for i in range(iterations):
	current_set = active_sets[current_set_index]
	current_set_index = ~current_set_index
	target_set = active_sets[current_set_index]

	for x in range(x_min, x_max + 1):
		for y in range(y_min, y_max + 1):
			for z in range(z_min, z_max + 1):
				for w in range(w_min, w_max + 1):
					adjacent = 0

					for y_0 in range(y - 1, y + 2):
						for z_0 in range(z - 1, z + 2):
							for w_0 in range(w - 1, w + 2):
								adjacent += (x + 1, y_0, z_0, w_0) in current_set
								adjacent += (x - 1, y_0, z_0, w_0) in current_set

					for z_0 in range(z - 1, z + 2):
						for w_0 in range(w - 1, w + 2):
							adjacent += (x, y + 1, z_0, w_0) in current_set
							adjacent += (x, y - 1, z_0, w_0) in current_set

					for w_0 in range(w - 1, w + 2):
						adjacent += (x, y, z + 1, w_0) in current_set
						adjacent += (x, y, z - 1, w_0) in current_set

					adjacent += (x, y, z, w + 1) in current_set
					adjacent += (x, y, z, w - 1) in current_set

					coordinates = (x,y,z,w)

					if coordinates in current_set:
						if adjacent == 2 or adjacent == 3:
							target_set.add(coordinates)
						else:
							target_set.discard(coordinates)
					else:
						if adjacent == 3:
							target_set.add(coordinates)
						else:
							target_set.discard(coordinates)
	x_min -= 1
	y_min -= 1
	z_min -= 1
	w_min -= 1
	x_max += 1
	y_max += 1
	z_max += 1
	w_max += 1

print(len(active_sets[current_set_index]))