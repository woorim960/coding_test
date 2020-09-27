# https://www.acmicpc.net/problem/2798

from itertools import combinations as comb
N, M = map(int, input().split())
cards = list(map(int, input().split()))
# 3개로 조합한 것들의 각각 합들을 구한 후 M 이하인 것들만 추리고, 그 중 MAX 값을 반환
print( max(filter(lambda x: x <= M, map(sum, comb(cards, 3)))) )