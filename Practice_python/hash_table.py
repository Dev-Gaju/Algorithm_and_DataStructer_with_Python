class HashTable:
    def __init__(self):
        self. max =10
        self.arr = [None for  i in range (self.max)]
        # print(self.arr)

    def get_hash_from_integer(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.max

    def __setitem__(self, key, value):
        h = self.get_hash_from_integer(key)
        self.arr[h] = value

    def __getitem__(self, key):
        h = self.get_hash_from_integer(key)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.get_hash_from_integer(key)
        self.arr[h]= None

object = HashTable()

object["march 6"]= 130
object["march 7"]= 140
object["march 8"]= 150
object["march 17"]= 160
object["march 3"]= 170

print(object["march 8"] )
del (object['march 17'])
a=object["march 6"]  #see value with index
print(a)