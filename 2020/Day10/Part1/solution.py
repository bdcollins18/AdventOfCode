f = open("input.txt")
nums = [int(line) for line in f.read().strip().split("\n")]
nums.sort()
ones = 0
twos = 0
threes = 1
j = 0
for i in nums:
	diff = i - j
	if diff == 1:
		ones += 1
	elif diff == 2:
		twos += 1
	else:
		threes += 1
	j = i

print(ones, threes, ones*threes)