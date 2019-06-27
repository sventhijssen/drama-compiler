from instructions.Instruction import Instruction


class ReserveMemory(Instruction):
    def __init__(self, name):
        super().__init__(name=name, opcode="RESGR", acc=1)