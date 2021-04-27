from queue import Queue
from Tree_Printer import BinaryTreePrinter
class TreeNode:
    def __init__(self,val):
        self.left=None   #left chile
        self.right= None  #right child
        self.val = val

class  Binary_Tree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
           self.root =TreeNode(val)
        else:
            nodes = Queue()                            #use Queue here to add depth
            nodes.enqueue(self.root)

            while True:
                checking_node =nodes.deque()
                if checking_node.left is None:
                    checking_node.left =TreeNode(val)
                elif checking_node.right is None :
                    checking_node.right =TreeNode(val)
                else:
                    nodes.enqueue(checking_node.left)
                    nodes.enqueue(checking_node.right)


    def __str__(self):
        tree_printer = BinaryTreePrinter()
        return tree_printer.get_tree_string(self.root)


mytree = Binary_Tree()
for c in ['a','b','c','d','e']:
    mytree.insert(c)
    print(mytree)


