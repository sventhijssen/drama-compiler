from instructions.Instruction import Instruction


class MyAssignment:
	def __init__(self, left, right):
		self.left = left
		self.right = right
		self.body = []

	def add_to_body(self, instructions):
		self.body.extend(instructions)

	def get_instructions(self):
		self.body.append(Instruction(opcode="BIG", acc="R?", operand="LOC?", comment="variable " + str(self.left.name)))
		return self.body
