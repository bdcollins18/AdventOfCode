from enum import Enum
from copy import deepcopy

class Seat(Enum):
	EMPTY = 0
	TAKEN = 1
	FLOOR = 2

	@staticmethod
	def fromChar(char):
		if char == "L":
			return Seat.EMPTY
		elif char == ".":
			return Seat.FLOOR
		elif char == "#":
			return Seat.TAKEN

f = open("input.txt")
row_strings = f.read().strip().split("\n")
waiting_area = list()
for row_string in row_strings:
	row = list()
	for char in row_string:
		row.append(Seat.fromChar(char))
	waiting_area.append(row)

# for row in waiting_area:
# 	print(row)

waiting_area_height = len(waiting_area)
bottom_row = waiting_area_height - 1
second_bottom_row = bottom_row - 1
waiting_area_width = len(waiting_area[0])
right_col = waiting_area_width - 1
second_right_col = right_col - 1

waiting_area_2 = deepcopy(waiting_area)
for row in range(waiting_area_height): #No simulation needed for step 1
	for col in range(waiting_area_width):
		if waiting_area_2[row][col] is Seat.EMPTY:
			waiting_area_2[row][col] = Seat.TAKEN

def get_next(waiting_area, row, col):
	current = waiting_area[row][col]
	if current is Seat.TAKEN:
		seen = 0
		test_row = row - 1
		while test_row >= 0:
			test = waiting_area[test_row][col]
			if test is Seat.TAKEN:
				seen += 1
				break
			elif test is Seat.EMPTY:
				break
			test_row -= 1

		test_row = row - 1
		test_col = col + 1
		while test_row >= 0 and test_col < waiting_area_width:
			test = waiting_area[test_row][test_col]
			if test is Seat.TAKEN:
				seen += 1
				break
			elif test is Seat.EMPTY:
				break
			test_row -= 1
			test_col += 1

		test_col = col + 1
		while test_col < waiting_area_width:
			test = waiting_area[row][test_col]
			if test is Seat.TAKEN:
				seen += 1
				break
			elif test is Seat.EMPTY:
				break
			test_col += 1

		test_row = row + 1
		test_col = col + 1
		while test_row < waiting_area_height and test_col < waiting_area_width:
			test = waiting_area[test_row][test_col]
			if test is Seat.TAKEN:
				seen += 1
				break
			elif test is Seat.EMPTY:
				break
			test_row += 1
			test_col += 1

		test_row = row + 1
		while test_row < waiting_area_height:
			test = waiting_area[test_row][col]
			if test is Seat.TAKEN:
				seen += 1
				break
			elif test is Seat.EMPTY:
				break
			test_row += 1

		test_row = row + 1
		test_col = col - 1
		while test_row < waiting_area_height and test_col >= 0:
			test = waiting_area[test_row][test_col]
			if test is Seat.TAKEN:
				seen += 1
				break
			elif test is Seat.EMPTY:
				break
			test_row += 1
			test_col -= 1

		test_col = col - 1
		while test_col >= 0:
			test = waiting_area[row][test_col]
			if test is Seat.TAKEN:
				seen += 1
				break
			elif test is Seat.EMPTY:
				break
			test_col -= 1

		test_row = row - 1
		test_col = col - 1
		while test_row >= 0 and test_col >= 0:
			test = waiting_area[test_row][test_col]
			if test is Seat.TAKEN:
				seen += 1
				break
			elif test is Seat.EMPTY:
				break
			test_row -= 1
			test_col -= 1

		if seen > 4:
			return Seat.EMPTY
		else:
			return Seat.TAKEN

	elif current is Seat.EMPTY:

		test_row = row - 1
		while test_row >= 0:
			test = waiting_area[test_row][col]
			if test is Seat.TAKEN:
				return Seat.EMPTY
			elif test is Seat.EMPTY:
				break
			test_row -= 1

		test_row = row - 1
		test_col = col + 1
		while test_row >= 0 and test_col < waiting_area_width:
			test = waiting_area[test_row][test_col]
			if test is Seat.TAKEN:
				return Seat.EMPTY
			elif test is Seat.EMPTY:
				break
			test_row -= 1
			test_col += 1

		test_col = col + 1
		while test_col < waiting_area_width:
			test = waiting_area[row][test_col]
			if test is Seat.TAKEN:
				return Seat.EMPTY
			elif test is Seat.EMPTY:
				break
			test_col += 1

		test_row = row + 1
		test_col = col + 1
		while test_row < waiting_area_height and test_col < waiting_area_width:
			test = waiting_area[test_row][test_col]
			if test is Seat.TAKEN:
				return Seat.EMPTY
			elif test is Seat.EMPTY:
				break
			test_row += 1
			test_col += 1

		test_row = row + 1
		while test_row < waiting_area_height:
			test = waiting_area[test_row][col]
			if test is Seat.TAKEN:
				return Seat.EMPTY
			elif test is Seat.EMPTY:
				break
			test_row += 1

		test_row = row + 1
		test_col = col - 1
		while test_row < waiting_area_height and test_col >= 0:
			test = waiting_area[test_row][test_col]
			if test is Seat.TAKEN:
				return Seat.EMPTY
			elif test is Seat.EMPTY:
				break
			test_row += 1
			test_col -= 1

		test_col = col - 1
		while test_col >= 0:
			test = waiting_area[row][test_col]
			if test is Seat.TAKEN:
				return Seat.EMPTY
			elif test is Seat.EMPTY:
				break
			test_col -= 1

		test_row = row - 1
		test_col = col - 1
		while test_row >= 0 and test_col >= 0:
			test = waiting_area[test_row][test_col]
			if test is Seat.TAKEN:
				return Seat.EMPTY
			elif test is Seat.EMPTY:
				break
			test_row -= 1
			test_col -= 1

		return Seat.TAKEN

	else:
		return Seat.FLOOR

def is_different(waiting_area, waiting_area_2):
	for row in range(waiting_area_height):
		for col in range(waiting_area_width):
			if waiting_area[row][col] != waiting_area_2[row][col]:
				return True
	return False

def print_waiting_area(waiting_area):
	for row in range(waiting_area_height):
		for col in range(waiting_area_width):
			val = waiting_area[row][col]
			if val is Seat.EMPTY:
				print("L",end="")
			elif val is Seat.TAKEN:
				print("#",end="")
			else:
				print(".",end="")
		print()

waiting_areas = [waiting_area, waiting_area_2]
current_area_index = 1
while is_different(waiting_area, waiting_area_2):
	current_area = waiting_areas[current_area_index]
	# print_waiting_area(current_area)
	# print()
	# input()
	current_area_index = not current_area_index
	target_area = waiting_areas[current_area_index]
	for row in range(waiting_area_height):
		for col in range(waiting_area_width):
			target_area[row][col] = get_next(current_area, row, col)

occupied = 0
for row in range(waiting_area_height):
	for col in range(waiting_area_width):
		occupied += waiting_areas[current_area_index][row][col] is Seat.TAKEN

print(occupied)




