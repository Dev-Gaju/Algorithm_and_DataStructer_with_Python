
#BFS and DFS very important and apply with graph or many edge  for root
from queue_check import Queue
from Tree_Printer import BinaryTreePrinter
from stack import Stack
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
            nodes = Queue()                            #use Queue here to add depth BFS
            nodes.enqueue(self.root)

            while True:
                checking_node =nodes.deque()
                if checking_node.left is None:
                    checking_node.left =TreeNode(val)
                    return
                elif checking_node.right is None :
                    checking_node.right =TreeNode(val)
                    return
                else:
                    nodes.enqueue(checking_node.left)
                    nodes.enqueue(checking_node.right)

        # when implement with normal tree
    def contrains(self, val):
        nodes = Stack()
        nodes.push(self.root)

        while not nodes.isEmpty():
            node = nodes.pop()
            print("checking Node :", node.val)
            if node.val == val:
                return True

            if node.left is not None:
                nodes.push(node.left)
            if node.right is not None:
                nodes.push(node.right)
        return False



    def __str__(self):
        tree_printer = BinaryTreePrinter()
        return tree_printer.get_tree_string(self.root)



my_tree = Binary_Tree()
for c in ['a','b','c','d','e']:
    my_tree.insert(c)
    print(my_tree)

print("contains a: ", my_tree.contrains('d'))


