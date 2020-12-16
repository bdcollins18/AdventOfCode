import re
import math

f = open("input.txt")

fields = dict()

for line in f:
	if line == "\n":
		break
	matches = re.search(r'(.+): (\d+)-(\d+) or (\d+)-(\d+)', line)
	if matches:
		fields[matches.group(1)] = ((int(matches.group(2)), int(matches.group(3))), (int(matches.group(4)), int(matches.group(5))))
	else:
		print("UhOh")
		exit()

f.readline() # Dump "your ticket:" line

your_ticket = [int(s) for s in f.readline().strip().split(",")]

f.readline()
f.readline() # Dump "nearby tickets:" and newline

nearby_tickets = list()

for line in f:
	if line == "\n":
		break
	nearby_tickets.append([int(s) for s in line.strip().split(",")])

all_field_ranges = list()
for field in fields:
	all_field_ranges.append(fields[field][0])
	all_field_ranges.append(fields[field][1])

all_field_ranges.sort()

def in_range(v, tup):
	return tup[0] <= v <= tup[1]

def ranges_overlap(range1, range2):
	return (in_range(range1[0], range2) or
			in_range(range1[1], range2) or
			in_range(range2[0], range1) or
			in_range(range2[1], range1))

def combine_ranges(range1, range2): #assumes ranges overlap
	bounds = [*range1, *range2]
	return (min(bounds), max(bounds))

combined_ranges = list()
combined_range = all_field_ranges[0]
for i in range(1, len(all_field_ranges)):
	if ranges_overlap(combined_range, all_field_ranges[i]):
		combined_range = combine_ranges(combined_range, all_field_ranges[i])
	else:
		combined_ranges.append(combined_range)
		combined_range = all_field_ranges[i]

if combined_range is not None:
	combined_ranges.append(combined_range)

valid_nearby_tickets = list()

for ticket in nearby_tickets:
	valid = True
	for value in ticket:
		for valid_range in combined_ranges:
			if not in_range(value, valid_range):
				valid = False
				break
		if not valid:
			break
	if valid:
		valid_nearby_tickets.append(ticket)

working_field_map = dict() #field -> Set[ticket_index]
field_map = dict() # field -> ticket_index

for field in fields:
	working_field_map[field] = set(range(len(your_ticket)))

def in_field_range(v, field):
	return in_range(v, fields[field][0]) or in_range(v, fields[field][1])

while True:
	found_value = False
	for ticket in valid_nearby_tickets:
		for field in working_field_map.copy():
			index_set = working_field_map[field]
			for index in index_set.copy():
				if not in_field_range(ticket[index], field):
					index_set.remove(index)
			if len(index_set) == 1:
				found_index = index_set.pop()
				field_map[field] = found_index
				del working_field_map[field]
				found_value = True
				for field in working_field_map:
					other_index_set = working_field_map[field]
					if found_index in other_index_set:
						other_index_set.remove(found_index)
	if len(working_field_map) == 0 or not found_value:
		break

departure_product = 1
for field in fields:
	if "departure" in field:
		departure_product *= your_ticket[field_map[field]]

print(departure_product)

