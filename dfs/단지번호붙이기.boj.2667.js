const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
let input = fs.readFileSync(filePath).toString().trimEnd().split('\n');

let countedHomeNumber = 0;
let graph = [];
function solution(N, ...home) {
  graph = [...home.reduce((acc, el) => [...acc, el.split('')], [])];
  let countedGroupNumber = 0;

  const result = [];
  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      countedHomeNumber = countHomeNumber(i, j, N);
      if (countedHomeNumber) {
        result.push(countedHomeNumber);
        countedGroupNumber++;
        countedHomeNumber = 0;
      }
    }
  }

  return `${countedGroupNumber}\n${result.sort((a, b) => a - b).join('\n')}`;
}

function countHomeNumber(x, y, N) {
  if (x < 0 || x >= N || y < 0 || y >= N) return false;

  if (graph[x][y] === '1') {
    graph[x][y] = '0';
    countedHomeNumber++;
    countHomeNumber(x - 1, y, N);
    countHomeNumber(x + 1, y, N);
    countHomeNumber(x, y - 1, N);
    countHomeNumber(x, y + 1, N);

    return countedHomeNumber;
  }
  return false;
}

console.log(solution(...input));
