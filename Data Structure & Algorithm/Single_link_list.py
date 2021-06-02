class Node:
    def __init__(self, val):
        self.next = None
        self.val = val


class Single_link_list:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_node(self, val):
        node = Node(val)
        if self.head is None:
            self.head = node
            self.tail = node
            self.size += 1
        else:
            self.tail.next = node
            self.tail = node
            self.size +=1


    def remove_node(self, val):
        node = self.head
        if node.val ==val:
            self.head = node.next
            return
        prev = None
        while node.val !=val :
            prev = node
            node = node.next
        if node is None:
            return
        prev.next = node.next



    #delete with position
    def position_delete(self, pos):
        node = self.head
        if pos ==0:
            self.head = node.next
            return
        prev = None
        count = 0
        while node and count !=pos:
            prev = node
            node = node.next
            count +=1
        if node is None:
            return
        prev.next = node.next







    def __str__(self):
        values = []
        node = self.head
        while node is not None:
            values.append(node.val)
            node = node.next
        return f"[{', '.join(str(val) for val in values)}]"

single_list=Single_link_list()
single_list.add_node(2)
single_list.add_node(5)
single_list.add_node(4)
single_list.add_node(9)
print(single_list)
# print(single_list.size)
# single_list.remove_node(2)
single_list.position_delete(1)
print(single_list)