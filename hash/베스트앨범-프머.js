// https://programmers.co.kr/learn/courses/30/lessons/42579?language=javascript
function solution(genres, plays) {
  genres = genres.reduce((acc, genre, i) => {
    if (genre in acc) {
      acc[genre].push([i, plays[i]]);
    } else {
      acc[genre] = [[i, plays[i]]];
    }
    return acc;
  }, {});

  for (const genre in genres) {
    genres[genre].sort((a, b) => b[1] - a[1]);
  }

  return Object.entries(genres)
    .sort((a, b) => sum(b[1]) - sum(a[1]))
    .reduce((acc, song) => {
      const next = song[1].reduce((acc, score, i) => {
        if (i < 2) return [...acc, score[0]];
        return acc;
      }, []);
      return [...acc, ...next];
    }, []);
}

function sum(numbers) {
  return numbers.reduce((acc, con) => acc + con[1], 0);
}
