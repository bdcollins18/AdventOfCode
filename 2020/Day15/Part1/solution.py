f = open("input.txt")
starting_nums = [int(s) for s in f.read().strip().split(",")]
memory = dict()
turn_num = 1
for starting_num in starting_nums[:-1]:
	memory[starting_num] = turn_num
	turn_num += 1

next_num = starting_nums[-1]
while turn_num <= 2020:
	spoken_num = next_num
	if spoken_num not in memory:
		next_num = 0
	else:
		next_num = turn_num - memory[spoken_num]
	memory[spoken_num] = turn_num
	turn_num += 1

print(f"{spoken_num} Spoken on Turn {turn_num - 1}")
print(f"{next_num} Will Be Spoken on Turn {turn_num}")