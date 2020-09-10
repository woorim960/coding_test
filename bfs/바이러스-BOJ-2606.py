# https://www.acmicpc.net/problem/2606

from collections import deque
# com = 7
# linked_cnt = 6
# linked_nodes = [
#   [1, 2],
#   [2, 3],
#   [1, 5],
#   [5, 2],
#   [5, 6],
#   [4, 7]
# ]

# 변수 입력 받기
com = int(input())            # 컴퓨터 수
linked_cnt = int(input())     # 연결된 컴퓨터 수
linked_nodes = []             # 연결된 컴퓨터 쌍 => 두 개씩 리스트로 저장됨
for _ in range(linked_cnt):
  linked_nodes.append(list(map(int, input().split())))

# 그래프 만들기
graph = [[] for _ in range(com+1)] # 빈 그래프 생성
# 연결된 노드들을 그래프로 만든다.
for nodes in linked_nodes:
  graph[nodes[0]].append(nodes[1])
  graph[nodes[1]].append(nodes[0])

# 각 노드를 방문 처리할 리스트
is_visitable = [False] * (com+1)

# BFS(너비 우선 탐색)
def bfs(graph, start):
  # 시작 노드부터 탐색
  q = deque([start])

  # 탐색한 노드들이 순서대로 저장될 리스트
  result = []
  # 큐가 빌 때까지 실행
  while q:
    # 노드 탐색
    node = q.popleft()
    # 탐색한 노드 방문처리
    is_visitable[node] = True
    # 방문처리한 노드를 결과 리스트에 저장
    result.append(node)

    # 탐색한 노드와 연결된 노드를 탐색
    for i in graph[node]:
      # 방문하지 않은 노드만 방문 처리 후 큐에 저장
      if not is_visitable[i]:
        is_visitable[i] = True
        q.append(i)
  
  # 탐색한 노드들 길이 반환 => 1번 노드는 바이러스를 퍼뜨린 주범이기 때문에 감염 대상이 아니다. 따라서 -1을 해주어야함.
  return len(result)-1


print(bfs(graph, 1))
