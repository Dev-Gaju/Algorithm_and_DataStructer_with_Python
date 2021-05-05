class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):                  # check stack empty or not
        return self.items == []

    def push(self, item):                # add item by calling push
        self.items.append(item)

    def pop(self):                        # delete last item as LIFO
        return self.items.pop()

    def peek(self):                         # see the last item which remove by pop
        return self.items[len(self.items) - 1]

    def display(self):                       #display all item
        return self.items

    def size(self):
        return len(self.items)


# s = Stack()
# print(s.isEmpty())
# s.push('Fox')
# s.push('Jackel')
# s.push('Dog')
# s.push('Puppy')
# print(s.peek())
# print(s.display())
# print(s.size())
# print(s.pop())
# print(s.display())
# print(s.pop())
# print(s.display())
# print(s.size())