from Register import Register
from instructions.Instruction import Instruction


class MyWhile:
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body
        self.body_instructions = []
        self.instructions = []

    def _get_comparator(self):
        if self.condition.operation == "<":
            return "GRG"  # >=
        elif self.condition.operation == ">":
            return "KLG"  # <=
        elif self.condition.operation == "<=":
            return "GR"  # >
        elif self.condition.operation == ">=":
            return "KL"  # <
        elif self.condition.operation == "==":
            return "NGEL"  # !=
        elif self.condition.operation == "!=":
            return "GEL"  # ==
        else:
            raise Exception("Invalid comparator.")

    def add_to_body(self, instructions):
        self.body_instructions = instructions

    def get_instructions(self, function=None, memory_allocation=None):
        comparator = self._get_comparator()
        self.instructions.append(Instruction(name="while", opcode="VGL", acc=Register(1), operand=Register(2)))  # TODO: Number loops for uniqueness
        self.instructions.append(Instruction(opcode="VSP", acc=comparator, operand="ewhile"))
        self.instructions.extend(self.body_instructions)
        self.instructions.append(Instruction(opcode="SPR", acc="while"))  # TODO: Change acc to unique name
        self.instructions.append(Instruction(name="ewhile"))  # TODO: Add following instructions
        return self.instructions
