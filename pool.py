class Pool():
	def __init__(self):
		with open('channels.txt') as f:
			pool = f.read().split()
		pool = [x.strip() for x in pool]
		pool = [x for x in pool if x]
		self.pool = {x:1 for x in pool}

	def update(self, name, pos):
		if self.pool[name] == pos:
			del self.pool[name]
		self.pool[name] = pos

	def items(self):
		return [(x, self.pool[x]) for x in self.pool]
