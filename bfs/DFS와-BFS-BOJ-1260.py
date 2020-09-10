# https://www.acmicpc.net/problem/1260

from collections import deque
# N, M, V = 4, 5, 1
# nodes = [
#   [1, 2],
#   [1, 3],
#   [1, 4],
#   [2, 4],
#   [3, 4]
# ]

# 정점(노드) 수, 간선(연결된 노드) 수, 탐색 시작 정점(노드) 입력 받기
N, M, V = map(int, input().split())
# 간선 입력 받기
nodes = []
for n in range(M) :
  nodes.append(list(map(int, input().split())))

# 간선을 토대로 그래프 만들기
graph = [[] for _ in range(N+1)]
for node in nodes :
  graph[node[0]].append(node[1])
  graph[node[1]].append(node[0])
# 작은 것부터 탐색해야하기 때문에 그래프 정렬
graph = list(map(sorted, graph))

# dfs와 bfs의 방문 처리를 따로 생성
# dfs의 방문 처리 리스트
is_visitable = [False] * (N+1)
# dfs의 결과값이 저장될 리스트
result = []
# DFS
def dfs(node, is_visitable, result) :
  # 방문 처리
  is_visitable[node] = True
  # 방문한 노드 저장
  result.append(node)

  # 깊이 우선 탐색
  for n in graph[node] :
    # 방문하지 않은 노드는 방문 처리
    if not is_visitable[n] :
      dfs(n, is_visitable, result)
  # 방문한 노드 리스트 반환
  return result

# BFS
def bfs(start) :
  # 방문 처리 리스트
  is_visitable = [False] * (N+1)

  # 큐 생성
  q = deque()
  q.append(start)               # 시작 노드 저장
  is_visitable[start] = True    # 시작 노드 방문 처리

  result = []                   # 방문한 노드가 저장될 리스트
  # 너비 우선 탐색
  while q :                     # 큐가 빌 때 까지
    node = q.popleft()          # 가장 아래쪽 노드 pop
    result.append(node)         # 방문한 노드는 저장
    for n in graph[node] :      # 너비 우선 탐색 => 방문 노드의 연결 노드를 순차 탐색
      if not is_visitable[n] :  # 방문하지 않은 노드일 경우
        is_visitable[n] = True  # 방문 처리
        q.append(n)             # 큐에 저장 => 너비 우선 탐색을 위함

  # 방문한 노드 리스트 반환
  return result

# DFS 출력
for node in dfs(V, is_visitable, result) :
  print(node, end=' ')
print()

# BFS 출력
for node in bfs(V) :
  print(node, end=' ')
print()