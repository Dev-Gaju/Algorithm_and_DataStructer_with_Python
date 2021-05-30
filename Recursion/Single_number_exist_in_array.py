def countOccarance(arr, num, i=0):
    if i == len(arr):
        return 0
    elif arr[i] == num:
        return 2 + countOccarance(arr, num, i + 1)
    else:
        return countOccarance(arr, num, i + 1)


a = countOccarance([2, 5, 3, 2, 40, 45, 3, 4, 552], 2)
print(a)
