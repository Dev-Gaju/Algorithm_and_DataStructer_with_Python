def count_value_Array(arr, num, i=0):
    if i == len(arr):
        return 0
    elif arr[i] == num:
        return 1 + count_value_Array(arr, num, i+1)
    else:
        return count_value_Array(arr, num, i + 1)


a = count_value_Array([1,2,6,3,4,5,6,7,8,9], 6)
print(a)
