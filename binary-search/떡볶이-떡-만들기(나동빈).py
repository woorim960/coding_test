def getSlicedCake(cake, point):
  result = cake - point
  return 0 if result <= 0 else result

def binary_search(cakes, target, low, high, pre):
  point = (low + high) // 2
  
  total = 0
  for cake in cakes:
    total += getSlicedCake(cake, point)

  if (total == target): return point
  elif (total > target): return binary_search(cakes, target, point + 1, high, total)
  else:
    if (pre > target): return pre
    return binary_search(cakes, target, low, point - 1, total)


N, M = map(int, input().split())
cakes = list(map(int, input().split()))

print(binary_search(cakes, M, 0, max(cakes), 0))