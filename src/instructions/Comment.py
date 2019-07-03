from instructions.Instruction import Instruction


class Comment(Instruction):
    def __init__(self, comment):
        self.comment = comment

    def __str__(self):
        return "| " + str(self.comment)
