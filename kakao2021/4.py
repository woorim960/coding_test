from collections import deque
import sys
sys.setrecursionlimit(10**8) 

path_a = []
path_b = []

def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n+1)]
    money = [{} for _ in range(n+1)]
    for f in fares :
      graph[f[0]].append(f[1])
      graph[f[1]].append(f[0])
      money[f[0]][f[1]] =  f[2]
      money[f[1]][f[0]] =  f[2]

    visit_a = [False] * (n+1)
    visit_b = [False] * (n+1)


    return dfs_a(graph, visit_a, s, a, b)
    
# DFS
path = []
def dfs_a(graph, visit_a, s, a, b) :
  # 깊이 우선 탐색
  for n in graph[s] :
    if not visit_a[n] :
      dfs_a(graph, visit_a, n, a, b)
  # 방문한 노드 리스트 반환
  if s == b :
    return False
  elif s == a :
    path.append(s)
    return path

  # 방문한 노드 저장
  visit_a[s] = True
  path.append(s)

  
  return path_a



print( solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))    
print( solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]) )
print( solution(6, 4, 5, 6, [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]) )