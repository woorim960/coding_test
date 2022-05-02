function combination(arr, selected) {
  if (selected <= 1) return arr.map((item) => [item]);

  const result = [];
  arr.forEach((fixed, idx, origin) => {
    const rest = origin.slice(idx + 1);
    const combinated = combination(rest, selected - 1);
    const attached = combinated.map((item) => [fixed, ...item]);
    result.push(...attached);
  });

  return result;
}

function solution(arr, n) {
  return combination(arr, n);
}

console.log(solution([1, 2, 3, 4, 5], 3));
