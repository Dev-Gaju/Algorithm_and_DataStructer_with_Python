class Node:
    def __init__(self, value):
        self.next = None
        self.val = value
        self.prev = None


class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, value):
        node = Node(value)
        if self.tail is None:
            self.head = node
            self.tail = node
            self.size += 1
        else:
            self.tail.next = node
            self.tail = node
            self.size += 1

    def __remove_node(self, node):

        if node.next is None:
            self.head = node
        else:
            self.head = node.next

    def remove(self, value):
        node = self.head
        while node is not None:
            if node.val == value:
                self.__remove_node(node)
            node = node.next

    def __str__(self):
        vals = []
        node = self.head
        while node is not None:
            vals.append(node.val)
            node = node.next
        return f"[{', '.join(str(val) for val in vals)}]"


a = SingleLinkedList()
a.add(5)
a.add(9)
a.add(3)
print(a)
print(a.size)
a.remove(5)
print(a)
