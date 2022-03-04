// 참고 알고리즘 : https://youtu.be/AogMbfRwguk
const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");

function solution(N) {
  const K = (BigInt(1) << BigInt(N)) - BigInt(1);
  console.log(String(K));
  if (N <= 20) console.log(hanoi(N, 1, 3));
}

function hanoi(n, from, to) {
  const mid = 6 - (from + to);
  if (n <= 1) {
    return `${from} ${to}\n`;
  } else {
    let s = "";
    s += hanoi(n - 1, from, mid);
    s += hanoi(1, from, to);
    s += hanoi(n - 1, mid, to);
    return s;
  }
}

solution(Number(input[0]));
