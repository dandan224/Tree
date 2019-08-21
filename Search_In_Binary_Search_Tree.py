Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
  def search(self, root, key):
    """
    input: TreeNode root, int key
    return: TreeNode
    """
    # write your solution here
    if not root:
      return None
    
    if key < root.val:
      return self.search(root.left, key)
    elif key > root.val:
      return self.search(root.right, key)
    else:
      return root
