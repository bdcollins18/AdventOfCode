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

#I never update the corners as per the update rules, so I preset them
if waiting_area[0][0] is Seat.EMPTY:
	waiting_area[0][0] = Seat.TAKEN
if waiting_area[bottom_row][0] is Seat.EMPTY:
	waiting_area[bottom_row][0] = Seat.TAKEN
if waiting_area[bottom_row][right_col] is Seat.EMPTY:
	waiting_area[bottom_row][right_col] = Seat.TAKEN
if waiting_area[0][right_col] is Seat.EMPTY:
	waiting_area[0][right_col] = Seat.TAKEN

def get_next_top(waiting_area, col):
	prev_col = col - 1
	next_col = col + 1
	current = waiting_area[0][col]
	if current is Seat.TAKEN:
		adjacent = 0
		adjacent += waiting_area[0][prev_col] is Seat.TAKEN
		adjacent += waiting_area[0][next_col] is Seat.TAKEN
		adjacent += waiting_area[1][prev_col] is Seat.TAKEN
		adjacent += waiting_area[1][col] is Seat.TAKEN
		adjacent += waiting_area[1][next_col] is Seat.TAKEN
		if adjacent >= 4:
			return Seat.EMPTY
		else:
			return Seat.TAKEN
	elif current is Seat.EMPTY:
		if (waiting_area[0][prev_col] is Seat.TAKEN or
			waiting_area[0][next_col] is Seat.TAKEN or
			waiting_area[1][prev_col] is Seat.TAKEN or
			waiting_area[1][col] is Seat.TAKEN or 
			waiting_area[1][next_col] is Seat.TAKEN):
			return Seat.EMPTY
		else:
			return Seat.TAKEN
	else:
		return Seat.FLOOR

def get_next_bottom(waiting_area, col):
	prev_col = col - 1
	next_col = col + 1
	current = waiting_area[bottom_row][col]
	if current is Seat.TAKEN:
		adjacent = 0
		adjacent += waiting_area[bottom_row][prev_col] is Seat.TAKEN
		adjacent += waiting_area[bottom_row][next_col] is Seat.TAKEN
		adjacent += waiting_area[second_bottom_row][prev_col] is Seat.TAKEN
		adjacent += waiting_area[second_bottom_row][col] is Seat.TAKEN
		adjacent += waiting_area[second_bottom_row][next_col] is Seat.TAKEN
		if adjacent >= 4:
			return Seat.EMPTY
		else:
			return Seat.TAKEN
	elif current is Seat.EMPTY:
		if (waiting_area[bottom_row][prev_col] is Seat.TAKEN or
			waiting_area[bottom_row][next_col] is Seat.TAKEN or
			waiting_area[second_bottom_row][prev_col] is Seat.TAKEN or
			waiting_area[second_bottom_row][col] is Seat.TAKEN or 
			waiting_area[second_bottom_row][next_col] is Seat.TAKEN):
			return Seat.EMPTY
		else:
			return Seat.TAKEN
	else:
		return Seat.FLOOR

def get_next_left(waiting_area, row):
	prev_row = row - 1
	next_row = row + 1
	current = waiting_area[row][0]
	if current is Seat.TAKEN:
		adjacent = 0
		adjacent += waiting_area[prev_row][0] is Seat.TAKEN
		adjacent += waiting_area[prev_row][1] is Seat.TAKEN
		adjacent += waiting_area[row][1] is Seat.TAKEN
		adjacent += waiting_area[next_row][0] is Seat.TAKEN
		adjacent += waiting_area[next_row][1] is Seat.TAKEN
		if adjacent >= 4:
			return Seat.EMPTY
		else:
			return Seat.TAKEN
	elif current is Seat.EMPTY:
		if (waiting_area[prev_row][0] is Seat.TAKEN or
			waiting_area[prev_row][1] is Seat.TAKEN or
			waiting_area[row][1] is Seat.TAKEN or
			waiting_area[next_row][0] is Seat.TAKEN or 
			waiting_area[next_row][1] is Seat.TAKEN):
			return Seat.EMPTY
		else:
			return Seat.TAKEN
	else:
		return Seat.FLOOR

def get_next_right(waiting_area, row):
	prev_row = row - 1
	next_row = row + 1
	current = waiting_area[row][right_col]
	if current is Seat.TAKEN:
		adjacent = 0
		adjacent += waiting_area[prev_row][right_col] is Seat.TAKEN
		adjacent += waiting_area[prev_row][second_right_col] is Seat.TAKEN
		adjacent += waiting_area[row][second_right_col] is Seat.TAKEN
		adjacent += waiting_area[next_row][right_col] is Seat.TAKEN
		adjacent += waiting_area[next_row][second_right_col] is Seat.TAKEN
		if adjacent >= 4:
			return Seat.EMPTY
		else:
			return Seat.TAKEN
	elif current is Seat.EMPTY:
		if (waiting_area[prev_row][right_col] is Seat.TAKEN or
			waiting_area[prev_row][second_right_col] is Seat.TAKEN or
			waiting_area[row][second_right_col] is Seat.TAKEN or
			waiting_area[next_row][right_col] is Seat.TAKEN or 
			waiting_area[next_row][second_right_col] is Seat.TAKEN):
			return Seat.EMPTY
		else:
			return Seat.TAKEN
	else:
		return Seat.FLOOR

def get_next_center(waiting_area, row, col):
	prev_row = row - 1
	next_row = row + 1
	prev_col = col - 1
	next_col = col + 1
	current = waiting_area[row][col]
	if current is Seat.TAKEN:
		adjacent = 0
		adjacent += waiting_area[prev_row][prev_col] is Seat.TAKEN
		adjacent += waiting_area[prev_row][col] is Seat.TAKEN
		adjacent += waiting_area[prev_row][next_col] is Seat.TAKEN
		adjacent += waiting_area[row][prev_col] is Seat.TAKEN
		adjacent += waiting_area[row][next_col] is Seat.TAKEN
		adjacent += waiting_area[next_row][prev_col] is Seat.TAKEN
		adjacent += waiting_area[next_row][col] is Seat.TAKEN
		adjacent += waiting_area[next_row][next_col] is Seat.TAKEN
		if adjacent >= 4:
			return Seat.EMPTY
		else:
			return Seat.TAKEN
	elif current is Seat.EMPTY:
		if (waiting_area[prev_row][prev_col] is Seat.TAKEN or
			waiting_area[prev_row][col] is Seat.TAKEN or
			waiting_area[prev_row][next_col] is Seat.TAKEN or
			waiting_area[row][prev_col] is Seat.TAKEN or
			waiting_area[row][next_col] is Seat.TAKEN or
			waiting_area[next_row][prev_col] is Seat.TAKEN or
			waiting_area[next_row][col] is Seat.TAKEN or
			waiting_area[next_row][next_col] is Seat.TAKEN):
			return Seat.EMPTY
		else:
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
	current_area_index = not current_area_index
	target_area = waiting_areas[current_area_index]
	for col in range(1, waiting_area_width - 1):
		target_area[0][col] = get_next_top(current_area, col)
		target_area[bottom_row][col] = get_next_bottom(current_area, col)

	for row in range(1, waiting_area_height - 1):
		target_area[row][0] = get_next_left(current_area, row)
		target_area[row][right_col] = get_next_right(current_area, row)

	for row in range(1, waiting_area_height - 1):
		for col in range(1, waiting_area_width - 1):
			target_area[row][col] = get_next_center(current_area, row, col)

occupied = 0
for row in range(waiting_area_height):
	for col in range(waiting_area_width):
		occupied += waiting_areas[current_area_index][row][col] is Seat.TAKEN

print(occupied)




