# x, y 초기값 0으로 정의
x = y = 0

# x, y가 2보다 작으면 다시 입력받는다.
while x < 2 or y < 2 :
  print('4 이상의 두 정수를 띄어쓰기 기준으로 입력하시오.')
  x, y = map(int, input().split())   # 띄어쓰기를 기준으로 x, y를 입력받는다.

x, y = min(x, y), max(x, y)   # x, y 중 작은 값은 x에, 큰 값은 y에 대입

# 일반적인 해결법
def general_solution(x, y) :
  prime_nums = set()    # 소수가 저장될 set() 타입의 배열 => set() 타입은 중복을 제거해주는 특성을 가짐(집합형이라고도 부름)

  # x~y까지 순회하면서 각 숫자가 소수인지 검사
  for i in range(x, y+1) :
    cnt = 0   # 소수인지 판별해줄 카운팅 변수

    # 2부터 i(검사될 현재 숫자)까지 증가하면서 숫자 i가 j로 나눠지는지 검사
    for j in range(2, i+1) :
      if i % j == 0 :    # 나눠지면 카운팅 + 1
        cnt += 1
    if cnt <= 1 :        # 소수면 prime_nums에 추가
      prime_nums.add(j)
  return prime_nums      # prime_nums 반환


prime_nums = general_solution(x, y)   # 일반적인 해결법 실행 후 반환된 값은 prime_nums에 저장

# 일반적인 해결법으로 풀은 소수값 출력
print('==== general solution ====')
print(f'{x}와 {y} 사이의 소수 : {sorted(prime_nums)}')
print(f'소수들의 합 : {sum(prime_nums)}')
