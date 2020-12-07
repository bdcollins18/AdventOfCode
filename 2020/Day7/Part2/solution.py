import re

f = open("input.txt")
input_string = f.read().strip()
bag_strings = input_string.split("\n")
bag_rules = dict() #a map of bag color to a map of bag color to number
for bag_string in bag_strings:
	color, contents_string = bag_string.split(" bags contain ")
	contents = dict()
	if contents_string != "no other bags.":
		content_string_list = re.sub(r' bags?','',contents_string[:-1]).split(", ")
		for content_string in content_string_list:
			contents[content_string[2:]] = int(content_string[:1])
	bag_rules[color] = contents

# for color in bag_rules:
# 	print(color)
# 	bag_rule = bag_rules[color]
# 	for color2 in bag_rule:
# 		print('\t{}:{}'.format(color2, bag_rule[color2]))

contents_memo = dict()

def count_contents(color):
	if color not in contents_memo:
		bag_rule = bag_rules[color]
		if bag_rule == {}:
			contents_memo[color] = 0
		else:
			contents = 0
			for color2 in bag_rule:
				contents += bag_rule[color2] + (bag_rule[color2] * count_contents(color2))
			contents_memo[color] = contents
	return contents_memo[color]

print(count_contents("shiny gold"))
print(contents_memo)

