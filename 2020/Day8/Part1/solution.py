from enum import Enum

class InstructionType(Enum):
	NOP = 0
	JMP = 1
	ACC = 2

class Instruction:
	def __init__(self, instruction_string):
		instruction_type_string = instruction_string[:3]
		instruction_arg_string = instruction_string[4:]
		if instruction_type_string == "nop":
			self.type = InstructionType.NOP
		elif instruction_type_string == "jmp":
			self.type = InstructionType.JMP
		elif instruction_type_string == "acc":
			self.type = InstructionType.ACC
		else:
			print(f'Bad Instruction Type in: {instruction_string}')
			exit()
		try:
			self.arg = int(instruction_arg_string)
		except:
			print(f'Bad Arg Value in: {instruction_string}')
			exit()

def interpret(instructions):
	visited = [False] * len(instructions)
	accumulator = 0
	address = 0

	while not visited[address]:
		visited[address] = True
		instruction = instructions[address]
		if instruction.type == InstructionType.NOP:
			address += 1
		elif instruction.type == InstructionType.ACC:
			accumulator += instruction.arg
			address += 1
		else:
			address += instruction.arg

	return accumulator, address, visited

f = open("input.txt")
instruction_strings = f.read().strip().split("\n")
instructions = list()

for instruction_string in instruction_strings:
	instructions.append(Instruction(instruction_string))

accumulator, address, visited = interpret(instructions)
print(accumulator)