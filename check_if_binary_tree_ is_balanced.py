 Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
  def isBalanced(self, root):
    """
    input: TreeNode root
    return: boolean
    """
    # write your solution here
    if not root:
      return True
    left = self.get_height(root.left)
    right = self.get_height(root.right)
    if abs(left - right) > 1:
      return False
    return self.isBalanced(root.left) and self.isBalanced(root.right)



  def get_height(self, root):
    if not root:
      return 0
    left = self.get_height(root.left)
    right = self.get_height(root.right)
    return 1 + max(left,right)
