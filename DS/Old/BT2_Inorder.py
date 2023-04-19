
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.right = None
        self.left = None

class Solution(object):
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        res = []
        self.helper(root, res)
        return res

    def helper(self, root: TreeNode, res: list[int]):
        if root != None:
            self.helper(root.left, res)
            res.append(root.val)
            self.helper(root.right,res)


