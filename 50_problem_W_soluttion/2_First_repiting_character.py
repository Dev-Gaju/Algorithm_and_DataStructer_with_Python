def repeating_character(str):   #O(n**2)
    for i in range (len(str)):
        # print(str[i])
        for j in range (i):
            if str[i] != str[j]:
                j +=1
            else:
                return str[i]+str[j]
    return None
# print(repeating_character('heldoe'))

 
def findRepeatingCharacter(str):   #O(n)
    visited ={}
    for ch in str:
        if visited.get(ch):
            return ch
        else:
            visited[ch]= True
    return None
print(findRepeatingCharacter('heldonge'))


