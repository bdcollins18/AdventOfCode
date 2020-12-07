f = open("input.txt")
lines = [line.strip() for line in f]
width = len(lines[0])
height = len(lines)
right = 3
down = 1
x = 0
y = 0
trees = 0
while y < height:
	if lines[y][x] == '#':
		trees += 1
	y += down
	x += right
	x %= width

print(width)
print(height)
print(trees)