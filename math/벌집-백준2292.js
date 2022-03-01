const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

function solution(N) {
  let [acc, cnt] = [1, 1];
  while (N > acc) {
    acc += cnt * 6;
    cnt++;
  }
  return cnt;
}

console.log(solution(...input[0].split(" ").map(Number)));
