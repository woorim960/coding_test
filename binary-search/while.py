def binary_search(arr, target, low, high):
  cur = high // 2

  while low <= high:
    if target == arr[cur]:
      return cur + 1
    elif target < arr[cur]:
      high = cur - 1
    elif target > arr[cur]:
      low = cur + 1
    cur = low + ((high - low) // 2) # (low + high) // 2
  return -1

arr = list(map(int, input().split()))
target = int(input())
print(binary_search(arr, target, 0, len(arr) - 1))
