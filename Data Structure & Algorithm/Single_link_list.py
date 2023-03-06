class Node():
    def __init__(self, val):
        self.next = None
        self.val = val


class SingleLinkList():
    def __init__(self):
        self.head = None
        self.size = 0

    def add(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.size += 1
        else:
            temp = self.head
            while temp.next is not None:
                temp=temp.next
            temp.next=new_node

    def remove(self, val):
        if self.head is None:
            return
        if self.head.val == val:
            self.head = self.head.next
            return
        current = self.head
        while current.next is not None:
            if current.next.val == val:
                current.next = current.next.next
                return
            current = current.next


    def print_node(self):
        current = self.head
        while current is not None:
            print(current.val, end="->")
            current = current.next
        print("None")


llist = SingleLinkList()
llist.add(5)
llist.add(4)
llist.add(3)
llist.remove(4)
llist.print_node()




    # #delete with position
    # def position_delete(self, pos):
    #     node = self.head
    #     if pos ==0:
    #         self.head = node.next
    #         return
    #     prev = None
    #     count = 0
    #     while node and count !=pos:
    #         prev = node
    #         node = node.next
    #         count +=1
    #     if node is None:
    #         return
    #     prev.next = node.next

