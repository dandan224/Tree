#Solution #1: by using recursion
Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
  def closest(self, root, target):
    """
    input: TreeNode root, int target
    return: int
    """
    # write your solution here
    if not root:
      return root
    # create a variable to store the current cloest number
    res = root.val
    if root.val < target and root.right:
      right = self.closest(root.right,target)
      if abs(res - target) > abs(right -target):
        res = right
    elif root.val > target and root.left:
      left = self.closest(root.left, target)
      if abs(res - target) > abs(left - target):
        res = left
    return res
