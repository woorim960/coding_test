const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
let input = fs.readFileSync(filePath).toString().trim().split('\n');

function solution(N) {
  return N <= 1 ? 1 : N * solution(N - 1);
}

console.log(solution(Number(input[0])));
