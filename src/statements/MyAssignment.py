from instructions.Instruction import Instruction


class MyAssignment:
	def __init__(self, left, right):
		self.left = left
		self.right = right
		self.body = []

	def add_to_body(self, instructions):
		self.body.extend(instructions)

	def get_instructions(self, function=None, memory_allocation=None):
		left = memory_allocation.get_address_by_variable_name(self.left.name, function)
		right = str(memory_allocation.get_active_register())  # TODO: Not only registers
		# right = memory_allocation.get_address_by_variable_name(self.right.name, function)

		if memory_allocation.in_register(self.left.name):
			self.body.append(Instruction(opcode="HIA", acc=left, operand=right, comment="variable " + str(self.left.name)))
		else:
			# right = memory_allocation.get_address_by_variable_name(self.right.name, function)
			self.body.append(Instruction(opcode="BIG", acc=right, operand=left, comment="variable " + str(self.left.name)))
		return self.body
