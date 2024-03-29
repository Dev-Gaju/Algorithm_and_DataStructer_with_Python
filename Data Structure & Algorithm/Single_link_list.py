class Node():
    def __init__(self, val):
        self.next = None
        self.val = val


# [][]--->[][]---> [][]-->[][] value & text value location


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
                temp = temp.next
            temp.next = new_node

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

    def position_remove(self, pos):
        if self.head is None:
            return
        if pos == 0:
            self.head = self.head.next
        current = self.head
        previous = None
        count = 0
        while current is not None and count != pos:   # find the current position of the linklist
            previous = current
            current = current.next
            count += 1
        if current is None:
            return
        previous.next = current.next   # remove current value from linklist anf update the position by adding before
        # and previous list together

    def find_mid(self):  # best way
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow.val

    def findMidPoint(self):
        count = 0
        middle = self.head
        while self.head is not None:
            count += 1
            self.head = self.head.next
        i = 0
        while i < count // 2:
            middle = middle.next
            i += 1
        return middle.val

    def print_node(self):
        current = self.head
        while current is not None:
            print(current.val, end="->")
            current = current.next
        print("None")


llist = SingleLinkList()
llist.add(7)
llist.add(4)
llist.add(3)
llist.add(1)
llist.add(9)
llist.remove(3)
llist.position_remove(2)
llist.print_node()

print(llist.find_mid())

print(llist.findMidPoint())
