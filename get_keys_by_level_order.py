Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
  def layerByLayer(self, root):
    """
    input: TreeNode root
    return: int[][]
    """
    # write your solution here
    if root == None:
      return []
    res = [[root.val]]
    # store the root in queue
    q = [root]
    #next = []
    #line = []
    while q:
      # store the pointer of the left and right child
      temp = []
      # store the value of the left and right child
      value =[]
      # for the available nodes in the queue
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
    return res
