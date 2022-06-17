
n=6
for i in range(1,n):
    print(' ' *(n-i) + "#"*i)


n = int(input())
for m in range(n):
    print((n - m - 1) * ' ' + (m + 1) * '#')