# https://www.acmicpc.net/problem/11399


# n = 5
# ls = [3, 1, 4, 3, 2]

n = int(input())
ls = sorted(map(int, input().split()))

total = [sum(ls[:i+1]) for i in range(n)]
# 정렬된 줄의 순서대로 자기 차례의 합산된 값을 total에 더해준다.
# for i in range(n) :
#   total += sum(ls[:i+1])  

print(sum(total))