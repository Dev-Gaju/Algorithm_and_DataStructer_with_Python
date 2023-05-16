from Tree_with_All import BinaryTree


def is_subtree(s, t):  # s= source, t= subTree
    if not s and not t:  # both trees are empty
        return True
    if not s or not t:  # one tree is empty, the other is not
        return False
    if s.val == t.val:  # current nodes match, check subtrees
        return is_identical(s.left, t.left) and is_identical(s.right, t.right)
    # current nodes don't match, check left and right subtrees of s
    return is_subtree(s.left, t) or is_subtree(s.right, t)


def is_identical(s, t):
    if not s and not t:  # both trees are empty
        return True
    if not s or not t:  # one tree is empty, the other is not
        return False
    if s.val == t.val:  # current nodes match, check subtrees
        return is_identical(s.left, t.left) and is_identical(s.right, t.right)
    # current nodes don't match
    return False


s = BinaryTree()
s_values = [3, 4, 5, 1, 2]
s.build_tree(s_values)

# define the smaller tree
t = BinaryTree()
t_values = [4, 1, 2]
t.build_tree(t_values)

# check if t is a subtree of s
if is_subtree(s.root, t.root):
    print("t is a subtree of s")
else:
    print("t is not a subtree of s")