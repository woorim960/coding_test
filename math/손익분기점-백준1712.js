const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");

function solution(A, B, C) {
  // 풀이
  // A + (B * 판매 개수) < (C * 판매 개수) 가 되는 순간의 판매 개수를 반환
  // 단순히 위의 식으로 while문을 돌리면 시간초과가 아닌 틀렸다고 나옴
  // 이유는 판매 개수가 억단위가 넘어갈 경우 기본 js의 Number타입으로 데이터를 담을 수 없기 때문으로 예상.
  // BitInt로 테스트 해본결과 실패가 아닌 시간초과가 뜨는 것으로 신빙성을 더할 수 있다.

  // let cnt = BigInt(1);
  // while (A + B * cnt >= C * cnt) {
  //   cnt++;
  // }
  // return Number(cnt);
  if (B >= C) return -1;
  return Math.floor(A / (C - B)) + 1;
}

// BigInt로 테스트할 경우 숫자 형변환을 Number가 아닌 BigInt로 해줘야함.
console.log(solution(...input[0].split(" ").map(Number)));
