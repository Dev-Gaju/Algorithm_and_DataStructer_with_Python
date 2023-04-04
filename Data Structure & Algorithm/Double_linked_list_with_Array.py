class Node():
    def __init__(self, val):
        self.next = None
        self.prev = None
        self.val = val


class Double_linklist():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # [][][]<--->[][][]<--->[][][]<-->[][][]   prev_addres_ value_next_address
    def add(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.size += 1
        else:
            new_node.prev = self.tail  # new node previous node is tail   1--2--3, now add 4
            self.tail.next = new_node  # added new node after the tail
            self.tail = new_node  # update tail coz we add new node in tail position

    def remove(self, val):
        if self.head is None:  # if list null
            return
        if self.head.val == val:
            if self.head == self.tail:  # if only node in linked list
                self.head = None  # both will be None
                self.tail = None
            else:  # if more than one None then only head related values will None
                self.head = self.head.next  # update new head
                self.head.prev = None   # after update new head delete the previuos head
            return
        current = self.head
        while current is not None:  # if first case not true then check rest
            if current.val == val:  # again head and val same
                if current == self.tail:  # now related with tail
                    self.tail = current.prev  # update new tail
                    self.tail.next = None  # after update new tail previous tail will be removed
                else:        # if value not same with current then update path
                    current.prev.next = current.next
                    current.next.prev = current.prev
                return
            current = current.next    # update loop

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.val, end="<--->")
            current = current.next
        print("None")


L = Double_linklist()
L.add(3)
L.add(2)
L.add(12)
L.remove(2)
L.print_list()




# #help to print the node
#     def __str__(self):
#         values = []
#         node = self.head
#         while node is not  None:
#             values.append(node.val)
#             node = node.next
#         return f"[{', '.join(str(val) for val in values)}]"
