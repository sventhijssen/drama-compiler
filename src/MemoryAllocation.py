class MemoryAllocation:
    def __init__(self):
        """
        Registers to be used for variables or computations: R1, R2, R3, R4, R5, R6
        Registers reserved: R0 (I/O), R7, R8, R9
        """
        self.nr_registers = 7
        self.registers = [None for i in range(self.nr_registers)]
        self.variables = dict()

    def allocate(self, variable):
        """
        :param variable:
        :return:
        """

        if variable.in_register():
            for i in range(self.nr_registers-1):
                if self.registers[i] is not None:
                    self.registers[i] = variable
                    self.variables[variable.name] = i
                    return
            raise Exception("All registers are full")
        else:
            pass

    def get_address(self, variable):
        if variable.in_register():
            return self.variables[variable.name]  # Return register location
