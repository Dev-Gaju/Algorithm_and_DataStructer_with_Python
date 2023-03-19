
from Tree_with_All import BinaryTree


def print_anchester(root, target):
    if not root:
        return False
    if root.val == target:
        return True
    if print_anchester(root.left, target) or print_anchester(root.right, target):
        print(root.val, end=" ")
        return True
    return False


def subTree(root):
    if not root:
        return
    print(root.val, end=" ")
    subTree(root.left)
    subTree(root.right)


def Height(root):
    if not root:
        return 0
    left_height = Height(root.left)
    right_height = Height(root.right)
    return max(left_height, right_height) + 1


def Node_count(root):
    if not root:
        return 0
    left_count = Node_count(root.left)
    right_count = Node_count(root.right)
    total_node = left_count + right_count + 1
    return total_node


def Node_Sum(root):
    if not root:
        return 0
    left_sum = Node_Sum(root.left)
    right_sum = Node_Sum(root.right)
    total_sum = left_sum + right_sum + root.val
    return total_sum


def diameter(root):
    if not root:
        return  0
    left_height = Height(root.left)
    right_height = Height(root.right)
    root_diameter = left_height + right_height + 1  # diameter with root
    left_diameter = diameter(root.left)  # diameter on left side
    right_diameter = diameter(root.right) # diameter on left side
    return max(root_diameter, left_diameter,right_diameter)

tree = BinaryTree()
# values = ['A', 'B', "C", "D", "E", "F", "G"]
values = [1, 2, 3, 4, 5, 6, 7]
tree.build_tree(values)
print_anchester(tree.root, "D")
print("\n")
subTree(tree.root.right)
print("\n")
print(Node_count(tree.root))
print("\n")
print(Node_Sum(tree.root))
print("\n")
print(diameter(tree.root))
