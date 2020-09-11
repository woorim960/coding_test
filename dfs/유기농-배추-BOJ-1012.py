# https://www.acmicpc.net/problem/1012

import sys
sys.setrecursionlimit(10**8) # 재귀함수 호출 범위를 10^8 까지 늘린다.

# DFS : 깊이 우선 탐색
def dfs(x, y) :
    # 배추밭 범위를 벗어나면 무시
    if x <= -1 or x >= N or y <= -1 or y >= M :
        return False
    
    # 현재 위치에 배추가 있으면 실행
    if graph[x][y] == 1 :
        graph[x][y] = 0         # 현재 위치의 탐색을 완료했으므로 0으로 바꾼다.

        # 깊이 우선 탐색
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)

        # 배추 주변에 있는 배추(1)들을 모두 탐색한 후(0으로 바꾼 후) True 반환
        return True

    # 현재 위치에 배추가 없으면 False 반환
    return False

# 테스트케이스 횟수 입력 받기
T = int(input())
# 테스트별 결과값이 저장될 리스트 선언
result = []

# 테스트케이스 횟수만큼 순회
for _ in range(T) :
    M, N, K = map(int, input().split())     # 배추밭의 가로, 세로와 배추 개수 입력 받기
    graph = [[0] * M for _ in range(N)]     # 배추밭 만들기

    # 배추 개수만큼 입력 받기
    for _ in range(K) :
        y, x = map(int, input().split())    # 배추 좌표
        graph[x][y] = 1                     # 배추 위치를 1로 표시

    count = 0                               # 카운팅 변수

    # 배추흰지렁이가 필요한 지역 카운팅
    for i in range(N) :
        for j in range(M) :
            if dfs(i, j) :                  # 현재 위치가 배추 밀집 지역이면 실행
                count += 1                  # 배추흰지렁이 카운팅
    result.append(count)                    # 테스트케이스별 배추흰지렁이 개수 저장

# 결과를 줄 단위로 출력
for r in result :
    print(r)