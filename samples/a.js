const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

function solution() {
  // 풀이
  const [a, b, c] = input[0].split(" ");
  return a;
}

console.log(solution());
