Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
  def maxPathSum(self, root):
    """
    input: TreeNode root
    return: int
    """
    # write your solution here
    import sys
    self.result = -sys.maxsize - 1
    self.helper(root)
    return self.result

  def helper(self, root):
      if root is None:
        return 0
      if root.left is None and root.right is None:
        return root.val
      left = self.helper(root.left)
      right = self.helper(root.right)
      if root.left and root.right:
        self.result = max(self.result, left + right + root.val)
        return max(left,right) + root.val
      else:
        return root.val + right if not root.left else root.val + left
