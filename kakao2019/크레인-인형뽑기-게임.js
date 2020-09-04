function solution(board, moves) {
    let stack = [0];
    let board_cnt = board.length;
    let cnt = 0
    
    for (let mv of moves) {
        for (let i=0; i<board_cnt; i++) {
            let item = board[i][mv-1];
            board[i][mv-1] = 0;
            
            if (item !== 0) {
                let idx = stack.push(item);
                if (stack[idx-2] === stack[idx-1]) {
                    stack.pop();
                    stack.pop();
                    cnt += 2;
                }
                break;
            }
        }
    }
    return cnt;
}
