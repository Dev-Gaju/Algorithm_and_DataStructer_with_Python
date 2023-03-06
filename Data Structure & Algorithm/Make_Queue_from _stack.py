#make queue from two stack

class Queue():
    def __init__(self):
        self.s1 = []
        self.s2 =[]

    def enqueue(self, item):
        self.s1.append(item)

    def dequeue(self):
        if len(self.s1 )==0 and len(self.s2)==0:
            print("Empty")
            return
        elif len(self.s2)==0 and len(self.s1 ) > 0:
            while len(self.s1):
                temp=self.s1.pop() # remove 1st item to s1
                self.s2.append(temp) #added 1st item froms1 to s2
            return self.s2.pop() #delete first item from s2
        else:
            return self.s2.pop() #also realesed from s2

    def display(self,):
        return self.s1



s = Queue()
s.enqueue(3)
s.enqueue(5)
s.enqueue(9)
print(s.display())
print(s.dequeue())
# q=Queue()
# q.enqueue()
# print(s.display())
