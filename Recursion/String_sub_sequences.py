# order follow and choice given
"""
Meaning ABC sequence C can not come before A or B and B can not come after C
"""


def SusSequences(A, idx, new_string):
    if idx == len(A):
        print(new_string)
        return

    current_str = A[idx]
    SusSequences(A, idx + 1, new_string + current_str)  # wanna come
    SusSequences(A, idx + 1, new_string)      # not come


A = "abc"
new_string = " "
SusSequences(A, 0, new_string)

# Print the subseq from aaa which have to unique

def Sequq_sub(string, idx, new_string):
    if idx == len(string):
        if new_string in  contain_string:
            return
        else:
            print(new_string)
            contain_string.add(new_string)
            return
    current_char = string[idx]
    Sequq_sub(string, idx + 1, new_string + current_char )
    Sequq_sub(string, idx + 1, new_string )


contain_string = set()
string = "abc"
new_string = " "
Sequq_sub(string, 0, new_string)

