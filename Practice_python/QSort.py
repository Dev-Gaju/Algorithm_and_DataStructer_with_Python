def Qsort(sequence):

    length= len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()
    small_item =[]
    greater_item = []
    for i in sequence:
        if pivot < i:
            greater_item.append(i)
        else:
            small_item.append(i)

    return Qsort(small_item) + [pivot] + Qsort(greater_item)


print(Qsort([3,6,5,2,9,4]))