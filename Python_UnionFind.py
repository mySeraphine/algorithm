class UnionFind:
	def __init__(self, nums):
		self.father = list(range(nums))
		self.size = [1] * nums

	def union(self, x, y):
		px = self.find(x)
		py = self.find(y)

		if self.size[px] > self.size[py]:
			px, py = py, px

			self.father[px] = py
			self.size[py] += self.size[px]

	def find(self, x):
		r = x
		while self.father[r] != r:
			r = self.father[r]
			i = x
			while i != r:
				tmp=self.father[i]
				self.father[i] = r
				i = tmp
		return r

	def find_recur(self, x):
		if self.father[x] != x:
			self.father[x] = self.find(x)
		return self.father[x]


uf = UnionFind(10)
print(uf.father)

uf.find(1)
print("执行find之后：", uf.father)
uf.union(1,2)
print("执行Union之后：", uf.father)
uf.union(2,3)
print("执行Union之后：", uf.father)
uf.union(3, 4)
print("执行Union之后：", uf.father)

for i in uf.father:
	print(uf.find(i))
