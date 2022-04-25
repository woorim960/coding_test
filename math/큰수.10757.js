const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

function solution([a, b]) {
  console.log(String(a + b));
}

solution(input[0].split(" ").map(BigInt));
