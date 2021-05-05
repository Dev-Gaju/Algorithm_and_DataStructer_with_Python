def quick_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop() 
    
    item_greater = []
    item_lower = []
    
    for item in sequence:
        if item > pivot:
            item_greater.append(item)
        else:
            item_lower.append(item)
            
    return quick_sort(item_lower) + [pivot] + quick_sort(item_greater)
            

print(quick_sort([3,6,5,2,9,4]))