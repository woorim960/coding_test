relation = [
    ["100","ryan","music","2"],
    ["200","apeach","math","2"],
    ["300","tube","computer","3"],
    ["400","con","computer","4"],
    ["500","muzi","music","3"],
    ["600","apeach","music","2"]
]

def solution(relation):
    tp_len = len(relation)                          # 튜플 길이
    cols = [[] for _ in range(len(relation[0]))]    # 컬럼 공간 만들기

    # 컬럼 분리
    for row in relation :
        for i, col in enumerate(row) :
            cols[i].append(col)
    
    # 유일키 식별
    cnt = 0
    for i, col in enumerate(cols) :
        if is_unique(col) :
            cnt += 1
            cols.pop(i)
    
    multi_cols = []

    return cnt

# 유일키 식별 함수
def is_unique(col) :
    if len(col) == len(set(col)) :
        return True
    return False


print(solution(relation))

