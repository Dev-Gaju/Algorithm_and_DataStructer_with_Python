class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


"""Provide tree and its utility function"""


class BinaryTree:
    def __init__(self):
        self.root = None

    def Insert_values(self, val):
        new_node = TreeNode(val)
        if self.root is None:
            self.root = new_node
            return
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if node.left is None:
                node.left = new_node
                return
            elif node.right is None:
                node.right = new_node
                return
            else:
                queue.append(node.left)
                queue.append(node.right)

    def build_tree(self, vals):
        for val in vals:
            self.Insert_values(val)


def pre_order(root):
    if not root:
        return
    print(root.val, end=" ")
    pre_order(root.left)
    pre_order(root.right)


def Post_order(root):
    if not root:
        return
    Post_order(root.left)
    Post_order(root.right)
    print(root.val, end=" ")


def Inorder(root):
    if not root:
        return
    Inorder(root.left)
    print(root.val, end=" ")
    Inorder(root.right)


def label_wise_print(root):
    if not root:
        return
    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.val, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


def search_node(node, value):
    if node is None:  # tree is empty or value not found
        return False
    if node.val == value:  # value found at current node
        return True
    # search left subtree and right subtree recursively
    return search_node(node.left, value) or search_node(node.right, value)


tree = BinaryTree()
# values =['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
# tree.build_tree(values)
#
# pre_order(tree.root)
# print("\n")
# Inorder(tree.root)
# print("\n")
# label_wise_print(tree.root)
if search_node(tree.root, 5):
    print("Value found in tree")
else:
    print("Value not found in tree")
