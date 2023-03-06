class Node:
    def __init__(self, val):
        self.prev = None
        self.next = None
        self.val = val

class double_linkList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0    #calculate the size of link_list

    def add(self, val):
        node = Node(val)
        if self.tail is None:
            self.head = node  #head point after  this node
            self.tail = node  #tail point previous node
            self.size +=1
        else:
            self.tail.next=node  #after head means new node
            node.prev = self.tail   #introuce new node to the before node
            self.tail = node   #add new node
            self.size =+1

    def __remove_node(self, node):   #update the remove node link
        if node.prev is None:  #check head node or not
            self.head = node.next  #update head
        else:
            node.prev.next = node.next

        if node.next is None:  #same as head
            self.tail =node.prev    #previous node will be tail
        else:
            node.next.prev = node.prev
        self.size =- 1

    def remove_node(self, value):  #remove function
        node = self.head     #start from head to search the removable value
        while node is not  None:
            if node.val == value:
                self.__remove_node(node)
            node = node.next    #iteration increased


#help to print the node
    def __str__(self):
        values = []
        node = self.head
        while node is not  None:
            values.append(node.val)
            node = node.next
        return f"[{', '.join(str(val) for val in values)}]"


my_list = double_linkList()
my_list.add(1)
my_list.add(2)
my_list.add(5)
my_list.add(4)
# my_list.add(5)
print(my_list)
my_list.remove_node(2)
print(my_list)
