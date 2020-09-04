# 올바른 괄호 문자열 체크 함수
def is_check(p):
    if p == '': return True
    count = 0
    for i in p:
        if i == '(': count += 1
        else: count -= 1
            
        if count < 0:
            return False
    return True

# u, v 분할 함수
def division(p):
    count = 0
    for i, w in enumerate(p):
        if w == '(':  count += 1
        else: count -= 1
            
        if count == 0: break
    return p[:i+1], p[i+1:]

def solution(p):
    # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
    if is_check(p): return p

    # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u,v 로 분리합니다. 단, u는 "균형잡힌 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
    u, v = division(p)

    # 3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
    if is_check(u): 
        u += solution(v) # 3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
        return u

    # 4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
    else:
        s = '(' # 4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
        s += solution(v) # 4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
        s += ')' # 4-3. ')'를 다시 붙입니다. 
        # 4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
        u = u[1:-1]
        for i in u:
            if i == "(": s += ')'
            else: s += '('
        return s
