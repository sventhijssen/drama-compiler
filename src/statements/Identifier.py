from instructions.Instruction import Instruction


class Identifier:
    def __init__(self, name, move_to_register=False):
        self.name = name
        self.move_to_register = move_to_register
        self.instructions = []

    def get_instructions(self, function=None, memory_allocation=None):
        if self.move_to_register is not None and not memory_allocation.in_register(self.name):
            self.instructions.append(Instruction(opcode="HIA", acc=self.move_to_register, operand=self.name))
        return self.instructions
