def solution(n, arr1, arr2):
    arr = list(map(lambda a : a[0] | a[1], zip(arr1, arr2)))
    arr = list(map(lambda a : '0'*(n-len(bin(a)[2:])) + bin(a)[2:], arr))
    result = []
    for a in arr :
        a = a.replace('1', '#')
        a = a.replace('0', ' ')
        result.append(a)
    return result
