class Instruction:
    def __init__(self, name=None, opcode=None, modus=None, acc=None, idx=None, operand=None, comment=None):
        if name is None:
            self.name = '\t\t'
        else:
            self.name = str(name) + ':\t'

        if opcode is None:
            self.opcode = ''
        else:
            self.opcode = str(opcode)

        if modus is None:
            self.modus = '\t'
        else:
            self.modus = '.' + str(modus)

        if acc is None:
            self.acc = ''
        else:
            self.acc = str(acc)

        if idx is None:
            self.idx = ''
        else:
            self.idx = '(' + str(idx) + ')'

        if operand is None:
            self.operand = ''
        else:
            self.operand = ', ' + str(operand)

        if comment is None:
            self.comment = ''
        else:
            self.comment = '\t| ' + comment

    def __str__(self):
        return self.name + self.opcode + self.modus + '\t' + self.acc + self.idx + self.operand + self.comment

