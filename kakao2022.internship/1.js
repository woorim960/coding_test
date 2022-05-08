function solution(survey, choices) {
  const scores = [0, 3, 2, 1, 0, 1, 2, 3];
  const characterTypes = ['RT', 'CF', 'JM', 'AN'];
  const types = {
    A: 0,
    N: 0,
    C: 0,
    M: 0,
    F: 0,
    R: 0,
    T: 0,
    J: 0,
  };

  for (let i = 0; i < survey.length; i++) {
    const [a, b] = survey[i].split('');
    if (choices[i] < 4) types[a] += scores[choices[i]];
    else types[b] += scores[choices[i]];
  }

  let result = '';
  for (let i = 0; i < characterTypes.length; i++) {
    const [a, b] = characterTypes[i].split('');
    if (types[a] === types[b]) result += [a, b].sort()[0];
    else if (types[a] > types[b]) result += a;
    else result += b;
  }

  return result;
}
