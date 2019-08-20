Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
  def insert(self, root, key):
    """
    input: TreeNode root, int key
    return: TreeNode
    """
    # write your solution here
    if not root:
      return TreeNode(key)
    if key < root.val:
      root.left = self.insert(root.left, key)
    elif key > root.val:
      root.right = self.insert(root.right, key)
    else:
      return root
    return root
