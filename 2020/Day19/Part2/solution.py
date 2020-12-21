import re
import regex

f = open("input.txt")

rule_strings = list()

for line in f:
	if line == "\n":
		break
	rule_strings.append(line.strip())

message_strings = list()

for line in f:
	if line == "\n":
		break
	message_strings.append(line.strip())

f.close()

message_rules = dict()

for rule_string in rule_strings:
	id, rule_list_string = rule_string.split(": ")
	if "\"" in rule_string:
		message_rules[int(id)] = rule_list_string[1:2]
	else:
		rules_substrings = [[int(rule_id_string) for rule_id_string in half.split(" ")] for half in rule_list_string.split(" | ")]
		message_rules[int(id)] = rules_substrings

regex_subroutines = dict()

for rule_id in message_rules:
	rule = message_rules[rule_id]
	if isinstance(rule, str):
		regex_subroutines[rule_id] = f"(?<r{rule_id}>{rule})"
	else:
		subroutine_options = list()
		for sub_rule in rule:
			subroutine_calls = list()
			for id in sub_rule:
				subroutine_calls.append(f"(?&r{id})")
			subroutine_options.append("".join(subroutine_calls))
		regex_subroutines[rule_id] = f"(?<r{rule_id}>{'|'.join(subroutine_options)})"

subroutine_definition_string = f"(?(DEFINE){''.join(regex_subroutines.values())})"

pattern_matches_rule_0 = regex.compile(f"{subroutine_definition_string}(?&r0)")

def matches_rule_0(message):
	return regex.fullmatch(pattern_matches_rule_0, message) is not None

sum = 0
for message_string in message_strings:
	sum += matches_rule_0(message_string)

print(sum)