Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
  def findHeight(self, root):
    """
    input: TreeNode root
    return: int
    """
    # write your solution here
    if not root:
      return 0
    left = self.findHeight(root.left)
    right = self.findHeight(root.right)
    return 1 + max(left,right)
