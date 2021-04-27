def Binary_search(list, target):
    first =0
    last =len(list)-1
    while first <= last:
        midpoint = (first+last)//2
        if list[midpoint]==target:
            return midpoint   #best case
        elif list[midpoint]<target:
            first = midpoint+1
        else:
            last = midpoint-1
    return None
def Verify(index):
    if index is not None:
        print("Index value is :", index)
    else:
        print("Target doesn't Exist")
Number = [1,2,3,4,5,6,7,8,9]
result = Binary_search(Number, 7)
Verify(result)