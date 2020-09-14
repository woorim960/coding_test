# https://www.acmicpc.net/problem/1931

# stdin을 사용하기 위한 모듈 => 입력 값이 많기에 발생하는 시간초과 방지
import sys

# 입력받기
N = int(input())
times = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 끝나는 시간으로 정렬한 후 시작하는 시간으로 재정렬
times = sorted(times, key=lambda t: (t[1], t[0]))

cnt = 0             # 카운팅
end_time = 0        # 끝난 회의 시간이 저장될 변수
# 사용가능한 회의 시간 카운팅
for time in times :
    if end_time <= time[0] :
        end_time = time[1]
        cnt += 1
print(cnt)