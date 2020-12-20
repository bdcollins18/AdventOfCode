import re

f = open("input.txt")

def parse(expression):
	tokens = re.findall(r"\d+|[()+*]", expression)
	return tokens

def eval(tokens, start = 0): # -> result, end
	
	accumulator = 0
	operator = "+"
	i = start

	current = tokens[i]
	while i < len(tokens) and current != ")":
		current = tokens[i]
		# print(f"Current: {current}, Operator: {operator}, Accumulator: {accumulator}")
		# input()
		if re.match(r"\d+", current):
			if operator == "+":
				accumulator += int(current)
			elif operator == "*":
				accumulator *= int(current)
			else:
				exit(f"Bad Operator: {operator}")
			i += 1

		elif current == "(":
			result, i = eval(tokens, start = i + 1)
			if operator == "+":
				accumulator += result
			elif operator == "*":
				accumulator *= result
			else:
				exit(f"Bad Operator: {operator}")

		elif current in "*+":
			operator = current
			i += 1

	return accumulator, i + 1

lines = f.read().strip().split("\n")
sum = 0
for line in lines:
	sum += eval(parse(line))[0]

print(sum)
