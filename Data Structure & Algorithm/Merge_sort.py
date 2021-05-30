
# import sys
# from load import load_numbers
# print(load_numbers)

# numbers =load_numbers(sys.argv[1])

# print(numbers)

def merge_sort(values):
    if len(values) <=1:
        return values   #list have 0 and 1 values then nothing to sort
    
    middle_index =len(values)//2
    
    #recursion on both side
    left_values =merge_sort(values[:middle_index])
    right_values = merge_sort(values[middle_index:])
    sorted_values = []   #merge both side
    
    #start looping while both value on the list
    left_index = 0  #help to remember the index position
    right_index= 0
    
    while left_index < len(left_values) and right_index <len(right_values):
        if left_values[left_index] <right_values[right_index]:  #insert low value first
            sorted_values.append(left_values[left_index])
            left_index +=1   #add and move to next value
        else:
            sorted_values.append(right_values[right_index])
            right_index += 1
    
    sorted_values += left_values[left_index:]
    sorted_values += right_values[right_index:]    
    
    return sorted_values

numbers = [2,5,3,77,22,6,45,67,11,2,44,62,7,21]
sorted_number = merge_sort(numbers)
print(sorted_number)
 


            
            
    
    
