// https://www.acmicpc.net/problem/11047
const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
let input = fs.readFileSync(filePath).toString().trim().split('\n');

function solution(A, ...moneys) {
  let [N, K] = A.split(' ');
  let shere = 0;
  for (const money of moneys.reverse()) {
    shere += parseInt(K / money);
    K %= money;
    if (K <= 0) return shere;
  }
}

console.log(solution(...input));
