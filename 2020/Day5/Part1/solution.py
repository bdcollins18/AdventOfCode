import math

f = open("input.txt")
seats = list()
for seat_string in [line.strip() for line in f]:
	row_start = 0
	row_end = 127
	column_start = 0
	column_end = 7
	for c in seat_string:
		if c == "F":
			row_end = math.floor((row_start + row_end) / 2)
		elif c == "B":
			row_start = math.ceil((row_start + row_end) / 2)
		elif c == "L":
			column_end = math.floor((column_start + column_end) / 2)
		elif c == "R":
			column_start = math.ceil((column_start + column_end) / 2)
	seats.append((row_start,column_start))

for seat in seats:
	print(seat)
print(max([(seat[0] * 8) + seat[1] for seat in seats]))