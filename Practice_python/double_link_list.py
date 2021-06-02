class Node:
    def __init__(self, val):
        self.prev = None
        self.next = None
        self.val = val

class Double_Link_list:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # def add(self, val):
    #     node = Node(val)
    #     if self.tail is None:
    #         self.head = node
    #         self.tail = node
    #         self.size += 1
    #     else:
    #         self.tail.next= node
    #         node.prev = self.tail
    #         self.tail = node
    #         self.size += 1

    def add_head(self, val):
        node = Node(val)
        if self.head is None:
            self.head = node
            self.tail = node
            self.size += 1
        else:
            self.head.prev= node
            node.next = self.head
            self.head = node
            self.size += 1

    def __remove_node(self, node):
        if node.prev is None:
            self.head = node.next
        else:
            node.prev.next = node.next
        if node.next is None:
            self.tail = node.prev
        else:
            node.next.prev = node.prev

        self.size -= 1


    def remove_node(self, val):
        node = self.head
        while node is not None:
            if node.val == val:
                self.__remove_node(node)
            node = node.next



    def __str__(self):
        values = []
        node = self.head
        while node is not None:
            values.append(node.val)
            node = node.next
        return f"[{', '.join(str(val) for val in values)}]"


mylist = Double_Link_list()
mylist.add_head(2)
mylist.add_head(3)
# mylist.add(4)
# print(mylist)
# print(mylist.size)
# mylist.remove_node(3)
print(mylist)
# print(mylist.size)