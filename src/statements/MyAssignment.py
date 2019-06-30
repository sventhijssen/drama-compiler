from instructions.Instruction import Instruction


class MyAssignment:
	def __init__(self, left, right, memory_allocation):
		self.left = left
		self.right = right
		self.memory_allocation = memory_allocation
		self.body = []

	def add_to_body(self, instructions):
		self.body.extend(instructions)

	def get_instructions(self):
		# if self.left.in_register():
		# 	pass # TODO: HIA
		# else:
		# 	pass # TODO: BIG
		# 	self.body.append(Instruction(opcode="BIG", acc="R?", operand="LOC?", comment="variable " + str(self.left.name)))
		self.body.append(Instruction(opcode="BIG", acc="R?", operand="LOC?", comment="variable " + str(self.left.name)))
		return self.body
