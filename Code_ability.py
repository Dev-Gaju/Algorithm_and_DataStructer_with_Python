def Reverse_string(A, idx):
    if idx == 0:
        print(A[0])
        return
    print(A[idx], end=" ")
    Reverse_string(A, idx - 1)


A = "ABCD"
Reverse_string(A, len(A) - 1)
