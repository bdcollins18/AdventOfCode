f = open("input.txt")
nums = [int(line) for line in f.read().strip().split()]
preamble_end = 25
window_start = 0
window_end = preamble_end
while window_end < len(nums):
	test_num = nums[window_end]
	found = False
	for i in range(window_start, window_end):
		for j in range(i + 1, window_end):
			if test_num == nums[i] + nums[j]:
				found = True
				break
	if not found:
		print(test_num)
		exit()
	window_start += 1
	window_end += 1

print("UhOh")
