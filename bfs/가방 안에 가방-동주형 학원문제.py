
# BFS 구현을 위한 deque 포함
from collections import deque

n = 4
actions = [
    'put 3 inside 4',
    'put 2 inside 3',
    'put 1 inside 2',
    'put 2 inside 4',
    'set 2 loose',
    'put 2 inside 1',
    'swap 3 with 4',
    'put 3 inside 3',
    'swqp 4 with 3',
    'put 4 inside 2'
]

# 연결된 노드들끼리 리스트에 담아준다.
graph = [[] for _ in range(n+1)]

# 방문 처리를 위한 방문 여부 변수 선언
is_visitable = [False] * (n+1)

# 잘못된 크기의 가방을 가지고있는 노드가 저장될 리스트
result = []

# 그래프(가방 안에 가방) 만들기 - actions 수행
def make_graph(n, actions):
  # 만들기
  for i in range(len(actions)):
    actions[i] = actions[i].split()
    if actions[i][0] == 'put' :
      graph[ int(actions[i][3]) ].append( int(actions[i][1]) )
    elif actions[i][0] == 'set' :
      graph[ int(actions[i][1]) ] = []
    else :
      graph[ int(actions[i][1]) ], graph[ int(actions[i][3]) ] = graph[ int(actions[i][3]) ], graph[ int(actions[i][1]) ]
  print(f'각 가방이 갖고 있는 가방들 : {graph}')

# BFS 함수
def bfs(graph, start, is_visitable):
  # 시작 노드를 큐로 만들어준다.
  q = deque([start])
  # 시작 노드 방문 처리
  is_visitable[start] = True

  # 큐가 빌 때 까지 반복
  while q:
    # FIFO 처리
    node = q.popleft()
    # out 노드 출력
    print(f'가방 탐색 순서 : {node}')

    # 인접 노드 순회
    for i in graph[node]:
      # 노드가 갖고 있는 원소가 본인보다 크다면 실행
      if node < i:
        result.append(node)

      # 해당 노드에 미방문시 실행
      if is_visitable[i] == False:
        # 큐에 추가
        q.append(i)
        # 방문 처리
        is_visitable[i] = True
  
  # 탐색하지 않은 노드 중 원소가 있는 노드가 있다면 bfs 다시 실행
  for i in range(len(is_visitable)) :
    if is_visitable[i] == False :
      if graph[i] != [] :
        bfs(graph, i, is_visitable)

# 가방 안에 가방 만들기 actions 시작
make_graph(n, actions)

# BFS(너비 우선 탐색) 시작
bfs(graph, 4, is_visitable)

# 잘못 들어간 가방이 없으면 n 반환, 있으면 -1 반환
print()
print(f'결과 반환 : {n if result == [] else -1}')

print(f'자기보다 큰 가방을 가지고 있는 가방 리스트 : {result}')

