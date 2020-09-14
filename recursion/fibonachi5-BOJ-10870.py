# https://www.acmicpc.net/problem/10870

# 피보나치 재귀함수
def recursion(n) :
    # 1보다 작으면 자신 반환
    if n <= 1 :
        return n
    # 이미 구한 값이면 그대로 반환
    if container[n] != 0 :
        return container[n]
    # 구하지 않은 값이면 구한 후 저장
    container[n] = recursion(n-1) + recursion(n-2)
    # 저장한 값 반환
    return container[n]

n = int(input())
# 한 번 구한 값은 다시 구하지 않기 위한 저장 리스트
container = [0] * (n+1)

print(recursion(n))