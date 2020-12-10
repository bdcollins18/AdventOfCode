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
		invalid_num = test_num
		break
	window_start += 1
	window_end += 1

window_start = 0
window_last = 1
sum = nums[window_start] + nums[window_last]
while sum != invalid_num:
	if sum < invalid_num:
		window_last += 1
		sum += nums[window_last]
	else:
		sum -= nums[window_start]
		window_start += 1

window = nums[window_start: window_last + 1]
window.sort()
print(window[0] + window[-1])


