def LS(list, target):

    for i in range( 0 , len(list)):

        if list[i]==target:
            return i
    return  None

def Verify_index(index):
    if index is not None:
        print("Index is ", index)
    else:
        print("index not exist")

Number = [ 32,4,2,23,4,5,53,443,54553,443,433,55,3,33]
result=LS(Number, 433)
Verify_index(result)