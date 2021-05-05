def get_hash(key):
    hash = 0
    for char in key:
        hash += ord(char)
    return hash % 100
a = get_hash('April 16')
print(a)