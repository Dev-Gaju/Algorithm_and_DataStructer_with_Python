rows = int(input("Inter the bumber the rows : "))
columns = int(input("Enter the number of columns: "))

matrix = []

for i in range(rows):
    ele = []
    for j in range(columns):
        a = int(input(j))
        ele.append(a)
    matrix.append(ele)

for i in matrix:
    for j in i:
        print(matrix[i] + matrix[j])
        break
