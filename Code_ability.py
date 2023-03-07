class Node():
    def __init__(self, val):
        self.next = None
        self.prev = None
        self.val = val


class Double_Linkedlist():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.size += 1
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def remove(self, val):
        if self.head is None:
            return
        if self.head.val ==val:
            if self.head == self.tail :
                self.head =None
                self.tail = None
            else:
                self.head= self.head.next
                self.head.prev = None
            return
        current = self.head
        while current is not None:
            if current.val == val:
                if current == self.tail :
                    self.tail = current.prev
                    self.tail.next= None
                else:
                    current.prev.next= current.next
                    current.next.prev = current.prev
                return
            current = current.next


    def print_node(self):
        current = self.head
        while current is not None:
            print(current.val, end="<--->")
            current = current.next
        print("None")


L = Double_Linkedlist()
L.add(4)
L.add(2)
L.add(1)
L.add(4)
L.print_node()
L.remove(1)
L.print_node()
