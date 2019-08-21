 Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
  def lca(self, root, p, q):
    """
    input: TreeNode root, int p, int q
    return: TreeNode
    """
    # write your solution here
    if not root:
      return [p,q,None]

    if p <= root.val <= q or p >= root.val >= q:
      return [p, q, root.val]
    elif p<= root.val and q <= root.val:
      return self.lca(root.left, p, q)
    else:
      return self.lca(root.right, p, q)
   
   ###Solution #2
    if not root:
      return [p, q, None]
    if root.val == p or root.val == q:
      return [p, q, root.val]
    ltree = self.lca(root.left, p, q)
    rtree = self.lca(root.right, p, q)
    if ltree[2] and rtree[2]:
      return [p, q, root.val]
    elif not ltree[2]:
      return [p, q, rtree[2]]
    else:
      return [p, q, ltree[2]]
   
