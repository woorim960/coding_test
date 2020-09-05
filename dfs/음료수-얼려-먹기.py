# n,m 공백을 기준으로 n행 m열 입력받기
n, m = map(int, input().split())

# 데이터 삽입
ices = []
for _ in range(n) :
  ices.append( list(map(int, input().split())) )

# 문제 풀이
def solution(n, m, ices) :
  # (0, 0) 부터 순회하면서 0을 모두 1로 바꾸고 다 바꿨으면 count 1 증가
  count = 0
  for i in range(n) :
    for j in range(m) :
      # 각 좌표
      if dfs(i, j) == True :
        count += 1
  
  # 결과값 반환
  return count

def dfs(x, y) :
  if x <= -1 or x >= n or y <= -1 or y >= m :
    return False

  if ices[x][y] == 0 :
    ices[x][y] = 1

    dfs(x-1, y)
    dfs(x, y-1)
    dfs(x+1, y)
    dfs(x, y+1)
    return True
  else :
    return False  

print( solution(n, m, ices) )