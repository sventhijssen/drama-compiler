from instructions.Instruction import Instruction


class MyConstant:
	def __init__(self, value):
		self.value = value

	def get_instructions(self):
		return [Instruction(opcode='HIA', modus='w', acc='R1', operand=self.value, comment='R1 <- ' + str(self.value))]