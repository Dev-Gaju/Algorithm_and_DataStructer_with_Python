
                # !-------For List------!

# dic = {Sabbir: 200, Anik : 500, Islam :900, Motableb : 800, Hossain : 400}
                 # Using Ascii Number we here to implement hash table

# def get_hash(key):
#     h =0
#     for char in key:
#         h +=ord(char)          #ord help to find the ascii code value
#     return h % 100        #100 is total list item

# ord('a')
# b=ord('march 17')
# print(b)
# b=get_hash('April 6')
# print(b)

class HasTable :       # implement hash table
    def __init__(self):
        self.max = 10
        self.arr = [None for i in range (self.max)]
    def get_hash(self, key):
        hash= 0
        for char in key:
            hash +=ord(char)
        return hash % self.max

    # def add_key_value(self, key, val):   #add value as key with value
    def __setitem__(self, key, val):
        h= self.get_hash(key)
        self.arr[h]=val

    # def get_value(self, key):   #get value from key
    def __getitem__(self, key):
        h=self.get_hash(key)
        return self.arr[h]

    def __delitem__(self, key):
        h=self.get_hash(key)
        self.arr[h]=None


object = HasTable()
# object.add_key_value("march 6", 130)
# a=object.get_value("march 6")       #its work
# print(a)

# Instead of upper function now we can easily add and remove by builting function
object["march 6"]= 130
object["march 7"]= 140
object["march 8"]= 150
object["march 17"]= 160
object["march 3"]= 170

# a= object.arr  #see all values
# print(a)
del (object["march 3"])
# print(a)


a=object["march 6"]  # see value with index
print(a)




