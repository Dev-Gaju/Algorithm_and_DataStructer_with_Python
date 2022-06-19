d1 = sum([a[x][x] for x in range(n)])
d2 = sum([a[x][n - 1 - x] for x in range(n)])
print(abs(d1 - d2))

N = int(input())
total = 0
for i in range(N):
    row = input().split()
    total += int(row[i]) - int(row[-(i + 1)])
print(abs(total))
