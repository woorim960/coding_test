const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

function solution(T, ...arr) {
  for (let i = 0; i < T; i++) {
    const [H, W, N] = arr[i].split(" ");
    let front = N % H;
    front = front ? front : H;
    let back = Math.ceil(N / H);
    let zero = back < 10 ? 0 : "";
    console.log(`${front || H}${zero}${back}`);
  }
}

solution(...input);

function solution2(n, ...arr) {
  let nArrNumber = Number(n);
  let newArr = arr.map((e) => e.split(" "));
  let nAnswer = "";

  for (let i = 0; i < nArrNumber; i++) {
    let H = newArr[i][0],
      N = newArr[i][2];

    let answerH = N % H;
    if (answerH === 0) {
      answerH = H;
    }

    let answerW = Math.ceil(N / H);
    answerW < 10 ? (answerW = String(0) + answerW) : answerW;

    nAnswer += `${answerH}${answerW}` + "\n";
  }
  return nAnswer;
}
