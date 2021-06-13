def recursive_binary_search(list, target):
    if len(list)==0:
        return False
    else:
        len(list)//2

        midpoint = len(list)//2
        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint+1:],target)
            else:
                return recursive_binary_search(list[:midpoint], target)
        
def verify(index):
    if index is not None:
        print("Index target is:", index)
    else:
        print("Target doesn't exist")
        
Number =[1,2,3,4,5,6,7,8,9]

result=recursive_binary_search(Number, 3)
verify(result)


"""
recursion take logarithm space and iterative take constant space
 
"""