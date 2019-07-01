class MemoryAllocation:
    def __init__(self):
        """
        Registers to be used for variables or computations: R1, R2, R3, R4, R5, R6
        Registers reserved: R0 (I/O), R7, R8, R9
        """
        self.nr_registers = 7
        self.registers = [None for i in range(self.nr_registers)]
        self.variables = dict()

    def allocate(self, variable, function):
        """
        A variable is allocated as follows:
        a) If the keyword 'register' is enabled, it must be stored in a register, regardless whether it is a global
        variable or a local variable
        b) Otherwise, if it is a global variable, memory must be allocated on the heap (RESGR)
        c) Otherwise, if it is a local variable, memory must be allocated on the stack (AFT.w R9, size)
        :param function:
        :param variable:
        :return:
        """

        if variable.in_register():
            for i in range(self.nr_registers-1, 0, -1):
                if self.registers[i] is None:
                    self.registers[i] = variable
                    self.variables[variable.name] = i
                    if not variable.is_global_variable():
                        function.add_local_variable(variable)
                    return
            raise Exception("All registers are full")
        elif not variable.is_global_variable():
            # Local variable, not in register -> heap
            function.add_local_variable(variable)

    def get_address(self, variable, function):
        """
        Returns the address of a variable.
        A variable's address is calculated as follows:
        a) If the keyword 'register' is enabled, it is stored in a register, regardless whether it is a global
        variable or a local variable
        b) Otherwise, if it is a global variable, it is stored on the heap
        c) Otherwise, if it is a local variable, it is stored on the stack
        :param variable:
        :param function:
        :return:
        """
        if variable.in_register():
            return 'R' + str(self.variables[variable.name])  # Return register location
        else:
            if variable.is_global_variable():
                return variable.name
            else:
                # The local variable is stored in the stack of a function
                m = -2
                for local_variable in function.local_variables:
                    if variable == local_variable:
                        return str(m) + '(R8)'
                    else:
                        m -= local_variable.get_size()
