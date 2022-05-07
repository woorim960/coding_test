const { BADFLAGS } = require('dns');
const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
let input = fs.readFileSync(filePath).toString().trimEnd().split('\n');

class Queue {
  #idx;
  #queue;

  constructor() {
    this.length = 0;
    this.#idx = 0;
    this.#queue = [];
  }

  getElements() {
    return this.#queue.slice(this.#idx);
  }

  enqueue(el) {
    this.#queue.push(el);
    this.length++;
  }

  dequeue() {
    const firstElement = this.#queue[this.#idx];
    this.length--;
    this.#idx++;
    return firstElement;
  }

  pop() {
    this.length--;
    return this.#queue.pop();
  }
}

function solution(firstLine, ...miro) {
  const [N, M] = firstLine.split(' ').map(Number);
  // const zip = Array(N)
  //   .fill()
  //   .map(() => Array(M).fill(0));
  miro = miro.map((el) => el.split(''));

  return bfs(miro, 0, 0, N, M);
}

function bfs(miro, x, y, N, M) {
  const q = new Queue();
  q.enqueue([x, y]);

  const [dx, dy] = [
    [-1, +1, 0, 0],
    [0, 0, -1, +1],
  ];

  while (q.length) {
    [x, y] = q.dequeue();

    for (let i = 0; i < 4; i++) {
      const [nx, ny] = [x + dx[i], y + dy[i]];

      if (nx < 0 || ny < 0 || nx >= N || ny >= M) continue;
      if (miro[nx][ny] == 0) continue;
      if (miro[nx][ny] == 1) {
        miro[nx][ny] = +miro[x][y] + 1;
        q.enqueue([nx, ny]);
      }
    }
  }
  return miro[N - 1][M - 1];
}

console.log(solution(...input));
