Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
  def isIdentical(self, one, two):
    """
    input: TreeNode one, TreeNode two
    return: boolean
    """
    # write your solution here
    if not one and not two:
      return True
    if one is not None and two is not None:
      return one.val == two.val and \
      self.isIdentical(one.left, two.left) and self.isIdentical(one.right,two.right)
    
    return False
