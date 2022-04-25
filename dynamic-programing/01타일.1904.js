const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

function solution(N) {
  const memory = [0, 1, 2, 3, 5, 8, 13].map(BigInt);

  for (let i = 7; i <= N; i++) {
    memory.push((memory[i - 1] + memory[i - 2]) % BigInt(15746));
  }

  return String(memory[N]);
}

console.log(solution(input[0]));
