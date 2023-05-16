"""Determine which case the node falls into: leaf node, node with one child
, or node with two children.
"""
from Tree_with_All import BinaryTree, Inorder


def delete_node(root, value):
    if root is None:
        return root

    # find the node to be deleted
    if value < root.val:
        root.left = delete_node(root.left, value)
    elif value > root.val:
        root.right = delete_node(root.right, value)
    else:
        # case 1: node has no children
        if root.left is None and root.right is None:
            return None
        # case 2: node has one child
        elif root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        # case 3: node has two children
        else:
            # find the in-order successor (the smallest value in the right subtree)
            current = root.right
            while current.left is not None:
                current = current.left
            # replace the node to be deleted with the in-order successor
            root.val = current.val
            # delete the in-order successor from the right subtree
            root.right = delete_node(root.right, current.val)

    return root


tree = BinaryTree()
values = [1, 2, 3, 4, 5, 6, 7]
tree.build_tree(values)
# delete a node from the tree
tree.root = delete_node(tree.root, 3)

Inorder(tree.root)
