def check_duplicate_value(arr):
    a= set(arr)
    return a

# print(check_duplicate_value([2,3,4,2,3,5,33,42,66,32,12]))

def CheckDuplicate(arr):      #O(nlogn)
    if len(arr)==0:
        return
    values = [arr[0]]
    arr.sort()
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            values.append(arr[i])

    return values
# print(CheckDuplicate([2,3,4,2,3,5,33,42,66,32,12]))

def RemoveDuplicate(arr):   #O(n)
    duplicate = {}
    for element in arr:
        duplicate[element] = True
    return list(duplicate.keys())

print(RemoveDuplicate([2,3,4,2,3,5,33,42,66,32,12]))
