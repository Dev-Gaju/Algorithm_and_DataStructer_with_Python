
def hasAdjacent(str, i=1):
    if i>=len(str):
        return False
    elif str[i] ==str[i-1]:
        return True
    else:
        return hasAdjacent(str, i+1)

a=hasAdjacent("programming")
print(a)

#iterative one

def check_Adjacence(str):
    for i in range (len(str)):
        if str[i] == str[i-1]:
            return True

    return False
b = check_Adjacence("Ahmeed")
print(b)