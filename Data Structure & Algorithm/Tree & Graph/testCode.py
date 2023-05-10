from Tree_with_All import BinaryTree


def NodeSUm(root):  # how many label a tree have
    if not root:
        return 0
    a = NodeSUm(root.left)
    b = NodeSUm(root.right)
    return a+b+root.val


tree = BinaryTree()
# values = ['A', 'B', "C", "D", "E", "F", "G"]
values = [1, 2, 3, 4, 5, 6, 9]
tree.build_tree(values)
print(NodeSUm(tree.root))
