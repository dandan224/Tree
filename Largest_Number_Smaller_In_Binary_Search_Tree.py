Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
  def largestSmaller(self, root, target):
    """
    input: TreeNode root, int target
    return: int
    """
    # write your solution here
    if not root:
      return -2**31
    if root.val >=target and not root.left and not root.right:
      return -2**31
    
    if root.val < target and not root.right:
      return root.val
    if root.val >= target and not root.left:
      return -2**31
    l = -2**31
    if root.val < target:
      l = self.largestSmaller(root.right, target)
      return max(root.val, l)
    if root.val >= target:
      r = self.largestSmaller(root.left, target)
      return max(r, l)
