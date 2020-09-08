import string
def solution(str1, str2):
    pattern = string.ascii_uppercase
    str1 = str1.upper()
    str2 = str2.upper()
    str1_ls, str2_ls = {}, {};
    
    # str1의 갯수 카운팅
    for i in range(len(str1)-1):
        # 영어면 카운팅하여 추가 => 특수문자, 숫자, 공백 등 제거
        if(str1[i] in pattern and str1[i+1] in pattern):
            str1_ls[str1[i] + str1[i+1]] = str1_ls.get(str1[i] + str1[i+1], 0) +1
    # str2의 갯수 카운팅
    for i in range(len(str2)-1):
        # 영어면 카운팅하여 추가 => 특수문자, 숫자, 공백 등 제거
        if(str2[i] in pattern and str2[i+1] in pattern):
            str2_ls[str2[i] + str2[i+1]] = str2_ls.get(str2[i] + str2[i+1], 0) +1
    
    sub_result = []
    add_result = []
    # str1 교집합, 합집합에 추가
    for s, count in str1_ls.items():
        # 다른 집합에도 값이 있으면 실행
        if (s in str2_ls):
            # 교집합
            count = min([str2_ls[s], count]) # 더 적은 갯수만큼 추가 하기 위함
            for cnt in range(count): # 추가
                sub_result.append(s)
                
        # 합집합
        for cnt in range(count): # 집합에 존재하는 문자 갯수만큼 추가
            add_result.append(s)

    # 합집합 구하기
    for s, count in str2_ls.items():
        # 중복 값의 갯수만큼 카운팅하기 위함
        if (s in add_result):
            count = max([str1_ls[s], count]) - min([str1_ls[s], count])
            
        for cnt in range(count):
            add_result.append(s)
            
    # 빈 집합일 경우 셋팅
    sub_len = 0 if sub_result == [] else len(sub_result)    
    add_len = 1 if add_result == [] else len(add_result)
    
    # 자카드 유사도 반환
    J = int(sub_len/add_len * 65536) 
    J = 65536 if sub_result == [] and add_result == [] else J
    return J
