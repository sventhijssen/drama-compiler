from Register import Register
from instructions.Instruction import Instruction


class MyUnaryOperation:
    def __init__(self, expression, operation):
        """
        The result of a unary operation is always in R1.
        The left argument can always be found in R1 and the right argument can always be found in R2.
        :param expression:
        :param operation:
        """
        self.right = expression
        self.operation = operation
        self.instructions = []

    def _get_operator(self):
        if self.operation == "p++":  # Post increment
            return "OPT"  # >=
        elif self.operation == "p--":  # Post decrement
            return "AFT"  # <=
        elif self.operation == "++":  # Pre increment
            return "OPT"  # >
        elif self.operation == "--":  # Pre decrement
            return "AFT"  # <
        else:
            raise Exception("Invalid operator.")

    def add_to_body(self, instructions):
        self.instructions.extend(instructions)

    def get_instructions(self, function=None, memory_allocation=None):
        operator = self._get_operator()
        self.instructions.append(Instruction(opcode=operator, acc=Register(1), operand=Register(2)))
        return self.instructions
