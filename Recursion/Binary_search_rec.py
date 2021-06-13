def Binary_search(arr, num, left, right):
    mid =(left+right)//2
    if left >right:
        return -1     #target value not found
    elif arr[mid] ==num:
        return mid
    elif arr[mid] < num:
        return Binary_search(arr,num, mid+1, right)
    else:
        return Binary_search(arr, num, left, mid-1)

def Binary_search_check(arr, num):
        return Binary_search(arr,num,0, len(arr)-1)

Number = [1,2,3,4,5,6,7,8,9]
print(Binary_search_check(Number, 5))