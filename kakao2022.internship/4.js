let line = [];
let answer = [];

function solution(n, paths, gates, summits) {
  const graph = {};
  for (let i = 0; i < paths.length; i++) {
    const [k, v, t] = paths[i];
    try {
      graph[k].push({ point: v, time: t });
    } catch (_) {
      graph[k] = [{ point: v, time: t }];
    }

    try {
      graph[v].push({ point: k, time: t });
    } catch (_) {
      graph[v] = [{ point: k, time: t }];
    }
  }

  const result = [];
  for (const start of gates) {
    dfs(graph, start, gates, summits, []);

    result.push(...answer);
    line = [];
    answer = [];
  }

  for (let i = 0; i < result.length; i++) {
    let max = 0;
    for (var j = 0; j < result[i].length; j++) {
      result[i][j] = { ...result[i][j] };
      if (max > result[i][j].time) {
        result[i][j].time = max;
      } else {
        max = result[i][j].time;
      }
    }
  }

  let min = 10000000;
  for (const nodes of result) {
    if (min > nodes[nodes.length - 1].time) {
      min = nodes[nodes.length - 1].time;
    }
  }
  let final = result.filter((nodes) => nodes[nodes.length - 1].time === min);

  for (const s of summits) {
    for (const nodes of final) {
      if (s === nodes[nodes.length - 1].point)
        return [nodes[nodes.length - 1].point, nodes[nodes.length - 1].time];
    }
  }
}

function dfs(graph, v, gates, summits, visited, toSave) {
  toSave = toSave ? toSave : { point: v, time: 0 };
  line.push(toSave);
  // console.log(line);
  visited[v] = true;
  if (summits.includes(v)) {
    visited[v] = false;
    return toSave;
  }

  for (const node of graph[v]) {
    if (!visited[node.point]) {
      if (gates.includes(node.point)) continue;
      let value = dfs(graph, node.point, gates, summits, visited, node);

      visited[v] = false;
      if (value) {
        // 산봉우리까지 찍고 왔다면 실행
        if (summits.includes(value.point)) {
          answer.push([...line]);
        }
        line.pop();
        value = false;
      }
    }
  }
  return line;
}

console.log(
  solution(
    6,
    [
      [1, 2, 3],
      [2, 3, 5],
      [2, 4, 2],
      [2, 5, 4],
      [3, 4, 4],
      [4, 5, 3],
      [4, 6, 1],
      [5, 6, 1],
    ],
    [1, 3],
    [5]
  )
);
