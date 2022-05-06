const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
let input = fs.readFileSync(filePath).toString().trimEnd().split('\n');

let result = '';
function solution(input, ...vectors) {
  const [N, M, start] = input.split(' ');
  const graph = makeGraph(vectors, M);

  getDFS(start, graph, []);
  const dfs = result;
  result = '';
  getBFS(start, graph, []);
  const bfs = result;

  return dfs + '\n' + bfs;
}

function getDFS(v, graph, visited) {
  visited[v] = true;
  result += v + ' ';
  if (!(v in graph)) return;
  for (const node of graph[v]) {
    if (!visited[node]) {
      getDFS(node, graph, visited);
    }
  }
}

function getBFS(v, graph, visited) {
  visited[v] = true;
  result += v + ' ';
  if (!(v in graph)) return;

  const queue = [...graph[v]];
  while (queue.length) {
    const node = queue.splice(0, 1);
    if (!visited[node]) {
      visited[node] = true;
      result += node + ' ';
      queue.push(...graph[node]);
    }
  }
}

function makeGraph(vectors, M) {
  const graph = {};
  for (let i = 0; i < M; i++) {
    const [k, v] = vectors[i].split(' ');
    try {
      graph[k].push(v);
    } catch (e) {
      graph[k] = [v];
    }

    try {
      graph[v].push(k);
    } catch (e) {
      graph[v] = [k];
    }
  }

  for (const k in graph) {
    graph[k].sort((a, b) => a - b);
  }
  return graph;
}

console.log(solution(...input));
