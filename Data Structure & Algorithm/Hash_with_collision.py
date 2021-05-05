#    !-------when you have two key with same index then collision happend -------!
#  1st   rules is separate chaining for multiple key share with same hash value like linked list.  worst case = O(n)
#  2nd   linear probing is find to the next slot if exact slot is filled up.


class HashTable:
    def __init__(self):
        self.max = 10
        self.arr = [[] for i in range(self.max)]     #insted of none use [] for collision

    def get_hash(self, key):
        hash= 0
        for char in key:
            hash +=ord(char)
        return hash % self.max


    def __getitem__(self, key):
        h=self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]         #not return anuthing in pthon it default return none



    # def add_key_value(self, key, val):   #add value as key with value
    def __setitem__(self, key, val):
        h= self.get_hash(key)
        found =False
        for idx, element in enumerate(self.arr[h]):
            if len(element)== 2 and element[0] ==key:        #handle if key already exist
                self.arr[h][idx]=(key, val)
                found=True
        if not found:
            self.arr[h].append((key, val))

    def __delitem__(self, key):
        h=self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][index]

# object =HasTable()
# object["march 3"]= 170
# object["march 6"]= 170
# object["march 6"]= 140
# object["march 8"]= 150
# object["march 17"]= 160
t = HashTable()
t["march 6"] = 310
t["march 7"] = 420
t["march 8"] = 67
t["march 17"] = 63457
a=t.arr
print(a)
# b =object.arr
# print(b)
# del object["march 3"]
# d=object.arr
# print(d)
a=t["march 17"]
print(a)