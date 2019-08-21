#solution #1:iterative method
Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
  def secondLargest(self, root):
    """
    input: TreeNode root
    return: int
    """
    
    # write your solution here
    import sys
    if not root:
      return None
    if not root.left and not root.right:
      return -sys.maxsize-1

    
    current = root
    while current:
      # the second case: the largest node have left subtree find the largest node
      if current.left and not current.right:
        return self.find_largest(current.left)
      # the current.right is the largest node
      if current.right and not current.right.left and not current.right.right:
        return current.val
      current = current.right
      
   def find_largest(self, root):
    if not root:
      return None
    if not root.right:
      return root.val
    return self.find_largest(root.right)
