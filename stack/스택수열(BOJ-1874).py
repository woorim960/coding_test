N = int(input())
example_stack = []
for _ in range(N):
  example_stack.append(int(input()))

init_stack = []
op_stack = []
cnt = 0
for i in range(1, N + 1):
  init_stack.append(i)
  op_stack.append('+')
  while (init_stack and example_stack and init_stack[-1] == example_stack[0]):
    example_stack.pop(0)
    init_stack.pop()
    op_stack.append('-')
    cnt += 1

if cnt == N:
  for op in op_stack:
    print(op)
else:
  print("NO")

  
