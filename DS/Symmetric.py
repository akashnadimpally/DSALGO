class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirror(root.left, root.right)

    def isMirror(self,left: TreeNode, right: TreeNode):
        if (left == None or right == None):
            return True
        if (left == None and right == None):
            return False

        return (left.value == right.value) or self.isMirror(left.left, right.right) or self.isMirror(left.right, right.left)