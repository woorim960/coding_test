def bottom_up(target):
  d = [10001] * (target + 1)
  d[0] = 0

  for money in moneys:
    for i in range(money, target + 1):
      d[i] = min(d[i], d[i - money] + 1)
  
  return d[target] if d[target] != 10001 else -1

N, M = map(int, input().split())
moneys = []
for _ in range(N):
  moneys.append(int(input()))

print(bottom_up(M))