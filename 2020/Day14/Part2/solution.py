import numpy as np

f = open('input.txt')

memory = dict()

def unpack(n, bits):
	return [n >> i & 1 for i in range(0, bits)]

def pack(bitfield): #LSB First
	place = 1
	val = 0
	for bit in bitfield:
		val += bit * place
		place *= 2
	return val

for instruction in f.read().strip().split("\n"):
	type, data = instruction.split(" = ")
	if type == "mask":
		floating_places = list()
		mask = 0
		for i, char in enumerate(data[::-1]):
			if char == "1":
				mask += 2**i
			elif char == "X":
				floating_places.append(i)
		floating_bits = [unpack(i, len(floating_places)) for i in range(2 ** len(floating_places))]
	else:
		address = int(type[4:-1])
		data = int(data)
		masked_address = address | mask
		for option in floating_bits:
			new_address = unpack(masked_address,36)
			for i, place in enumerate(floating_places):
				new_address[place] = option[i]
			memory[pack(new_address)] = data

sum = 0
for address in memory:
	sum += memory[address]

print(sum)
