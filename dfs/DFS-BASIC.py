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

# DFS 함수
def dfs(graph, node, is_visitable) :
  # 방문 처리
  is_visitable[node] = True
  # 방문한 노드 출력
  print(node, end=' ')

  # 인접 노드 중 방문하지 않은 노드 방문
  for i in graph[node] :
    # 방문하지 않았다면 실행
    if is_visitable[i] == False :
      # 노드 방문 처리 및 출력
      dfs(graph, i, is_visitable)

# DFS 실행
dfs(graph, 1, is_visitable)