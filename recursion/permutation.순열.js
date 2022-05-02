function permutation(arr, selected) {
  if (selected <= 1) return arr.map((item) => [item]);

  const result = [];
  arr.forEach((fixed, idx, origin) => {
    const rest = [...origin.slice(0, idx), ...origin.slice(idx + 1)];
    const permutated = permutation(rest, selected - 1);
    const attached = permutated.map((item) => [fixed, ...item]);
    result.push(...attached);
  });

  return result;
}

function solution(arr, n) {
  return permutation(arr, n);
}

console.log(solution([1, 2, 3, 4, 5], 2));
