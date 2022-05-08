const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
let input = fs.readFileSync(filePath).toString().trimEnd().split('\n');

function solution(cnt, ...rest) {
  let result = '';
  for (let i = 0; i < cnt; i++) {
    const [M, N, K] = rest.shift().split(' ');
    const ground = rest.splice(0, K);
    const graph = Array(+N)
      .fill()
      .map(() => Array(+M).fill(0));

    for (const str of ground) {
      const [k, v] = str.split(' ');
      graph[v][k] = 1;
    }

    const countedKimchi = countKimchi(graph, M, N);
    result += countedKimchi + '\n';
  }
  return result;
}

function countKimchi(graph, M, N) {
  let result = 0;
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < M; j++) {
      const countedKimchi = getCountedKimchi(graph, i, j, N, M);
      if (countedKimchi) result++;
    }
  }
  return result;
}

function getCountedKimchi(graph, x, y, N, M) {
  if (x < 0 || y < 0 || x >= N || y >= M) return false;
  if (graph[x][y]) {
    graph[x][y] = 0;
    getCountedKimchi(graph, x - 1, y, N, M);
    getCountedKimchi(graph, x + 1, y, N, M);
    getCountedKimchi(graph, x, y - 1, N, M);
    getCountedKimchi(graph, x, y + 1, N, M);
    return true;
  }
  return false;
}

console.log(solution(...input));
