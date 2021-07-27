import sys

def bin_search(arr, target, low, high):
  mid = (low + high) // 2

  if target == arr[mid]:
    return True
  if low >= high:
    return False
  
  if target < arr[mid]:
    high = mid - 1
  elif target > arr[mid]:
    low = mid + 1
  return bin_search(arr, target, low, high)

N = int(input())
bases = sorted(map(int, sys.stdin.readline().rstrip().split()))
M = int(input())
searches = list(map(int, sys.stdin.readline().rstrip().split()))

for search in searches:
  if bin_search(bases, search, 0, len(bases) - 1):
    print(1)
  else:
    print(0)
