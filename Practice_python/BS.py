def BS(list, target):
    first  = 0
    last = len(list)-1
    while first <= last:
        midpoint = (first + last )//2
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] <target :
            first = midpoint+1
        else:
            last = midpoint-1
    return None

def verify_indexx(index):
    if index is not None:
        print("Index is ", index)
    else:
        print("index is not found")

Number = [ 2,4,5,8,9,10]
result = BS(Number, 10)
verify_indexx(result)

