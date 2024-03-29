# we only move right and bottom
#find the minimum cost from left top to right bottom

#brute force solution is obvious just check all value and take the less value

# def minimumCostPath(matrix, i=0, j=0):
#     # print("hello value", matrix[2][0])
#     n=len(matrix)  #row
#     # print(n)
#     m = len(matrix[0])  #rcolumn
#     # print(m)
#     # break
#     if i==n-1 and j== m-1:  #in last value
#         print("First tine", matrix[i][j])
#         return matrix[i][j]
#     elif i==n-1:    #in last row minimum cost of right
#         print("n-1", matrix[i][j])
#         return matrix[i][j] + minimumCostPath(matrix, i, j+1)
#     elif j== m-1:  #in last column
#         print("m-1", matrix[i][j])
#         return  matrix[i][j] + minimumCostPath(matrix, i+1, j )
#     else:
#         return matrix[i][j] + min (minimumCostPath(matrix, i+1, j), minimumCostPath(matrix, i, j+1))
#
# cost= [ [1, 2, 3],
#         [4, 5, 6],
#         [7, 8, 9] ]
# a = minimumCostPath(cost)
# print(a)


# By using dynamoc programming:
def minimumCostPath(matrix):
  n = len(matrix)
  m = len(matrix[0])
  costs = [[0] * m for i in range(n)]
  costs[0][0] = matrix[0][0]
  for i in range(1, m):
    costs[0][i] = costs[0][i-1] + matrix[0][i]
  for i in range(1, n):
    costs[i][0] = costs[i-1][0] + matrix[i][0]
  for i in range(1, n):
    for j in range(1, m):
      costs[i][j] = min(costs[i-1][j], costs[i][j-1]) + matrix[i][j]
  return costs[n-1][m-1]



cost= [ [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9] ]
a = minimumCostPath(cost)
print(a)
