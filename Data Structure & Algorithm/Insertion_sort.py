def Insertion_sort(sequences):
    indexing_list = range(1, len(sequences))  #1 becoz first item already sorted
    
    for i in indexing_list:
        value_to_sort = sequences[i]   
        
        #i-1 means immediate steps
        while sequences[i-1] > value_to_sort and i>0:   #Greather than previous item then swap tp next item
            sequences[i], sequences[i-1] =sequences[i-1], sequences[i]  #swap the position
            i= i-1   #check each previous steps
            
    return sequences
print(Insertion_sort([12,14,32,3,5,9,3,2,12,4,5,9,4,7,9,5,4,2]))
            