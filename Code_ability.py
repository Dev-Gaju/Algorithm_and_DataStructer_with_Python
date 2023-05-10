class Tree:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


class BuildTree:
    def __init__(self):
        self.root = None

    def insertVal(self, val):
        newNode = Tree(val)

        if self.root is None:
            self.root = newNode
            return
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if node.left is None:
                node.left = newNode
                return
            elif node.right is None:
                node.right = newNode
                return
            else:
                queue.append(node.left)
                queue.append(node.right)

    def buildTree(self, values):
        for val in values:
            self.insertVal(val)


def preOrder(root):
    if root is None:
        return
    print(root.val, end=" ")
    preOrder(root.left)
    preOrder(root.right)


def Inorder(root):
    if root is None:
        return
    Inorder(root.left)
    print(root.val, end=" ")
    Inorder(root.right)


def labelWisePrint(root):
    if root is None:
        return
    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.val, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)


tree = BuildTree()
valus = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
tree.buildTree(valus)
preOrder(tree.root)
print("\n")
Inorder(tree.root)
print('\n')
labelWisePrint(tree.root)
