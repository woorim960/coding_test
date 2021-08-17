def top_down(n):
  if (n <= 1): return 1
  if (d[n] != 0): return d[n]
  d[n] = top_down(n - 1) + top_down(n - 2)
  return d[n]

def bottom_up(n):
  d = [0] * 101

  d[0], d[1] = 1, 1

  for i in range(2, n + 1):
    d[i] = d[i - 1] + d[i - 2]
  
  return d[n]

n = int(input())
d = [0] * 101 # 피보나치 수 n을 100까지만 구할 수 있음.
print(top_down(n))
print(bottom_up(n))