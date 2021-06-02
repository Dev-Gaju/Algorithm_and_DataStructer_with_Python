def get_Subsequences(str):
    subsequences =[]
    def rec(str, i, subsequence):
        if i == len(str):
            subsequences.append(subsequence)
        else:
            rec(str, i+1, subsequence+str[i])
            rec(str,i+1, subsequence)

    rec(str,0,"")
    return subsequences
a = get_Subsequences("abcd")
print(a)