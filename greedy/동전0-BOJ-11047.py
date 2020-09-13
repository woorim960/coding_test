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

# 동전 개수와 돈 입력받기
N, K = map(int, input().split())
# 동전 입력받기
standard = [int(input()) for _ in range(N)]

cnt = 0                         # 몇개의 동전이 사용되는지 카운팅할 변수
for n in standard[::-1] :       # 동전의 리스트를 거꾸로 순회
  cnt += money // n             # 돈과 동전을 나눠서 몫을 카운팅 변수에 더한다. => 4200원//1000원 = 4 이기 때문
  money = money % n             # 남은 돈으로 동전을 계속 나눠주기 위해 나머지값을 money에 저장

print(cnt)                      # 출력
  