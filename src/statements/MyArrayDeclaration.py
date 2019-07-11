from instructions.Instruction import Instruction


class MyArrayDeclaration:
    def __init__(self, name, initial_value, variable_type, size, global_variable=True, register=False):
        self.name = name
        self.initial_value = initial_value
        self.variable_type = variable_type
        self.global_variable = global_variable
        self.register = False  # Never store in register
        self.size = size
        self.instructions = []

    def get_size(self):
        return self.size

    def is_global_variable(self):
        return self.global_variable

    def in_register(self):
        return self.register

    def add_to_body(self, instructions):
        self.instructions.extend(instructions)

    def get_instructions(self, function=None, memory_allocation=None):
        """
        If the register directive is given, we will store it in a register.
        Otherwise, we will either allocate memory if it is a global variable or
        ??? heap of stack ???
        :return:
        """
        if self.in_register():
            return []
        elif not self.in_register() and self.is_global_variable():
            if self.initial_value is not None:
                values = [e.value for e in self.initial_value.exprs]
                arg = '; '.join(values)
                return [Instruction(name=self.name, acc=arg)]
            return [Instruction(name=self.name, opcode="RESGR", acc=self.size)]
        else:
            return [Instruction(opcode="AFT", modus="w", acc="R9", operand="1", comment='variabele ' + self.name)]
