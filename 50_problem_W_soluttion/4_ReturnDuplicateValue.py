def returnDuplicateValue(arr):   #0(nlog)  #just n+1 value for duplicate like PigeonHOle
    if len(arr) < 0:              #n and 1 inclusive
        return
    duplicate_num =[arr[0]]
    arr.sort()
    for i in range (1, len(arr)):
        if arr[i] == arr[i-1]:
            duplicate_num.append(arr[i])
    return duplicate_num

# print(returnDuplicateValue([1,3,2,5,6,7,8,9,1]))

def DupValue(arr):  #O(n) also  Space
    hash_table ={}
    for element  in arr :
        if hash_table.get(element):
            return element
        else:
            hash_table[element] =True
    # return hash_table

# print(DupValue([1,3,2,5,6,7,8,9,1]))

# We can run this algo with 0(1) Space using floyed cycle detection.
# Tortoise and hare algo for reduce space complexity

def findDublicate(arr):
    tortoise = arr[0]
    # print(tortoise)
    hare = arr[arr[0]]
    # print(hare)
    while tortoise != hare:
        tortoise = arr[tortoise]
        hare = arr[arr[hare]]
    tortoise = 0
    while tortoise != hare:
        tortoise = arr[tortoise]
        hare = arr[hare]
    return tortoise

print(findDublicate([2, 6, 3, 4, 5, 2, 3]))



