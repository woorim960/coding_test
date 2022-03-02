const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

function solution(N) {
  let [분자, 분모] = [1, 1];
  let [변경될_분자, 변경될_분모] = [0, 0];
  while (N > 1) {
    // console.log(`${분자}/${분모}`, N);
    N--;

    let [나눠진_분자, 나눠진_분모] = [분자 % 2, 분모 % 2];
    if (분자 === 1) {
      if (나눠진_분모) {
        // 분모 +1
        변경될_분모 = +1;
        변경될_분자 = 0;
      } else {
        // 분모 -1, 분자 +1
        변경될_분자 = +1;
        변경될_분모 = -1;
      }
    } else if (분모 === 1) {
      if (나눠진_분자) {
        // 분모 + 1, 분자 -1
        변경될_분모 = +1;
        변경될_분자 = -1;
      } else {
        // 분자 +1
        변경될_분모 = 0;
        변경될_분자 = +1;
      }
    }
    [분자, 분모] = [분자 + 변경될_분자, 분모 + 변경될_분모];
  }
  return `${분자}/${분모}`;
}

console.log(solution(...input[0].split(" ").map(Number)));
