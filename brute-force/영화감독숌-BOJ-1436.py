n = int(input())

result = [666]
i = 666
while len(result) < n :
    i += 1
    if '666' in str(i) :
        result.append(i)
print(result[-1])