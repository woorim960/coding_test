# BFS 구현을 위한 deque 포함
from collections import deque

# 연결된 노드들끼리 리스트에 담아준다.
graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [6, 8],
  [1, 7]
]

# 방문 처리를 위한 방문 여부 변수 선언
is_visitable = [False] * 9

# BFS 함수
def bfs(graph, start, is_visitable) :
  # 시작 노드를 큐로 만들어준다.
  q = deque([start])
  # 시작 노드 방문 처리
  is_visitable[start] = True

  # 큐가 빌 때 까지 반복
  while q :
    # FIFO 처리
    node = q.popleft()
    # out 노드 출력
    print(node, end=' ')

    # 인접 노드 순회
    for i in graph[node] :
      # 해당 노드에 미방문시 실행
      if is_visitable[i] == False :
        # 큐에 추가
        q.append(i)
        # 방문 처리
        is_visitable[i] = True

# BFS(너비 우선 탐색) 시작
bfs(graph, 1, is_visitable)