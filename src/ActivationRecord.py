from instructions.Comment import Comment


class ActivationRecord:
    def __init__(self, function):
        self.function = function
        self.instructions = []

    def get_instructions(self, memory_allocation):
        head = 'Activatierecord ' + self.function.name
        self.instructions.append(Comment(head))
        self.instructions.append(Comment(''.join('-' for i in range(len(head)))))
        self.instructions.append(Comment('...'))

        for variable in self.function.get_local_variables():
            if not variable.in_register():
                if variable.get_size() > 1:
                    for s in range(variable.get_size()-1):
                        self.instructions.append(Comment(variable.name + '[' + str(s) + ']'))
                else:
                    self.instructions.append(Comment(variable.name))

        if self.function.is_main():
            self.instructions.append(Comment('TKA = -1'))
            self.instructions.append(Comment('R8 = -1'))
        else:
            self.instructions.append(Comment('TKA'))
            self.instructions.append(Comment('oude R8'))
            # TODO: Add parameters
            # for variables in self.function.get_parameters():
            #     pass
            self.instructions.append(Comment('...'))
        return self.instructions
