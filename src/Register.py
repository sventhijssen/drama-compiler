class Register:
    def __init__(self, number, value=None):
        self.number = number
        self.value = value

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def __str__(self):
        return 'R' + str(self.number)

    def __eq__(self, other):
        return isinstance(other, Register) and self.number == other.number
