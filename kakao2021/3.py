import re
def solution(infos, querys):
    rest = {}
    result = []
    for i in range(len(querys)):
        querys[i] = re.split(' and ', querys[i])
        querys[i] = querys[i][:-1] + querys[i][-1].split()
        q = ''.join(querys[i])
        if q in rest :
            result.append(rest[q])
        else :
            member = 0
            for info in map(lambda i: i.split(), infos):
                cnt = 0
                for j in range(4):
                    if querys[i][j] == '-' or querys[i][j] == info[j]:
                        cnt += 1

                if cnt == 4 and int(querys[i][-1]) <= int(info[-1]):
                    member += 1
            result.append(member)

    return result

print( solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))
