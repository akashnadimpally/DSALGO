# Given the root of a binary tree, return the preorder traversal of its nodes' values.

class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.right = None
        self.left = None

class Solution(object):
    def PreOrderTraversal(self, root: TreeNode) -> list[int]:
        if root is None:
            return []

        stack, output = [root, ], []

        while stack:
            root = stack.pop()
            if root is not None:
                output.append(root.val)
                if root.right is not None:
                    stack.append(root.right)
                if root.left is not None:
                    stack.append(root.left)

        return output


root = [1,None,2,3]

s = Solution()
t = s.PreOrderTraversal(root)
print(t)