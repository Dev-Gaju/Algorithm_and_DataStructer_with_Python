class Tree:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def InsertVal(self, value):
        node = Tree(value)
        if self.root is None:
            self.root = node
            return
        current = self.root
        while True:
            if value < current.val:
                if current.left is None:
                    current.left = node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = node
                    return
                current = current.right

    def Invalues(self, values):
        for val in values:
            self.InsertVal(val)

    def PostOrder(self, root):
        if root is None:
            return
        self.PostOrder(root.left)
        self.PostOrder(root.right)
        print(root.val, end=" ")

    def FindPath(self, root, path):
        if not root:
            return
        path.append(root.val)
        if root.left is None and root.right is None:
            print(path)
        self.FindPath(root.left, path)
        self.FindPath(root.right, path)
        path.pop()

    def RangePrint(self, root, start, end):
        if not root:
            return
        if start < root.val:
            self.RangePrint(root.left, start, end)
        if start <= root.val <= end:
            print(root.val, end=" ")
        if end > root.val:
            self.RangePrint(root.right, start, end)

    def Search_val(self, val):
        current = self.root
        while current is not None:
            if val == current.val:
                return True
            elif val < current.data:
                current = current.left
            else:
                current = current.right
        return False


def DeleteNod(root, val):
    if root is None:
        return root
    if val < root.val:
        root.left = DeleteNod(root.left, val)
    elif val > root.val:
        root.right = DeleteNod(root.right, val)
    else:
        if root.left is None and root.right is None:
            return None
        elif root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:
            curr = root.right
            while curr.left is not None:
                curr = curr.left
            root.val = curr.val
            root.right = DeleteNod(root.right, curr.val)
    return root

bst = BinarySearchTree()
values = 5, 3, 7, 2, 4, 6, 8
bst.Invalues(values)
# bst.PostOrder(bst.root)
# bst.FindPath(bst.root, [])
# bst.RangePrint(bst.root, 3,7)
# print(bst.Search_val(5))
DeleteNod(bst.root, 3)

bst.PostOrder(bst.root)
