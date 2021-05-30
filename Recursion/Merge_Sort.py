def Merger_sort_ARR(left, right):
    return Merger_sort(left) + Merger_sort(right)



def Merger_sort(arr):
    if len(arr) <=1:
        return arr
    else:
        mid =len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        left =Merger_sort(left)
        right =Merger_sort(right)
        return Merger_sort_ARR(left,right)

numbers = [2, 7, 9, 77, 22, 6, 45, 67, 11, 2, 44, 62, 7, 21]
print(Merger_sort(numbers))