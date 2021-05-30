def ISort(sequence):
    index_Calculation = range(1, len(sequence))

    for i in index_Calculation:
        to_be_sort =  sequence[i]

        while sequence[i-1] > to_be_sort and i >0:
            sequence[i], sequence[i-1] = sequence[i-1], sequence[i]
            i =i -1
    return sequence


print(ISort([12,14,32,3,5,9,3,2,12,4,5,9,4,7,9,5,4,2]))