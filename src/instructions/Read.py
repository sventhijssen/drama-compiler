from instructions.Instruction import Instruction


class Read(Instruction):
    def __init__(self):
        super().__init__(opcode="LEZ", comment="getint()")

    def __str__(self):
        return "\t\tLEZ\t\t\t\t| getint()"