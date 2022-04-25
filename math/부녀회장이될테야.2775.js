// BOJ 2775
// https://www.acmicpc.net/problem/2775

const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

function solution(inputs) {
  const T = inputs[0];
  for (let i = 1; i < inputs.length; i += 2) {
    const [k, n] = [inputs[i], inputs[i + 1]];
    if (k === undefined || n === undefined) return;
    const builded = Array.from(Array(k + 1), () => Array(n + 1).fill(0));
    builded[0] = getArray(1, n);

    for (let j = 1; j <= k; j++) {
      for (let m = 1; m <= n; m++) {
        builded[j][m] = builded[j - 1][m] + builded[j][m - 1];
      }
    }
    console.log(builded[k][n]);
  }
}

function getArray(a, b) {
  const array = [0];
  for (let i = a; i < b + 1; i++) {
    array.push(i);
  }
  return array;
}

solution(input.map(Number));
