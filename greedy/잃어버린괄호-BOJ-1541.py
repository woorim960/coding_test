# https://www.acmicpc.net/problem/1541

# 정규표현식을 사용하기 위해
import re

# 입력된 연산식을 +와 -를 기준으로 나눈 후 리스트로 만들어준다.
numbers = re.split('([+-])', input())

# 0으로 시작하는 숫자가 있으면 앞자리의 0들을 지워준다. ex) 00707 -> 707
for i, n in enumerate(numbers) :
    if n[0] == '0' :
        numbers[i] = str(int(n))

# +가 있으면 먼저 수행한다.
while '+' in numbers :
    idx = numbers.index('+')
    numbers[idx-1] = str(eval(numbers[idx-1] + '+' + numbers[idx+1]))
    del numbers[idx:idx+2]

# +가 수행되고 남은 연산식을 수행한다.
print( eval(''.join(numbers)) )