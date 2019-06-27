from instructions.Instruction import Instruction


class EndProgram(Instruction):
    def __init__(self):
        super().__init__(opcode="EINDPR")