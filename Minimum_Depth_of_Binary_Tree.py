 Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
  def minDepth(self, root):
    """
    input: TreeNode root
    return: int
    """
    # write your solution here
    if not root:
      return 0
    if not root.left and not root.right:
      return 1
    left = self.minDepth(root.left) if root.left else float('inf')
    right = self.minDepth(root.right) if root.right else float('inf')
    return 1 + min(left, right)
    
    # solution #2:(why it doesn't work)
  class Solution(object):
  def minDepth(self, root):
    """
    input: TreeNode root
    return: int
    """
    # write your solution here
    if not root:
      return 0
    left = self.minDepth(root.left)
    right = self.minDepth(root.right)
    return 1 + min(left, right)
