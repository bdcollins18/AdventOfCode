# ENDC = '\033[0m'
# BACK_WHITE = '\u001b[47;1m'
# FORE_BLACK = '\u001b[30m'



import re

f = open("input.txt")

def parse(expression):
	tokens = re.findall(r"\d+|[()+*]", expression)
	return tokens

def eval(tokens, start = 0, expecting_paren = False): # -> result, end
	accumulator = 0
	operator = "+"
	i = start

	while i < len(tokens):
		current = tokens[i]

		# print(f"{''.join(tokens[:i])}", end = "")
		# print(f"{BACK_WHITE}{FORE_BLACK}{tokens[i]}{ENDC}", end = "")
		# print(f"{''.join(tokens[i+1:])}")
		# print(f"Current: {current}, Operator: {operator}, Accumulator: {accumulator}, Expecting Paren: {expecting_paren}")
		# input()

		if re.fullmatch(r"\d+", current):
			if operator == "+":
				accumulator += int(current)
				i += 1
			elif operator == "*":
				result, i = eval(tokens, start = i, expecting_paren = False)
				accumulator *= result

		elif current == "(":
			if operator == "+":
				result, i = eval(tokens, start = i + 1, expecting_paren = True)
				accumulator += result
			elif operator == "*":
				result, i = eval(tokens, start = i, expecting_paren = False)
				accumulator *= result

		elif current in "+*":
			operator = current
			i += 1

		elif current == ")":
			if expecting_paren:
				i += 1
			break
	return accumulator, i

lines = f.read().strip().split("\n")
sum = 0
for line in lines:
	result, i = eval(parse(line))
	# print(result)
	sum += result

print(sum)
