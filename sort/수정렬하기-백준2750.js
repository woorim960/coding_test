const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");

function solution(N, ...nums) {
  return nums.sort((a, b) => a - b).join("\n");
}

console.log(solution(...input));
