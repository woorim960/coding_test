N = list(map(int, input().split()))
board = [input() for _ in range(N[0])]

# 변환된 흑돌 갯수 카운팅
def getCountChangedWhite(board, i, j):
  # (i, j) 위치에서 8 x 8 크기의 체스판을 검사한다.
  count = 0
  for a in range(i, i + 8):
    for b in range(j, j + 8):
      point = a + b
      if (point % 2 == 0 and board[a][b] != 'W'):
        count += 1
      elif (point % 2 == 1 and board[a][b] != 'B'):
        count += 1
  return count

# 변환된 흑돌 갯수 카운팅
def getCountChangedBlack(board, i, j):
  # (i, j) 위치에서 8 x 8 크기의 체스판을 검사한다.
  count = 0
  for a in range(i, i + 8):
    for b in range(j, j + 8):
      point = a + b
      if (point % 2 == 0 and board[a][b] != 'B'):
        count += 1
      elif (point % 2 == 1 and board[a][b] != 'W'):
        count += 1
  return count

# 메인 솔루션
def solution(N, board):
  x, y = N[0] - 7, N[1] - 7 # 8 x 8 크기의 체스판만 검사하면 되므로, (x, y)는 각 행과 열의 -8 위치에서부터 검사하도록 해야한다. -8이 아닌 -7을 한 이유는 아래 range() 함수에서 -1까지 순회하기 때문.

  result = []
  for i in range(x):
    for j in range(y):
      wCount = getCountChangedWhite(board, i, j)
      bCount = getCountChangedBlack(board, i, j)
      result.append(min(wCount, bCount))

  return min(result)

print(solution(N, board))