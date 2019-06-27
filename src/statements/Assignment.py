from instructions.Instruction import Instruction


class Assignment:
	def __init__(self, variable, expression):
		self.variable = variable
		self.expression = expression

	def compile(self):
		return Instruction(opcode = "BIG", acc = "R?", operand = "LOC?")