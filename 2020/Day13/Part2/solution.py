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

def inverse(a, n): #from https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
	t, t2 = 0, 1
	r, r2 = n, a

	while r2 != 0:
		q = r // r2
		t, t2 = t2, t - (q * t2)
		r, r2 = r2, r - (q * r2)

	if r > 1:
		return None
	if t < 0:
		t += n

	return t

M = 1
for bus in busses:
	M *= bus[0]

x = 0
for bus in busses:
	m = M // bus[0]
	x += bus[1] * m * inverse(m,bus[0])

print(x % M)

