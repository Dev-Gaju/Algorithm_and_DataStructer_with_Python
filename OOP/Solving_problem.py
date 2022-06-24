a = []
for i in range(5):
    ele = int(input())
    a.append((ele))
# print(a)

a.sort()
b=0
for i in range(len(a)-1):
     b += a[i]
print(b)
c=0
for i in range(1,len(a)):
     c += a[i]
print(c)
