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
    self.result = -2147483648
    self.helper(root, self.result)
    return self.result

  def helper(self, root, result):
      if root is None:
        return 0
      if not root.left and not root.right:
        self.result = max(self.result, root.val)
        return root.val

      left = self.helper(root.left,result)
      right = self.helper(root.right,result)

      self.result = max(self.result, max(max(left, right), 0)+root.val)
      return max(max(left, right), 0) + root.val
