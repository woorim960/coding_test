N = int(input())

# 최소값 범위 설정
m = N - (9*len(str(N)))
m = 1 if m < 1 else m

result = [n for n in range(m, N) if sum(map(int, str(n)))+n == N]
print(result[0] if result != [] else 0)