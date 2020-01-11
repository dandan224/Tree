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
  
  
#get_height of the tree(top_down method)
def get_height_1(root):
    if not root:
        return 0
    global result 
    result = 0
    helper(root,0)
    return result
    
def helper(root, depth):
    if not root:
        global result
        result = max(result, depth)
        return
    helper(root.left, depth + 1)
    helper(root.right, depth + 1)
    return
