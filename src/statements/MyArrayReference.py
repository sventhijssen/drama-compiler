class MyArrayReference:
    def __init__(self, name, subscript):
        self.name = name
        self.subscript = subscript
        self.instructions = []

    def get_instructions(self, function=None, memory_allocation=None):
        return self.instructions