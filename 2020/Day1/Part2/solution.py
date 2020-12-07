from math import inf

f = open("input.txt")
nums = list()
for numString in f.readlines():
	nums.append(int(numString))
nums.sort()

low = 0
mid = 1
high = len(nums) - 1
bad_high_nums = 0

while True:
	sum = nums[low] + nums[mid] + nums[high]
	if sum == 2020:
		print(nums[low], nums[mid], nums[high])
		print(sum)
		print(nums[low] * nums[mid] * nums[high])
		break
	if sum > 2020:
		high -= 1
		if low + 1 == mid:
			bad_high_nums += 1
		continue
	elif low < high:
		mid += 1
	else:
		low += 1
		mid = low + 1
		high = len(nums) - 1 - bad_high_nums
