class Block:
	def __init__(self, statements):
		self.statements = statements

	def execute(self):
		for statement in self.statements:
			statement.execute()