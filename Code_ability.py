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
string = "aaaa"
new_string = " "
Sequq_sub(string, 0, new_string)
