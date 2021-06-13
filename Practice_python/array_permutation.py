def get_permutations(arr):
    if len(arr) <2:
        return [arr]
    else:
        permutation = []
        for i in range (len(arr)):  #NOT CALLED ANY DUBLICATE ARRAY
            if arr[i] not in arr[:i]:
                remaining_element = arr.copy()
                remaining_element.pop(i)
                remaining_permutation = get_permutations(remaining_element)
                remove_elem = [arr[i]]
                for permutations in remaining_permutation:
                    permutation.append(remove_elem + permutations)
        return permutation
print(get_permutations([1,2,3]))








