file = open("input.txt")
group_strings = file.read().strip().split("\n\n")
groups = list()
for group_string in group_strings:
	group = list()
	for person in group_string.split("\n"):
		group.append({c for c in person.strip()})
	groups.append(group)

group_questions = list()
for group in groups:
	if len(group) == 1:
		group_questions.append(group[0])
		continue
	else:
		group_questions.append(group[0].union(*group[1:]))

sum = 0
for s in group_questions:
	sum += len(s)

print(sum)