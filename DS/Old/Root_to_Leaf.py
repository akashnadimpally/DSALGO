class TreeNode(object):
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


class Solution(object):
    def binaryTreePaths(self, root: TreeNode, targetSum: int):
        if root is None:
            return []
        if (root.left == None and root.right == None):
            return [str(root.val)]

        # subtree is always a list, though it might be empty
        left_subtree = self.binaryTreePaths(root.left, targetSum)
        right_subtree = self.binaryTreePaths(root.right, targetSum)
        full_subtree = left_subtree + right_subtree  # the last part of comprehension

        list1 = []
        for leaf in full_subtree:  # middle part of the comprehension
            list1.append(root.val)  # the left part

        for i in list1:
            if (sum(i) == targetSum):
                return True
            else:
                return False


target = 21

root = TreeNode(10)
s = Solution()
root.left = TreeNode(8)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(5)
root.right.left = TreeNode(2)
print(s.binaryTreePaths(root, target))

# n = [5,4,8,11,null,13,4,7,2,null,null,null,1]

