
def LengthOfLongestSubstring(s):

    if len(s) ==0:
        return 0
    map ={} #take dictionary
    max_length= start =0  #maxlength is longest sequence

    for i in range (len(s)):
        if s[i] in map and start <= map[s[i]]:    #check character in dictionary or not
            start =map[s[i]]+1   #start point will be 1 instead of 0 ir b instead of a
        else:
            max_length =max(max_length, i-start+1)    #checking max length between those

        map[s[i]]=i
    return (max_length)

s =  ['a','b','c','a','b','c','b','b']
print(LengthOfLongestSubstring(s))




