#Note all numbers in the input are prime -> pairwaise coprime. Chinese Remainder Theorem can be applied
f = open("input.txt")
estimate = int(f.readline())
bus_with_id = list(enumerate(f.readline().strip().split(",")))
busses = list()
for bus in bus_with_id:
	try:
		busses.append((int(bus[1]), int(bus[1]) - bus[0]))
	except:
		pass

M = 1
for bus in busses:
	M *= bus[0]

x = 0
for bus in busses:
	m = M // bus[0]
	x += bus[1] * m * pow(m,-1,bus[0])

print(x % M)

