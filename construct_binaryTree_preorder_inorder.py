# this is not an effective approach as it takes O(n^2) as it first takes O(n)
# in pop first element from list and the searching for that element
# and then slicing cause it O(n) 

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Solution:
    def preorder(self, start):
        if start is None:
            return

        print(start.data)
        self.preorder(start.left)
        self.preorder(start.right)


    def constructBinaryTree(self, preorder: list[int], inorder: list[int]):
        if len(inorder) == 0:
            return
        if len(preorder) == 1:
            return Node(preorder[0])
        idx = inorder.index(preorder.pop(0))  # pop element from preorder and save the index of it in inorder.
        root = Node(inorder[idx])  # created a node of popped element from inorder list

        root.left = self.constructBinaryTree(preorder, inorder[:idx])
        root.right = self.constructBinaryTree(preorder, inorder[idx + 1:])

        return root


preorder = [1, 2, 4, 8, 9, 5, 10, 11, 3, 6, 7]
inorder = [8, 4, 9, 2, 10, 5, 11, 1, 6, 3, 7]
tree = Solution()
root = tree.constructBinaryTree(preorder, inorder)
tree.preorder(root)
