class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

"""
       5
     /   \
    3     7
   / \   / \
  2   4 6   8
"""

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return
        current = self.root
        while True:
            if data < current.data:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right

    def search(self, data):
        current = self.root
        while current is not None:
            if data == current.data:
                return True
            elif data < current.data:
                current = current.left
            else:
                current = current.right
        return False

    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.data, end=' ')
            self.inorder(node.right)

    def preorder(self, node):
        if node is not None:
            print(node.data, end=' ')
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=' ')

    def find_paths(self, node, path):
        if node is None:
            return

        path.append(node.data)

        if node.left is None and node.right is None:
            print(path)
        else:
            self.find_paths(node.left, path)
            self.find_paths(node.right, path)

    def print_in_range(self, node, start, end):
        if node is None:
            return

        if start < node.data:
            self.print_in_range(node.left, start, end)

        if start <= node.data <= end:
            print(node.data)

        if end > node.data:
            self.print_in_range(node.right, start, end)

bst = BinarySearchTree()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)
bst.insert(6)
bst.insert(8)

bst.inorder(bst.root)   # prints "2 3 4 5 6 7 8"
print("\n")
bst.preorder(bst.root)  # prints "5 3 2 4 7 6 8"
print("\n")
bst.postorder(bst.root) # prints "2 4 3 6 8 7 5"
print("\n")
bst.print_in_range(bst.root, 3, 7)
print("\n")
bst.find_paths(bst.root, [])