// 1번 문제, 100점
function solution(p) {
  let count = 0;
  const visited = [];
  p.forEach(([a, b]) => {
    let max, min;
    if (a > b) [max, min] = [a, b];
    else [max, min] = [b, a];

    try {
      if (visited[min][max]) count++;
      else visited[min][max] = true;
    } catch (e) {
      visited[min] = [];
      visited[min][max] = true;
    }
  });

  return count;
}

console.log(
  solution([
    [1, 3],
    [3, 1],
    [3, 5],
    [999, 5],
    [5, 999],
  ])
);
