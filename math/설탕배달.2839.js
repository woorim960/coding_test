const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

function solution(N) {
  let count = 0;
  while (N > 0) {
    if (N % 5 === 0) {
      count += N / 5;
      console.log(count);
      return;
    }

    N -= 3;
    count++;
    if (N === 0) {
      console.log(count);
      return;
    }
  }
  console.log(-1);
}

solution(input[0]);
