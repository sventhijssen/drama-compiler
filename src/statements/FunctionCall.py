from instructions.Instruction import Instruction
from Stack import Stack
from instructions.Read import Read


class FunctionCall:
	def __init__(self, name, arguments):
		self.name = name
		self.arguments = arguments
		self.instructions = []

	def get_instructions(self, function=None, memory_allocation=None):
		"""
		Calling a method consists of the steps:
		a) Save R0, R1 ... if necessary
		b) Allocate memory for result on heap if necessary
		c) Pass parameters by means of register of heap if necessary
		d) Set up environment
		e) Go to subroutine (SBR)
		f) Recover environment
		g) Remove parameters from heap if necessary
		h) Remove result if necessary
		i) Restore registers if necessary

		:return:
		"""

		if self.name == 'getint':
			memory_allocation.set_active_register(0)
			self.instructions.append(Read())
		elif self.name == 'printint':
			memory_allocation.set_active_register(0)
			self.instructions.append(Instruction(opcode='DRU'))
		else:
			# d) Set up environment
			self.instructions.append(Instruction(opcode="BST", acc="R8", comment='vorige R8'))
			self.instructions.append(Instruction(opcode="HIA", acc="R8", operand="R9", comment='omgeving opzetten'))

			# e) Go to subroutine (SBR)
			self.instructions.append(Instruction(opcode="SBR", name=self.name))

			# f) Recover environment
			self.instructions.append(Instruction(opcode="HST", acc="R8", comment='omgeving herstellen'))
		return self.instructions
