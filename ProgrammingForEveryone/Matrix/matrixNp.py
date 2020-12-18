import numpy as np

R = int(input("enter the number of row: "))
C = int(input("enter the number of column: "))

print("Enter the entity in a single line: ")

entries = list(map(int, input().split()))
matrix =np.array(entries).reshape(R, C)
print(matrix)

