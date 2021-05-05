from Tree_Printer import BinaryTreePrinter
from stack import Stack
class TreeNode:
    def __init__(self,val):
        self.left=None   #left chile
        self.right= None  #right child
        self.val = val

class BinarySearchTree:
    def __init__(self):
        self.root = None
    def __insert_value(self, node, value):   #helper function of recursion
        if node is None:      # Never have duplcate value
            return
        if node.val == value:
            return
        elif value < node.val:
            if node.left is None:    #check left node none or not
                node.left=TreeNode(value)
                return
            self.__insert_value(node.left, value)
        else:
            if node.right is None:   #check right node none or not
                node.right = TreeNode(value)
                return
            self.__insert_value(node.right, value )


    def insert(self, val):   #1st work with recursively
        if self.root is None:
            self.root = TreeNode(val)
        else:
            self.__insert_value(self.root, val)

    def __str__(self):
        tree_printer = BinaryTreePrinter()
        return tree_printer.get_tree_string(self.root)

#In Order Travrsal
    def __in_order(self, node):   #heler of inorder
        if node is None:
            return
        self.__in_order(node.left)   #print left item
        print(node.val, end=" ")
        self.__in_order(node.right)

    def inorder(self):
        self.__in_order(self.root)


    def contrains(self, val):         #dfs start for binary tree
        nodes = Stack()
        nodes.push(self.root)

        while not nodes.isEmpty():
            node= nodes.pop()
            print("checking Node :", node.val)
            if node.val ==val:
                return  True

            elif  val < node.val:
                if node.left is not None:
                    nodes.push(node.left)
            else:
                if node.right is not None:
                    nodes.push(node.right)
        return False


bst = BinarySearchTree()
for i in [6,2,3,9,5,7,4,0,1]:
    bst.insert(i)
    print(bst)


#inOrder Print
bst.inorder()

#DFS check
print("Contains 10 ", bst.contrains(5) )    #shift tab for back index

