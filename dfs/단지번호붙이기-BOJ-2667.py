# https://www.acmicpc.net/problem/2667

# N = 7
# nodes = [
#     [0,1,1,0,1,0,0],
#     [0,1,1,0,1,0,1],
#     [1,1,1,0,1,0,1],
#     [0,0,0,0,1,1,1],
#     [0,1,0,0,0,0,0],
#     [0,1,1,1,1,1,0],
#     [0,1,1,1,0,0,0]
# ]

# 지도의 크기 => 정사각형임
N = int(input())
# 집 데이터(노드) 입력
nodes = []
for _ in range(N) :
    nodes.append(list(map(int, list(input()))))

# 단지마다의 집 개수를 반환해줄 함수
def get_house_cnt(x, y) :
    global house_cnt                # mutable형 전역 변수의 값을 함수 내에서 변경하기 위한 global 선언

    # 지도를 벗어나면 무시
    if x <= -1 or x >= N or y <= -1 or y >= N :
        return False
    
    # 현재 위치가 1이면 0으로 바꾼 뒤 집 카운팅
    if nodes[x][y] == 1 :
        nodes[x][y] = 0             # 0으로 바꾼다.
        house_cnt += 1              # 집 카운팅
        
        # 깊이 우선 탐색 적용
        get_house_cnt(x-1, y)       
        get_house_cnt(x+1, y)
        get_house_cnt(x, y-1)
        get_house_cnt(x, y+1)

        # 1 근처의 노드의 탐색을 마치면 집 카운팅 값 반환
        return house_cnt
    
    # 1이 아니면 무시
    return False

# 변수 선언
house_cnt, group_cnt = 0, 0                     # 집, 단지 카운팅 변수
house_cnts = []                                 # 집 카운팅 값이 저장될 리스트

# 모든 지도 탐색
for i in range(N) :
    for j in range(N) :
        house_cnt = get_house_cnt(i, j)         # x, y 위치가 1이면 해당 단지의 집 개수 반환
        if house_cnt :                          # 현재 위지가 단지였다면 실행
            house_cnts.append(house_cnt)        # 집 카운팅 값 저장
            house_cnt = 0                       # 새로운 단지의 집 개수를 다시 카운팅 하기 위해 0으로 초기화
            group_cnt += 1                      # 단지 카운팅

# 단지 개수와 단지별 집 개수를 줄 단위로 출력
for cnt in [group_cnt] + sorted(house_cnts) :
    print(cnt)