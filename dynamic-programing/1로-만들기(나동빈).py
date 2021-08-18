import sys
sys.setrecursionlimit(10**9)

def top_down(n):
  if (n <= 1): return 0
  if (n <= 3 or n == 5): return 1
  if (d[n] != 0): return d[n]

  d[n] = top_down(n - 1) + 1
  if (n % 2 == 0): d[n] = min(d[n], top_down(n // 2) + 1)
  if (n % 3 == 0): d[n] = min(d[n], top_down(n // 3) + 1)
  if (n % 5 == 0): d[n] = min(d[n], top_down(n // 5) + 1)

  return d[n]

def bottom_up(n):
  d = [0] * 30001
  d[:8] = [0, 0, 1, 1, 2, 1, 2, 3]

  for i in range(8, n + 1):
    d[i] = d[i - 1] + 1
    if (i % 2 == 0): d[i] = min(d[i], d[i // 2] + 1)
    if (i % 3 == 0): d[i] = min(d[i], d[i // 3] + 1)
    if (i % 5 == 0): d[i] = min(d[i], d[i // 5] + 1)

  return d[n]

n = int(input())

d = [0] * 30001
print(top_down(n))
print(bottom_up(n))
