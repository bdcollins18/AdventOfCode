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

colors_to_check = set(bag_rules.keys())
successful_colors = set()
last_check_size = len(colors_to_check)
while True:
	for color in colors_to_check:
		bag_rule = bag_rules[color]
		for color2 in bag_rule:
			if color2 == "shiny gold" or color2 in successful_colors:
				successful_colors.add(color)
				break
	colors_to_check -= successful_colors
	if len(colors_to_check) == last_check_size:
		break
	else:
		last_check_size = len(colors_to_check)

print(successful_colors)
print(len(successful_colors))