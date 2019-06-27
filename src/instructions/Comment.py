from instructions.Instruction import Instruction


class Comment(Instruction):
    def __init__(self, comment):
        super().__init__(comment=comment)

    def __str__(self):
        return self.comment