# https://www.acmicpc.net/problem/11047

# N, money = 10, 4200
# standard = [
#   1,
#   5,
#   10,
#   50,
#   100,
#   500,
#   1000,
#   5000,
#   10000,
#   50000
# ]

N, K = map(int, input().split())
standard = [int(input()) for _ in range(N)]

cnt = 0
for n in standard[::-1] :
  cnt += money // n
  money = money % n

print(cnt)
  