# 모듈 포함
import re
import itertools

# 문제 풀이 함수
def solution(expression) :
    # 모든 연산자의 우선순위를 탐색하기 위해 연산자들의 순열 구하기
    operators = list(itertools.permutations(['-', '+', '*'], 3)
    # 숫자와 연산자를 구분하여 리스트 만들기
    expression = re.split('([-+*]{1})', expression)
    
    # 연산자 우선순위에 따른 최대값 구하기
    result = []
    for operator in operators : # 연산자 우선순위 리스트
        exp = expression[:]     # expression copy
        for op in operator :    # 우선순위대로 연산하기 위함
            while op in exp :                                             # 연산자가 표현식에 있다면 실행
                idx = exp.index(op)                                       # 연산자 인덱싱
                exp[idx-1] = str(eval(exp[idx-1] + op + exp[idx+1]))      # 연산
                del exp[idx:idx+2]                                        # 연산된 값만 남기고 나머지는 Delite
        result.append(abs(int(exp[0])))                                   # 최종 연산 결과를 절대값으로 저장
    return max(result)          # 결과값들 중 최대값 반환
            
