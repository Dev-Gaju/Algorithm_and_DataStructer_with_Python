"""
rjust() method will right align the string, using a specified character (space is default) as the fill character
Also have ljust.
"""

n = 6
for i in range(1, n + 1):
    print(str('#' * i).rjust(n))

#second one example
n=6
for i in range(n):
    print(' ' *(n-i) + "#"*i)


# 3rd one solution
n = int(input())
for m in range(n):
    print((n - m - 1) * ' ' + (m + 1) * '#')