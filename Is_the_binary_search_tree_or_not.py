# solution #1:
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
  
  # Solution#2:
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
    if not root:
      return True
    min_val = float('-inf')
    max_val = float('inf')
    return self.BST(root, min_val, max_val)
    
  def BST(self, root, min_val, max_val):
    if not root:
      return True
    if root.val <= min_val or root.val >= max_val:
      return False
    return self.BST(root.left, min_val, root.val) and self.BST(root.right, root.val, max_val)
  
  # Solution #3:by using inorder tranversal
  def isValidBST(root):
    prev = []
    res = [True]
    inorder(root, prev, res)
    return res[0]
  def inorder(root, prev, res):
    if not root:
      return
    inorder(root.left,prev,res)
    if prev[0] and prev[0] >= root.val:
      res[0] = False
    prev[0] = root.val
    inorder(root.right, prev, res)
