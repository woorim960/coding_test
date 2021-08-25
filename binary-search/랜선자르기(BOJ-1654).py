import sys

K, N = map(int, input().split())
lines = [int(sys.stdin.readline()) for _ in range(K)]

def solution(K, target, lines):
  start = 1
  end = max(lines)

  while start <= end:
    slicing_length = (start + end) // 2

    total_line_count = 0
    for line in lines:
      total_line_count += line // slicing_length

    if total_line_count < target:
      end = slicing_length - 1
    elif total_line_count >= target:
      start = slicing_length + 1
    # elif total_line_count == target:
    #   break
  return end

print(solution(K, N, lines))

