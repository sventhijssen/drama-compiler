from Register import Register
from instructions.Instruction import Instruction


class MyConstant:
	def __init__(self, value):
		self.value = value
		self.instructions = []

	def get_instructions(self, function=None, memory_allocation=None):
		memory_allocation.set_active_register(Register(1))
		self.instructions.append(Instruction(opcode='HIA', modus='w', acc='R1', operand=self.value, comment='R1 <- ' + str(self.value)))
		return self.instructions