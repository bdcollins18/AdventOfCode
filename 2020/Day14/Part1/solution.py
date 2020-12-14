f = open('input.txt')

memory = dict()
mask_max = (2**36)-1
mask_min = 0

for instruction in f.read().strip().split("\n"):
	type, data = instruction.split(" = ")
	if type == "mask":
		zero_mask = (2**36)-1
		one_mask = 0
		for i, char in enumerate(data[::-1]):
			if char == "0":
				zero_mask -= 2 ** i 
			elif char == "1":
				one_mask += 2 ** i
	else:
		address = int(type[4:-1])
		data = int(data)
		masked = (data & zero_mask) | one_mask
		memory[address] = masked

sum = 0
for address in memory:
	sum += memory[address]

print(sum)
