const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
let input = fs.readFileSync(filePath).toString().trim().split('\n');

const dp = [];

function solution(N) {
  if (N <= 1) return N;
  if (dp[N]) return dp[N];
  dp[N] = solution(N - 1) + solution(N - 2);
  return dp[N];
}

console.log(solution(input[0]));
