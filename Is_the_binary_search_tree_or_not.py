Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
  def isBST(self, root):
    """
    input: TreeNode root
    return: boolean
    """
    # write your solution here
    return self.helper(root)[0]

  def helper(self, root):
    if not root:
      return (True, None, None)
    left_res = self.helper(root.left)
    right_res = self.helper(root.right)
    # verify the left_res and the right_res is BST or not, if not, return False
    if not left_res[0] or not right_res[0]:
      return (False, None, None)
    # verify the root is greater than the left_res[2], if not, return False
    if left_res[2] and left_res[2] >= root.val:
      return (False, None, None)
    # verify the root is less than the right_res[1], if not, return False
    if right_res[1] and right_res[1] <= root.val:
      return (False, None, None)
    # return(True, the minimum of the root, the maximum of the root)
    return (True, left_res[1] or root.val, right_res[2] or root.val)
