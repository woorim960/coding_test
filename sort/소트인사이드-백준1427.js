const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");

function solution(nums) {
  return [...nums].sort((a, b) => b - a).join("");
}

console.log(solution(input[0]));
