from instructions.Instruction import Instruction
from Stack import Stack


class FunctionCall:
	def __init__(self, name, arguments):
		self.name = name
		self.arguments = arguments
		self.stack = Stack()

	def compile(self):
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

		# d) Set up environment
		self.stack.push(Instruction(opcode="BST", acc="R8", comment='vorige R8'))
		self.stack.push(Instruction(opcode="HIA", acc="R8", operand="R9", comment='omgeving opzetten'))

		# e) Go to subroutine (SBR)
		self.stack.push(Instruction(opcode="SBR", name=self.name))

		# f) Recover environment
		self.stack.push(Instruction(opcode="HST", acc="R8", comment='omgeving herstellen'))

		pass