from Register import Register
from instructions.Instruction import Instruction


class MyBinaryOperation:
	def __init__(self, left, right, operation):
		"""
		The result of a binary operation is always in R1.
		The left argument can always be found in R1 and the right argument can always be found in R2.
		:param left:
		:param right:
		:param operation:
		"""
		self.left = left
		self.right = right
		self.operation = operation
		self.instructions = []

	def _get_operator(self):
		if self.operation == "+":
			return "OPT"  # >=
		elif self.operation == "-":
			return "AFT"  # <=
		elif self.operation == "*":
			return "VER"  # >
		elif self.operation == "/":
			return "DEL"  # <
		else:
			raise Exception("Invalid operator.")

	def add_to_body(self, instructions):
		self.instructions.extend(instructions)

	def get_instructions(self, function=None, memory_allocation=None):
		operator = self._get_operator()
		# if not memory_allocation.in_register(self.left.name):
		# 	address = memory_allocation.get_address_by_variable_name(self.left.name, function)
		# 	self.instructions.append(Instruction(opcode="HIA", acc="Rx", operand=address))
		# if not memory_allocation.in_register(self.right.name):
		# 	address = memory_allocation.get_address_by_variable_name(self.right.name, function)
		# 	self.instructions.append(Instruction(opcode="HIA", acc="Ry", operand=address))
		# comment = self.left.name + " " + self.operation + " " + self.right.name
		self.instructions.append(Instruction(opcode=operator, acc=Register(1), operand=Register(2)))
		return self.instructions
