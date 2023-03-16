first = -1
last = -1

def StringOccurence(A, idx, element):
    global first, last

    if idx == len(A):
        print(first),
        print(last)
        return

    current_char = A[0]
    if current_char == element:
        if first == -1:
            first = idx
        else:
            last = idx
    StringOccurence(A, idx + 1, element)


A = "abcdfgaba"
print(len(A))
StringOccurence(A, 0, "a")
