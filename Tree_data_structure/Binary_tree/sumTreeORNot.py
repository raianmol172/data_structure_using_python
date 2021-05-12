import sys


class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None


def isSumTree(root):

	if root is None:
		return 0

	if root.left is None and root.right is None:
		return root.data

	# if the root's value is equal to the sum of all elements present in its

	if root.data == isSumTree(root.left) + isSumTree(root.right):
		return 2 * root.data

	return -sys.maxsize



tree = Node(26)
tree.left = Node(10)
tree.right = Node(3)
tree.right.right = Node(3)
tree.left.left = Node(6)
tree.left.right = Node(4)


if isSumTree(tree) != -sys.maxsize:
	print("Binary tree is a sum tree")
else:
	print("Binary tree is not a sum tree")
