def outOfBoard(board, i, j):
  n = len(board)
  m = len(board[0])
  return i < 0 or i >= n or j < 0 or j >= m

def searchWord(board, word, i, j, counter, visited):
  if counter == len(word):
    return True
  elif outOfBoard(board, i, j) or visited[i][j] or board[i][j] != word[counter]:
    return False
  else:
    visited[i][j] = True
    if searchWord(board, word, i+1, j, counter+1, visited) or searchWord(board, word, i, j+1, counter+1, visited) or searchWord(board, word, i-1, j, counter+1, visited) or searchWord(board, word, i, j-1, counter+1, visited):
      return True
    else:
      visited[i][j] = False
      return False

def exist(board, word):
  n = len(board)
  m = len(board[0])
  visited = [[False] * m for i in range(n)]
  for i in range(n):
    for j in range(m):
      if board[i][j] == word[0]:
        if searchWord(board, word, i, j, 0, visited):
          return True
  return False

n = [ ["K", "I", "N","T"],
      ["B", "I","N","S"],
      ["G","N","Y","I"],
      ["U","O","E","D"]]
print(exist(n, 'INSIDE'))