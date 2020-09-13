# https://www.acmicpc.net/problem/11399


# n = 5
# ls = [3, 1, 4, 3, 2]

n = int(input())
ls = sorted(map(int, input().split()))

total = [sum(ls[:i+1]) for i in range(n)]   # 정렬된 줄의 순서대로 자기 차례까지의 값들을 합산하여 리스트에 저장
print(sum(total))   # 모든 값들을 더한 후 출력