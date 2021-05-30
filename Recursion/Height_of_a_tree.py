
def Height_tree(root):
    if root==None:
        return 0
    left = 1
    right =1
    left= Height_tree(root+left)
    right =Height_tree(root + right)
    return 1+max(left,right)

Height_tree(5)