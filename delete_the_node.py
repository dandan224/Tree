Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
class Solution(object):
  def deleteTree(self, root, key):
    """
    input: TreeNode root, int key
    return: TreeNode
    """
    # write your solution here
    if not root:
      return root
    if key > root.val:
      root.right = self.deleteTree(root.right, key)
    elif key < root.val:
      root.left = self.deleteTree(root.left, key)
    else:
      if not root.left:
        return root.right
      if not root.right:
        return root.left
      t = root
      root = self.find_min(root.right)
      root.right = self.del_min(t.right)
      root.left = t.left
    return root



  def find_min(self, root):
    """
    find the minimum treenode
    """
    if not root:
      return root
    if not root.left:
      return root
    return self.find_min(root.left)

  def del_min(self, root):
    """
    delete minimum treenode
    """
    if not root:
      return root
    if not root.left:
      return root.right
    root.left = self.del_min(root.left)
    return root
