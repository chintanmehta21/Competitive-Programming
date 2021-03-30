"""
A Binary tree is a data structure in which there is a parent object and each object can have zero, one or two children
"""

class Node():
	def __init__(self, data1):
		self.data = data1
		self.left = None
		self.right = None

class Tree():
	def __init__(self, data2 = None):
		if data2:
			self.root = Node(data2)

		else:
			self.root = None

	def insert(self, data3):
		#self.new_node = Node(data3)
		if not self.root:
			self.root = Node(data3)
		else:
			self.helper(data3, self.root)

	def helper(self, data4, cur_node):
		self.cur_node = cur_node
		if data4 < self.cur_node.data:
			if not self.cur_node.left:
				self.cur_node.left = Node(data4)
			else:
				self.helper(data4, self.cur_node.left)
		elif data4 > self.cur_node.data:
			if not self.cur_node.right:
				self.cur_node.right = Node(data4)
			else:
				self.helper(data4, self.cur_node.right)

	def inorder(self, start, traversal):
		if start:
			traversal = self.inorder(start.left, traversal)
			traversal += str(start.data) + "  "
			traversal = self.inorder(start.right, traversal)
		return traversal

	def preorder(self, start, traversal):
		if start:
			traversal += str(start.data) + "  "
			traversal = self.inorder(start.left, traversal)
			traversal = self.inorder(start.right, traversal)
		return traversal

	def postorder(self, start, traversal):
		if start:
			traversal = self.inorder(start.left, traversal)
			traversal = self.inorder(start.right, traversal)
			traversal += str(start.data) + "  "
		return traversal

t1 = Tree(10)
t1.insert(13)
t1.insert(11)
t1.insert(9)
t1.insert(15)
t1.insert(6)
t1.insert(8)
print("Inorder Traversal : ")
print(t1.inorder(t1.root, " "))
print("Preorder Traversal : ")
print(t1.preorder(t1.root, " "))
print("Postorder Traversal : ")
print(t1.postorder(t1.root, " "))