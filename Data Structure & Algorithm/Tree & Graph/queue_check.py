class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def deque(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def display(self):          # deque is a method like queue which dont follow FIFO or LIFO
        return self.items


# q = Queue()                       # create an object
#
# q.isEmpty()
#
# q.enqueue(34)
# q.enqueue(23)
# q.enqueue(12)
# q.enqueue(84)
# print(q.display())
#
# print(q.deque())
# print(q.display())
