from instructions.Instruction import Instruction


class EmptyLine(Instruction):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return ""
