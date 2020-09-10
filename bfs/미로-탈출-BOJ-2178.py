# https://www.acmicpc.net/problem/2178

# 큐 구현을 위한 모듈 포함
from collections import deque

''' n행 m열 입력받기 '''
# n, m = map(int, input().split())
n, m = 5, 6

''' 데이터 삽입 '''
# graph = []
# for _ in range(n) :
#   graph.append(list(map(int, input().split())))
graph = [
  [1, 0, 1, 0, 1, 0],
  [1, 1, 1, 1, 1, 1],
  [0, 0, 0, 0, 0, 1],
  [1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1],
]

# 상, 하, 좌, 우 이동 경로
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# DFS 함수
def bfs(x, y) :
  # Queue 선언
  q = deque()
  # 초기 데이터 삽입
  q.append((x, y))

  # Queue가 빌 때까지 실행
  while q :
    # FIFO 구현
    x, y = q.popleft()
    # 상, 하, 좌, 우 순회하면서 가장 빠른 경로 탐색
    for i in range(4) :
      # 이동할 좌표 초기화
      nx = x + dx[i]
      ny = y + dy[i]

      # 좌표를 벗어나면 빠져나감
      if nx <= -1 or nx >= n or ny <= -1 or ny >= m :
        continue
      # 탐색 데이터가 0(막혀 있으면)이면 빠져나감
      if graph[nx][ny] == 0 :
        continue
      # 길이 뚫려있으면(1이면) 카운팅된 숫자를 기존에 1과 대치
      if graph[nx][ny] == 1 :
        graph[nx][ny] = graph[x][y] + 1 # 기존에 1과 대치
        q.append((nx, ny))              # Queue에 탐색 경로 삽입
  
  # 최단 경로의 카운팅된 값 반환
  return graph[n-1][m-1]

# BFS 실행
print(bfs(0, 0))
