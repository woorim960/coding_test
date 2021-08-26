def solution(target):
  start = 1
  end = max(trees)
  
  while start <= end:
    mid = (start + end) // 2
    
    totalTrees = 0
    for tree in trees:
      if tree > mid:
        totalTrees += tree - mid

    if totalTrees < target:
      end = mid - 1
    else:
      start = mid + 1

  return end

N, M = map(int, input().split())
trees = list(map(int, input().split()))

print(solution(M))