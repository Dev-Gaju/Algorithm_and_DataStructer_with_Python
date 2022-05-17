

for i in range(5):
    if i%2==0:
        for j in range(i+1):
            print("*", end=" ")
    else:
        for j in range(i+1):
            print('1', end=" ")
    print()