
# 팩토리얼
def factorial(n) :
    # 1 이하면 1 반환, 아니면 n*(n-1)
    return 1 if n <= 1 else n * factorial(n-1)

n = int(input())
print(factorial(n))