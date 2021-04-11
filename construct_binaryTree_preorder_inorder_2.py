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
        dict = {}
        for i, e in enumerate(inorder):
            dict[e] = i

        root = self.helper(preorder[::-1], inorder, 0, len(inorder), dict)
        return root

    def helper(self, preorder, inorder, left_pointer, right_pointer, dict):
        if left_pointer >= right_pointer:
            return None
        else:
            num = preorder.pop()
            root = Node(num)
            idx = dict.get(num)
            root.left = self.helper(preorder, inorder, left_pointer, idx, dict)
            root.right = self.helper(preorder, inorder, idx + 1, right_pointer, dict)

        return root


preorder = [1, 2, 4, 8, 9, 5, 10, 11, 3, 6, 7]
inorder = [8, 4, 9, 2, 10, 5, 11, 1, 6, 3, 7]
tree = Solution()
binaryTree = tree.constructBinaryTree(preorder, inorder)
tree.preorder(binaryTree)
