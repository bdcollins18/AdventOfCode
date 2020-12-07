f = open("input.txt")
nums = list()
for numString in f.readlines():
	nums.append(int(numString))

diffs = list()
for num in nums:
	diffs.append(2020 - num)

p = None
for i, num in enumerate(nums):
	for j, diff in enumerate(diffs):
		if num == diff and i != j:
			print(nums[i],nums[j])
			print(nums[i] * nums[j])