grades = []

for i in range(5):
    a = int(input(i))
    grades.append(a)
# print(grades)

for n in grades:
    if n >= 38:
        if n % 5 == 3:
            n += 2
        elif n % 5 == 4:
            n += 1
    else:
        pass
    print(n)


# second solution
def Grade_check(a):
    r = []
    for grade in grades:
        diff = 5 - grade % 5
        if grade >= 38 and diff < 3:
            grade += diff
        r.append(grade)
    return r
