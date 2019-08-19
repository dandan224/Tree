global_max = -1
res = None
def findMaxDiff(root):
    if not root:
        return 0
    left_total = findMaxDiff(root.left)
    right_total = findMaxDiff(root.right)
    global global_max
    global res
    if abs(left_total - right_total) > global_max:
        global_max = abs(left_total - right_total)
        res = root
    return left_total + right_total + 1
def max_diff(root):
    global global_max
    global res
    findMaxDiff(root)
    return res
    
