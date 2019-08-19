 Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
  def isTweakedIdentical(self, one, two):
    """
    input: TreeNode one, TreeNode two
    return: boolean
    """
    # write your solution here
    if not one and not two:
      return True
    if not one or not two:
      return False
    # verify the root value same or not 
    if one.val != two.val:
      return False
    # verify the original left and right child is same
    if self.isTweakedIdentical(one.left, two.left) and self.isTweakedIdentical(one.right, two.right):
      return True
    # verify the tweaked left and right child is same
    if self.isTweakedIdentical(one.left, two.right) and self.isTweakedIdentical(one.right, two.left):
      return True
    return False
