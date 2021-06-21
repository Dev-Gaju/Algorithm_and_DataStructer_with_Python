def number_checking(arr, value):     #O(n**2)

    for i in  arr:
        for j in range(i+1, len(arr)):
            if arr[i] +arr[j] == value:
                return True
    return False

# print(number_checking([2,3,4,52,23,1,9,6,5], 17))

# another Way to solv this

def two_number_combination(arr, num):     #O(Nlogn)
    arr.sort()
    left = 0
    right = len(arr)-1
    while left < right:
        if arr[left] + arr[right] == num:
            return  True
        elif arr[left] + arr[right] < num:
            left +=1
        else:
            right -= 1

    return False

# print(two_number_combination([2,3,4,52,23,1,9,6,5], 7))

def findPair(arr, k): #0(n)  ---(k-arr[i])==store in hashtable
    visited ={}
    for element in arr:
        if visited.get(k - element):   #get basically return value based on keys
            return True
        else:
            visited[element] = True
    return False

print(findPair([2,3,4,52,23,1,9,6,5], 7))
