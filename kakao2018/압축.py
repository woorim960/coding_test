import string

def solution(msg):
    # 알파벳을 키로하여 인덱스를 값으로 부여
    alpha = {a : i+1 for i, a in enumerate(string.ascii_uppercase)}
    cnt = 26
    result = []

    # msg가 빌 때까지 실행
    while msg :
        # 가장 긴 문자열을 찾는 과정
        i = 1
        while msg[:i] in alpha and i <= len(msg):
            i += 1
        
        # 가장 긴 문자열의 인덱스를 사전에서 찾아서 저장
        result.append(alpha[msg[:i-1]])
        # 새로운 문자열과 인덱스를 저장
        cnt += 1
        alpha[msg[:i]] = cnt     
        # result 리스트에 저장된 문자를 제거   
        msg = msg[i-1:]
    return result