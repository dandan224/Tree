# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
  def isSymmetric(self, root):
    """
    input: TreeNode root
    return: boolean
    """
    # write your solution here
    if not root:
      return True
    return self.helper(root.left, root.right)
    


  def helper(self, root1, root2):
    if not root1 and not root2:
      return True
    if not root1 or not root2:
      return False
    if root1.val != root2.val:
      return False
    return self.helper(root1.left, root2.right) and self.helper(root1.right, root2.left)
