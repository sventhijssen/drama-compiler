from instructions.Instruction import Instruction


class MyWhile:
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body
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
        self.instructions.extend(instructions)

    def get_instructions(self, function=None, memory_allocation=None):
        comparator = self._get_comparator()
        self.instructions.append(Instruction(name="while", opcode="VSP", acc=comparator, operand="ewhile"))  # TODO: Number loops for uniqueness
        return self.instructions