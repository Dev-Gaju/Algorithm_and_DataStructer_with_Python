def Binary_search(arr, value, left, right):
    mid = (left + right)//2
    # print(mid)
    if left > right:
        return -1
    elif arr[mid] == value:
        return mid
    elif arr[mid] < value:
        return Binary_search(arr, value, mid+1, right)
    else:
        return Binary_search(arr, value, left, mid-1)

def check_output(arr, num):
    return Binary_search(arr, num, 0, len(arr)-1)

a= [2,3,4,5,7,9,11,13]
print(check_output(a, 4))