function solution(n) {
  const [A, B] = [4, 13];
  const arr = [];
  let cnt = 1;
  while (!arr[n]) {
    arr.push(recursion(A, B));

    cnt++;
  }
}

console.log(solution(1));
console.log(solution(2));
console.log(solution(3));
console.log(solution(4));
