import re
def solution(dartResult):
    result = []
    # 문자 변환에 필요한 딕셔너리
    charConv = {'S':'**1', 'D':'**2', 'T':'**3', '#':'*-1'}
    
    # 1. 입력 문자열(dartResult) 분할
    parser = re.sub('([SDT][*#]?)', '\g<1> ', dartResult).split()
    
    # 2. 분할된 문자열을 문제의 요구사항에 맞춰서 변환
    for parse in parser:
        for word in parse:
            parse = parse.replace(word, charConv.get(word, word))
        if parse[-1] == '*':
            parse += '2'
            if result:
                result[-1] = result[-1][:-1] + '*2+'
        parse += '+'
        result.append(parse)
    
    # 3. 변환된 문자열의 연산값 반환
    return eval(''.join(result)[:-1])
