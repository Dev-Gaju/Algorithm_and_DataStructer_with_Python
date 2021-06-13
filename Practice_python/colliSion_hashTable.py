class Hashtable:
    def __init__(self):
        self.max = 10
        self.arr = [[] for i in range (self.max)]

    def char_to_integer(self, key):
        val = 0
        for char in key:
            val +=ord(char)
        return  val % self.max

    def __setitem__(self, key, value):
        h = self.char_to_integer(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) ==2 and element[0]== key:
                self.arr[h][idx]=(key, value)
                found = True
        if not found:
            self.arr[h].append((key, value))

    def __getitem__(self, key):
        h = self.char_to_integer(key)
        for element in self.arr[h]:
            if element[0]==key:
                return element[1]

    def __delitem__(self, key):
        h = self.char_to_integer(key)
        for idx, element in enumerate (self.arr[h]):
            if element[0]==key:
                # self.arr[h][idx] = None
                del self.arr[h][idx]

t = Hashtable()
t["march 6"] = 310
t["march 17"] = 63457

# print(t.arr)

del(t["march 6"])

print(t.arr)
