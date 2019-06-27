from instructions.Instruction import Instruction
from Stack import Stack


class Declaration:
	def __init__(self, name, variable_type, value, size, global_variable=True, register=False):
		self.name = name
		self.variable_type = variable_type
		self.value = value  # init
		self.global_variable = global_variable
		self.register = register
		self.size = size
		self.stack = Stack()

	def get_size(self):
		return self.size

	def is_global_variable(self):
		return self.global_variable

	def in_register(self):
		return self.register

	def get_instructions(self):
		"""
		If the register directive is given, we will store it in a register.
		Otherwise, we will either allocate memory if it is a global variable or
		??? heap of stack ???
		:return:
		"""
		if self.in_register():
			return Instruction(opcode="HIA", modus="w", acc=self.size, comment="")
		elif not self.in_register() and self.is_global_variable():
			return Instruction(name=self.name, opcode="RESGR", acc=self.size)
		else:
			return Instruction(opcode="AFT", modus="w", acc="R9", operand="1", comment='variabele ' + self.name)
