from Tree_with_All import BinaryTree


def Ancestor(root, target):  # parents nodes are ancestor of child
    if not root:
        return False
    if root.val == target:
        return True
    if Ancestor(root.left, target) or Ancestor(root.right, target):
        print(root.val, end=" ")
        return True
    return False


def subTree(root):  # Belongs to same tree but have child with root
    if not root:
        return
    print(root.val, end=" ")
    subTree(root.left)
    subTree(root.right)


def Height(root): # how many label a tree have
    if not root:
        return 0
    left_height = Height(root.left)
    right_height = Height(root.right)
    return max(left_height, right_height) + 1


def Node_count(root):  # how much node a tree have
    if not root:
        return 0
    left_count = Node_count(root.left)
    right_count = Node_count(root.right)
    total_node = left_count + right_count + 1
    return total_node


def Node_Sum(root):   # Calculate the sum of each node's values
    if not root:
        return 0
    left_sum = Node_Sum(root.left)
    right_sum = Node_Sum(root.right)
    total_sum = left_sum + right_sum + root.val
    return total_sum


def diameter(root):  # calculate distance between two node
    if not root:
        return 0
    left_height = Height(root.left)
    right_height = Height(root.right)
    root_diameter = left_height + right_height + 1  # diameter with root
    left_diameter = diameter(root.left)  # diameter on left side
    right_diameter = diameter(root.right)  # diameter on left side
    return max(root_diameter, left_diameter, right_diameter)


tree = BinaryTree()
values = ['A', 'B', "C", "D", "E", "F", "G"]
# values = [1, 2, 3, 4, 5, 6, 7]
tree.build_tree(values)
# Ancestor(tree.root, "A")
# print("\n")
# subTree(tree.root.right)
# print("\n")
# print(Node_count(tree.root))
# print("\n")
# print(Node_Sum(tree.root))
# print("\n")
print(diameter(tree.root))
