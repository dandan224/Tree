 ##Solution #1: Top-down method
 Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
  def exist(self, root, target):
    """
    input: TreeNode root, int target
    return: boolean
    """
    # write your solution here
    self.target = target
    self.ret = False
    self.helper(root, 0)
    return self.ret
  def helper(self, root, current):
    # current not include root
    if root is None:
      return
    if root.left is None and root.right is None:
      self.ret = self.ret or (current + root.val == self.target)
    self.helper(root.left, current + root.val)
    # how the current and root.val change
    self.helper(root.right, current + root.val)
    return

