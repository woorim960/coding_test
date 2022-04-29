// 3번 문제, 54.5점
function solution(n, r, c) {
  // n 값이 1천만일 때 "n * n"인 1000조개의 숫자를 저장시켜야하는데
  // 이 과정에서 메모리 초과가 발생하는 것 같다.
  // 각 값의 크기는 문제가 없고, 모든 값을 메모리에 할당하지 않고 풀어야한다. (수학적 접근 필요)
  // 수학적으로 접근하는 과정에서
  // 1 -> 3 -> 6 -> 10 -> 15 -> 19 -> 22 -> 24 -> 25 의 관계를 찾아 각 값을 O(n)로 찾는 알고리즘은 알았다.
  // 다만, arr[r][c]의 값을 O(n)로 찾는 수식을 고민해보다 시간 부족으로 인해 실패..

  // 아래 풀이는 무지성으로 모든 값을 '1 - (n ** 2)'까지 메모리에 할당한 뒤
  // arr[r][c]를 반환한다. 메모리 문제로 통과하지 못하는 테스트케이스가 존재하는 것으로 추측.
  const TOTAL = n ** 2;
  const array = Array.from(Array(n), () => []);
  let cnt = 1;

  let [x, y] = [0, -1];
  let dir = "UP";

  while (cnt <= TOTAL) {
    if (x === n - 1 && cnt <= TOTAL) {
      array[++y][x] = cnt++;
      dir = "DOWN";
    }
    if (y === n - 1 && cnt <= TOTAL) {
      array[y][++x] = cnt++;
      dir = "UP";
    }
    if (y === 0 && cnt <= TOTAL) {
      array[y][++x] = cnt++;
      dir = "DOWN";
    }
    if (x === 0 && cnt <= TOTAL) {
      array[++y][x] = cnt++;
      dir = "UP";
    }
    if (dir === "UP" && x !== n - 1 && y !== 0 && cnt <= TOTAL)
      array[--y][++x] = cnt++;
    if (dir === "DOWN" && y !== n - 1 && x !== 0 && cnt <= TOTAL)
      array[++y][--x] = cnt++;

    if (array[r - 1][c - 1]) return array[r - 1][c - 1];
  }

  return array[r - 1][c - 1];
}

console.log(solution(5, 3, 2));
console.log(solution(6, 5, 4));
console.log(solution(10000, 5, 4));
