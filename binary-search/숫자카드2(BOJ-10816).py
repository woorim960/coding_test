N = int(input())
nHaves = sorted(map(int, input().split()))

# n의 개수 카운팅하여 key:value로 만들기 
# -> while로 찾는 것보다 빠름.
# -> 파이썬의 리스트 특성상 n번지에 접근하는 것이 O(n)이 걸리는 반면, 딕셔너리는 O(1)의 시간복잡도를 갖기 때문인것으로 보임.
nCounts = {}
for n in nHaves:
  if n in nCounts:
    nCounts[n] += 1
  else:
    nCounts[n] = 1

M = int(input())
mOrigins = list(map(int, input().split()))

def getTargetIndex(target, start, end):
  mid = (start + end) // 2
  
  if start > end: return -1
  
  if nHaves[mid] == target:
    return mid
  elif nHaves[mid] < target:
    return getTargetIndex(target, mid + 1, end)
  else:
    return getTargetIndex(target, start, mid - 1)

# while로 리스트를 순회하면서 중복값을 찾는다.
# getTargetCount()로 찾을 경우 시간초과 발생.
def getTargetCount(targetIndex):
  if targetIndex == -1: return 0
  cnt = 1

  i = targetIndex + 1
  while i < N and nHaves[i] == nHaves[targetIndex]:
    i += 1
    cnt += 1
  
  i = targetIndex - 1
  while i >= 0 and nHaves[i] == nHaves[targetIndex]:
    i -= 1
    cnt += 1
  
  return cnt

result = []
for m in mOrigins:
  targetIndex = getTargetIndex(m, 0, N - 1)
  # targetCount = getTargetCount(targetIndex)
  if (targetIndex != -1):
    result.append(nCounts.get(nHaves[targetIndex], 0))
  else: 
    result.append(0)
    
for r in result:
  print(r, end=' ')