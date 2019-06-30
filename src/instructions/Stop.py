from instructions.Instruction import Instruction


class Stop(Instruction):
    def __init__(self):
        super().__init__(opcode='STP')