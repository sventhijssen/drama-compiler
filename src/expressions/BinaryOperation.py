class BinaryOperation:
	def __init__(self, left, right, operation):
		self.left = left
		self.right = right
		self.operation = operation

	def evaluate(self):
		return self.left + self.right  # TODO: Change to operation
