values = []

for i in range(0, 6):
    a = int(input(i))
    values.append(a)

# print(values)


p = 0
n = 0
z = 0
for i in range(len(values)):
    if values[i] == 0:
        z +=1
    if values[i] > 0:
        p += 1
    if values[i] < 0:
        n +=1

print("{0:6f}".format(p/len(values)))
print("{0:6f}".format(n/len(values)))
print("{0:6f}".format(z/len(values)))