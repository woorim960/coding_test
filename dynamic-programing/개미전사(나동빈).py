def top_down(i):
  if (i == 0): return arr[0]
  if (i == 1): return max(arr[:2])
  if (d[i] != 0): return d[i]

  d[i] = max(top_down(i - 1), top_down(i - 2) + arr[i])
  return d[i]

def bottom_up(n):
  d = [0] * n

  d[0] = arr[0]
  d[1] = max(arr[0:2])
  for i in range(2, n):
    d[i] = max(d[i - 1], arr[i] + d[i - 2])

  return d[n - 1]


n = int(input())
arr = list(map(int, input().split()))

d = [0] * n
print(top_down(n - 1))
print(bottom_up(n))