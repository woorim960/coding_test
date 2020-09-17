N, M = map(int, input().split())
board = '''\
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
WWWWWWWWWWBWB
WWWWWWWWWWBWB
'''
board = list(map(list, board.split('\n')))
# board = [input() for _ in range(N)]

def get_changed_count(x, y, el) :
    cnt = 0
    for i in range(8) :
        for j in range(8) :
            if i % 2 == 0 :
                if j % 2 == 0 :
                    if board[i+x][j+y] == el[0] :
                        continue
                    cnt += 1
                else :
                    if board[i+x][j+y] == el[1] :
                        continue
                    cnt += 1
            else :
                if j % 2 == 0 :
                    if board[i+x][j+y] == el[1] :
                        continue
                    cnt += 1
                else :
                    if board[i+x][j+y] == el[0] :
                        continue
                    cnt += 1
    return cnt

result = []
for i in range(N-7) :
    for j in range(M-7) :
        result.append(get_changed_count(i, j, ['W', 'B']))
        result.append(get_changed_count(i, j, ['B', 'W']))

print(min(result))
