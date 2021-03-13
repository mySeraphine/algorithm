class UnionFind:
	def __init__(self, data_list):
		# 初始化，father表示指向父节点的指针，height表示当前节点在树内高度，set_count表示并查集中集合个数
		self.father = {}
		self.height = {}
		self.set_counts = len(data_list)

		# 每个节点指针初始化为指向自己的指针，高度为1的树
		for d in data_list:
			self.father[d] = d
			self.height[d] = 1

	def find(self, d):
		parent = self.father[d]
		if d != parent:  # 如果d不是父节点
			parent = self.find(parent)  # 使用递归方式寻找根节点
		self.father[d] = parent  # 使用路径压缩
		return parent

	# 查找两个节点是否在同一个集合
	def isSameSet(self, a, b):
		return self.find(a) == self.find(b)

	# 合并两个集合
	def union(self, a, b):
		if not a or not b: return
		aHead = self.find(a)
		bHead = self.find(b)

		if (aHead != bHead):
			aHeight = self.height[aHead]  # a的集合数
			bHeight = self.height[bHead]  # b的集合数
			if aHeight >= bHeight:  # 如果a比b大
				self.father[bHead] = aHead  # 将b合并入a
				if aHeight == bHeight:
					self.height[aHeight] += 1  # a的集合数加1
				else:
					self.father[aHead] = bHead  # 否则将a并入b

		self.set_counts -= 1  # 总集合数-1


if __name__ == "__main__":
	a = [1, 2, 3, 4, 5]
	ufs = UnionFind(a)
	ufs.union(1, 2)
	ufs.union(3, 5)
	ufs.union(3, 1)
	ufs.union(4, 5)
	print(ufs.set_counts)
	print(ufs.isSameSet(2, 5))
	print(ufs.father)
	print(ufs.height)
