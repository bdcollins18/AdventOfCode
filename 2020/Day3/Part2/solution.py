f = open("input.txt")
lines = [line.strip() for line in f]
width = len(lines[0])
height = len(lines)
slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
trees = list()

for slope in slopes:
	right = slope[0]
	down = slope[1]
	x = 0
	y = 0
	trees_hit = 0
	while y < height:
		if lines[y][x] == '#':
			trees_hit += 1
		y += down
		x += right
		x %= width
	trees.append(trees_hit)

product = 1
for n in trees:
	product *= n
print(product)