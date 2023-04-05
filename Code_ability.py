class Node:
    def __init__(self, val):
        self.next = None
        self.val = val


class Linked_List:
    def __init__(self):
        self.head = None
        self.size = 0

    def Add_val(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node

    def remove(self, val):
        if self.head is None:
            return
        if self.head.val == val:
            self.head = self.head.next
        curr = self.head
        while curr.next is not None:
            if curr.next.val == val:
                curr.next = curr.next.next
                return
            curr = curr.next

    def del_with_pos(self, pos):
        if self.head is None:
            return
        if pos == 0:
            self.head = self.head.next

        current = self.head
        previous = None
        count = 0
        while current is not None and count != pos:
            previous = current
            current = current.next
            count += 1
            if current is None:
                print("Value not exist")
                return
        previous.next = current.next

    def print_node(self):
        current = self.head
        while current is not None:
            print(current.val, end="--->")
            current = current.next


LL = Linked_List()
LL.Add_val(5)
LL.Add_val(2)
LL.Add_val(3)
LL.print_node()
print('\n')
LL.del_with_pos(3)
LL.print_node()
