const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

function solution(A, B, V) {
  return Math.ceil((V - B) / (A - B));
}

console.log(solution(...input[0].split(" ").map(Number)));
