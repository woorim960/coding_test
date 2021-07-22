def binary_search(arr, target, low, cur, high):
  if target == arr[cur]:
    return cur + 1
  if low > high:
    return -1
  
  if target < arr[cur]:
    high = cur - 1
  elif target > arr[cur]:
    low = cur + 1
  return binary_search(arr, target, low, (low + high) // 2, high)

arr = list(map(int, input().split()))
target = int(input())
high = len(arr) - 1
print(binary_search(arr, target, 0, high // 2, high))
