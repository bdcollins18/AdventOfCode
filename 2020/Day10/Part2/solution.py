#https://oeis.org/A000073
def tribonacci(n):
	store = [0,0,1]
	i = 2
	for init in store:
		yield init
	while i < n:
		next = store[i] + store[i - 1] + store[i - 2]
		yield next
		i += 1
		store.append(next)

f = open("input.txt")
nums = [int(line) for line in f.read().strip().split("\n")]
nums.sort()
nums.insert(0,0)
nums.append(nums[-1] + 3)

diffs = list()
for i in range(len(nums) - 1):
	diffs.append(nums[i+1] - nums[i])

sections = list()
ones = 0
max = 0
for n in diffs:
	if n == 1:
		ones += 1
	elif n == 3:
		sections.append(ones)
		if ones > max:
			max = ones
		ones = 0
	else:
		print("UhOh")
		exit()

t = list(tribonacci(max + 2))
product = 1
for n in sections:
	product *= t[n + 2]

print(product)
