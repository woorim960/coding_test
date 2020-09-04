def solution(N, stages):
    # 실패율 생성
    dic = {}
    allPlayer = len(stages)
    for i in range(1, N+1):
        notClearPlayer = stages.count(i)
        if allPlayer == 0 :
            failRate = 0
        else:
            failRate = notClearPlayer / allPlayer
        dic[i] = failRate
        
        allPlayer -= notClearPlayer
        
    # 실패율을 기준으로 정렬
    dicSort = sorted(dic.items(), key = lambda x : x[0])
    dicSort = sorted(dicSort, key = lambda x : x[1], reverse = True)
    
    # 정렬된 실패율 반환
    result = [dicSort[i][0] for i in range(len(dicSort))]
    return result
