def getCountChangedWhite(board, i, j):
  count = 0
  for a in range(i, i + 8):
    for b in range(j, j + 8):
      point = a + b
      if (point % 2 == 0 and board[a][b] != 'W'):
        count += 1
      elif (point % 2 == 1 and board[a][b] != 'B'):
        count += 1
  return count


def getCountChangedBlack(board, i, j):
  count = 0
  for a in range(i, i + 8):
    for b in range(j, j + 8):
      point = a + b
      if (point % 2 == 0 and board[a][b] != 'B'):
        count += 1
      elif (point % 2 == 1 and board[a][b] != 'W'):
        count += 1
  return count

def solution(N, board):
  x, y = N[0] - 7, N[1] - 7

  result = []
  for i in range(x):
    for j in range(y):
      wCount = getCountChangedWhite(board, i, j)
      bCount = getCountChangedBlack(board, i, j)
      result.append(min(wCount, bCount))

  return min(result)

N = list(map(int, input().split()))
board = [input() for _ in range(N[0])]

print(solution(N, board))