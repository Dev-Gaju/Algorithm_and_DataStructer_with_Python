def MergeSort(sequence):
    if len(sequence) <=1:
        return sequence

    middle_length = len(sequence)//2

    left_values = MergeSort(sequence[:middle_length])
    print("left Value is", left_values)
    right_values = MergeSort(sequence[middle_length:])
    print("Right Values is ", right_values)
    # sorted_values =[]

    # left_index  = 0
    # right_index = 0
    # print("length of left value:", len(left_values))
    # print("length of Right value:", len(right_values))

    # while left_index <len(left_values) and right_index < len(right_values):
    #
    #     if left_values[left_index] < right_values[right_index]:
    #         sorted_values.append(left_values[left_index])
    #         left_index +=1
    #     else:
    #         sorted_values.append(right_values[right_index])
    #         right_index +=1
    # sorted_values += left_values[left_index:]
    # sorted_values += right_values[right_index:]
    # return sorted_values


numbers = [2, 7, 9, 77, 22, 6, 45, 67, 11, 2, 44, 62, 7, 21]
sorted_number = MergeSort(numbers)
print(sorted_number)
