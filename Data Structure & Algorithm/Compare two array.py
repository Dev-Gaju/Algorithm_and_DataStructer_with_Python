
# n = int(input("enter the number of element : "))

a =[]
b =[]

for  ele in range(0, 3):
    val = int(input())
    a.append(val)
print("Those Number is", a)

for j in range(0,3):
    c = int(input())
    b.append(c)
print("Those Number is", b)

def BiggerValue(a,b):
    alice = 0
    bob = 0
    for i in range(len(a)):
        for i in range(len(b)):
            if a[i] > b[i]:
                alice +=1
            if a[i] < b[i]:
                bob +=1
            if a[i]==b[i]:
                pass
        return (alice,bob)
    print(alice, bob)


print(BiggerValue(a,b))