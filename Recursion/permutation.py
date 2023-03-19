# define first value and rest two define from each sit.
"""
suppose three values have, abc, sit a is manually and b, c do by calling
total number permutation of each string will be n! so time complexity will be n!
"""


def stringPerm(string, permutation):
    if len(string) == 0:
        print(permutation)
        return
    for i in range(len(string)):
        current_char = string[i]
        new_string = string[0:i] + string[i + 1:]
        stringPerm(new_string, permutation + current_char)


strval = "abc"
permut = " "
stringPerm(strval, " ")
