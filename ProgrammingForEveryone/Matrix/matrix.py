R = int(input("enter the number of row: "))
C = int(input("enter the number of column: "))

matrix = []
print("enter the entities row wise: ")

for i in range(R):
    col=[]
    for j in range(C):
        col.append(int(input()))
    matrix.append(col)

for i in range(R):
    for j in range(C):
        print(matrix[i][j], end=" ")
    print()
