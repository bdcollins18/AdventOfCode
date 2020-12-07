def check_pwd(lower, upper, char, password):
	counter = 0
	for c in password:
		if c == char:
			counter += 1
	return lower <= counter and counter <= upper

f = open("input.txt")
i = 0
for line in f.readlines():
	parts = line.split()
	bounds = list(map(int, parts[0].split("-")))
	char = parts[1][0]
	password = parts[2]
	if check_pwd(bounds[0],bounds[1],char,password):
		i += 1
print(i)