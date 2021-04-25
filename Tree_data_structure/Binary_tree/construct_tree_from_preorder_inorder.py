class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def constructBtFromPreIn(preorder: list[int], inorder: list[int]):
    memory = {}
    for i, e in enumerate(inorder):
        memory[e] = i

    root = helper(preorder[::-1], inorder, 0, len(inorder), memory)
    return root


def helper(preorder, inorder, left_pointer, right_pointer, memory):
    if left_pointer < right_pointer:
        num = preorder.pop()
        root = Node(num)
        idx = memory.get(num)
        root.left = helper(preorder, inorder, left_pointer, idx, memory)
        root.right = helper(preorder, inorder, idx+1, right_pointer, memory)
        return root


def preorderTraversal(root):
    if root is None:
        return None
    else:
        print(root.data, end=' ')
        preorderTraversal(root.left)
        preorderTraversal(root.right)


preorder1 = [1, 2, 4, 5, 3, 6, 7]
inorder2 = [4, 2, 5, 1, 6, 3, 7]
result = constructBtFromPreIn(preorder1, inorder2)
print('after constructing the tree the preorder traversal is: ')
preorderTraversal(result)
