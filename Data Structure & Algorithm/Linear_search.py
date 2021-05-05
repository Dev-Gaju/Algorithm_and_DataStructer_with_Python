def Linear_search(value, target):
    
    for i in range(0, len(value)):
        if value[i]==target:
            return i
    return None

def verify(index):
    if index is not None:
        print("Index number is ", index)
    else:
        print("Target not Exist")

Number = [2,3,5,6,22,33,45,67,11,2,44,62,7,21]

result = Linear_search(Number, 49)
verify(result)
