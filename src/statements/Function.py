from functools import reduce

from instructions.Instruction import Instruction
from Stack import Stack
from statements.Declaration import Declaration


class Function:
	# Add variables and their addresses to the allocation table
	# The keyword 'register' indicates the variable must be stored in a register,
	# otherwise it is stored on the stack
	def __init__(self, name, parameters, body):
		self.name = name
		self.parameters = parameters
		self.body = body
		self.allocation_table = {}
		self.stack = Stack()

	def _get_declarations(self):
		"""
		Returns a list of the declarations in the body of this function.
		:return:
		"""
		return filter(lambda s: isinstance(s, Declaration), self.body.statements)

	def _get_declarations_not_in_register(self):
		"""
		Returns a list of the declarations which will be stored not in a register.
		:return:
		"""
		return filter(lambda d: not d.in_register(), self._get_declarations())

	def _get_local_variable_size(self):
		"""
		Returns the size of memory allocation needed for all declarations.
		:return:
		"""
		return reduce(lambda x, y: x.size() + y.size(), self._get_declarations_not_in_register())

	def execute(self):
		"""
		The execution of a method consists of the following steps:
		a) Allocate space for local variables which are not stored in registers if necessary
		b) Save registers R3, R4, ... if they are being used by this function
		c) Execute body
		c) Save the results in a register of on the heap if necessary
		d) Restore registers R3, R4, ... if necessary
		e) Remove local variables from the heap if necessary
		f) Return (KTG)
		:return:
		"""

		# a) Allocate space for local variables which are not stored in registers if necessary
		for declaration in self._get_declarations_not_in_register():
			self.stack.push(Instruction(opcode="AFT", modus="w", acc="R9", operand="1", comment='variabele ' + declaration.name))

		self.body.execute()

		# e) Remove local variables from the heap if necessary
		for declaration in self._get_declarations_not_in_register():
			self.stack.push(Instruction(opcode="OPT", modus="w", acc="R9", operand="1", comment='variabele ' + declaration.name))

		# f) Return
		self.stack.push("KTG")
		return self.stack

		# if self.name == 'main':
		# 	stack.push(Instruction(opcode='HIA', modus='a', acc='R7', operand='heap'))
		# 	stack.push(Instruction(opcode='BST', acc='R0'))
		# 	stack.push(Instruction(opcode='HIA', acc='R8', operand='R9'))
		# 	stack.push(Instruction(opcode='BST', acc='R0'))
		# 	stack.push(Instruction(name='main', opcode='HIA', modus='w', acc='R0', operand='-1'))
		#
		#
		# for e in self.body:
		# 	if isinstance(e, Decl):


