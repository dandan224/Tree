# Solution #1(iterative method)
Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
  def postOrder(self, root):
    """
    input: TreeNode root
    return: Integer[]
    """
    # write your solution here
    output = []
    if not root:
      return output
    stack = [(root, 1)]
    while stack:
      node, count = stack.pop()
      if count == 3:
        output.append(node.val)
      if count == 1:
        stack.append((node, count + 1))
        if node.left:
          stack.append((node.left, 1))
      if count == 2:
        stack.append((node, count + 1))
        if node.right:
          stack.append((node.right, 1))
     
    return output
