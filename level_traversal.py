Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
  def levelOrderBottom(self, root):
    """
    input: TreeNode root
    return: Integer[]
    """
    # write your solution here
    if not root:
      return []
    res = [[root.val]]
    q = [root]
    while q:
      temp =[]
      value = []
      for node in q:
       if node.left:
        temp.append(node.left)
        value.append(node.left.val)
       if node.right:
        temp.append(node.right)
        value.append(node.right.val)
      q = temp
      if value:
        res.append(value)
    return res[-1]
