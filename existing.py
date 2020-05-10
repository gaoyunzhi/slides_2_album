class Existing():
	def __init__(self):
		with open('existing') as f:
			self.existing = set([x.strip() for x in f.read().split()])

	def contain(self, x):
		return x.strip() in self.existing

	def add(self, x):
		x = x.strip()
		if self.contain(x):
			return False
		self.existing.add(x)
		with open('existing', 'a') as f:
			f.write('\n' + x)
		return True