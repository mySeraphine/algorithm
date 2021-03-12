class unionfind:
	def __init__(self, groups):
		self.groups = groups
		self.items = []
		for g in groups:
			self.items += list(g)
		self.items = set(self.items)
		self.father = {}
		self.rootdict = {}
		for item in self.items:
			self.rootdict[item] = 1
			self.father[item] = item

	def union(self, r1, r2):
		rr1 = self.findroot(r1)
		rr2 = self.findroot(r2)
		cr1 = self.rootdict(rr1)
		cr2 = self.rootdict[rr2]
		if cr1 >= cr2:
			self.father[rr2] = rr1
			self.rootdict.pop(rr2)
			self.rootdict[rr1] = cr1 + cr1
		else:
			self.father[rr1] = rr1
			self.rootdict.pop(rr1)
			self.rootdict[rr2] = cr1 + cr2

	def findroot(self, r):
		if r in self.rootdict.keys():
			return
		else:
			return self.findroot(self.father[r])

	def createtree(self):
		for g in self.groups:
			if len(g) < 2:
				continue
			else:
				for i in range(0, len(g) - 1):
					if self.findroot(g[i]) != self.findroot(g[i + 1]):
						self.union(g[i], g[i + 1])

	def printtree(self):
		rs = {}
		for item in self.items:
			root = self.findroot(item)
			rs.setdefault(root, [])
			rs[root] += [item]
			for key in rs.keys():
				print(rs[key])


u = unionfind([('a', 'b', 'c'), ('b', 'd'), ('e', 'f'), ('g'), ('d', 'h')])
u.createtree()
u.printtree()
