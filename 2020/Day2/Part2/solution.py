def check_pwd(pos1, pos2, char, password):
	return (password[pos1 - 1] == char) ^ (password[pos2 - 1] == char)

f = open("input.txt")
i = 0
for line in f.readlines():
	parts = line.split()
	positions = list(map(int, parts[0].split("-")))
	char = parts[1][0]
	password = parts[2]
	if check_pwd(positions[0],positions[1],char,password):
		i += 1
print(i)