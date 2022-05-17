def greater(a, b):
    if a > b:
        return a
    return b

# print(greater(2, 9))

def greater1(a, b, c):
    return greater(greater(a, b), c)

print(greater1(2, 9, 45))

def greater2(a, b, c, d):
    return greater(greater1(a, b, c), d)


print(greater2(2, 9, 45, 50))
