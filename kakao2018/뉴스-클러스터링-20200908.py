def solution(str1, str2):
    # 문자를 2개씩 묶고 개수 카운팅
    strings = []
    for string in [str1, str2] :
        # 대문자로 바꾼 후 한 글자씩 리스트에 저장
        conv = list(string.upper())
        convs = {} # 카운팅된 문자열 개수가 딕셔너리 형태로 저장
        for i in range(1, len(conv)) :
            # 문자열 두개씩 합치기
            word = conv[i-1] + conv[i]
            # 합친 문자열이 알파벳이 아니면 카운팅하지 않는다.
            if not word.isalpha() :
                continue
            # 문자별로 카운팅
            convs[word] = convs.get(word, 0) + 1
        # 저장
        strings.append(convs)
    
    # 언패킹
    str1, str2 = strings
    
    # 교집합 생성
    interaction = []
    for s1, cnt in str1.items() :
        if s1 in str2 :
            # s1이 str2에 있으면 최소 개수만큼 추가
            interaction += [s1 for _ in range(min(cnt, str2[s1]))]
    
    # 합집합 생성
    union = []
    s1, s2 = list(str1.keys()), list(str2.keys()) # 사용하기 쉽도록 분리
    for s in set(s1+s2) : # 중복 원소 제거 후 순회
        # 모든 원소를 최대 개수만큼 추가
        union += [s for _ in range(max(str1.get(s, 0), str2.get(s, 0)))]
    
    # 교집합, 합집합 길이
    c1, c2 = len(interaction), len(union)
    # 분모가 0이면 1, 아니면 나눠준다.
    J = 1 if c2 == 0 else c1/c2
    # 정수형으로 반환
    return int(J * 65536)
