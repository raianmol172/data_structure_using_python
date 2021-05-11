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



root = Node(26)
root.left = Node(10)
root.right = Node(3)
root.right.right = Node(3)
root.left.left = Node(6)
root.left.right = Node(4)


if isSumTree(root) != -sys.maxsize:
	print("Binary tree is a sum tree")
else:
	print("Binary tree is not a sum tree")
