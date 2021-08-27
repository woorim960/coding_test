N, C = map(int, input().split())
locates = sorted([int(input()) for _ in range(N)])

def solution(target):
  start = 0
  end = locates[-1]

  while start <= end:
    mid = (start + end) // 2
    # print(f'mid: {mid}')
    cnt = 1
    current = locates[0]
    if (locates[0] + mid * (target - 1)) <= locates[-1]:
      # print(locates)
      for i in range(1, len(locates)):
        # print(current, mid, locates[i])
        if current + mid <= locates[i]:
          # print(f'current, mid, locates[{i}] => {current} {mid} {locates[i]}')
          current = locates[i]
          cnt += 1
      # print(f'cnt: {cnt}')
      if cnt < target:
        end = mid - 1
      else:
        start = mid + 1
    else:
      end = mid - 1
  return end

print(solution(C))