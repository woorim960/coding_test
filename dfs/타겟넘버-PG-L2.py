# 프로그래머스 Level 2
# https://programmers.co.kr/learn/courses/30/lessons/43165

# 카운팅 변수
cnt = 0

# 메인 함수
def solution(numbers, target):
    # 재귀 때마다 len()을 호출하면 효율성이 안좋으므로 미리 구한 후 매개변수로 넘겨준다.
    len_numbers = len(numbers)
    # 깊이 우선 탐색 실행
    dfs(0, 0, len_numbers, target, numbers)

    # 타겟 숫자를 만들 수 있는 개수 반환
    return cnt

# DFS : 깊이 우선 탐색
def dfs(idx, total, len_numbers, target, numbers) :
    '''
        @ idx : numbers에 어느 인덱스까지 값을 더할 것인지 정한다.
        @ total : 현 idx까지 더해진 값
        @ len_numbers : numbers 길이
        @ target : 만들어야하는 숫자
        @ numbers : target을 만들기 위해 사용해야될 숫자들
    '''

    global cnt                  # imputable형 전역 변수의 값을 변경하기 위해 global 선언
    
    if idx == len_numbers :     # numbers의 숫자를 전부 더했다면 실행
        if total == target :    # 더한 총합이 target과 일치한다면
            cnt += 1            # 카운팅
    else :
        '''
            깊이 우선 탐색이라는 점을 기억하자.

            1. 0번 인덱스부터 1씩 증가시키며 numbers의 값을 더한(or 뺀)다.
            2. numbers의 모든 값을 더할 때 까지 재귀 함수는 계속 호출된다.
            3. 모든 값을 다 더했다면 
                위에 "if idx == len_numbers" 에서 걸러질 것이다.
            
            ps. 가장 먼저 연산되는 결과값은 [1+1+1+1+1] 이며,
                [1+1+1+1-1] -> [1+1+1-1+1] -> [1+1+1-1-1] ... [-1-1-1-1+1] -> [-1-1-1-1-1]
                순서로 호출되어 마무리된다.

            ps. 분명 이해가 어려울 것이다.
                초보자는 소스의 진행 방향을 직접 그려보면서 개념을 잡아야할 필요성이 분명히 있다.
        '''
        dfs(idx+1, total+numbers[idx], len_numbers, target, numbers)
        dfs(idx+1, total-numbers[idx], len_numbers, target, numbers)