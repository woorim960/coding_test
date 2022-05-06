const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
let input = fs.readFileSync(filePath).toString().trimEnd().split('\n');

let result = 0;
function solution(comNumber, lineNumber, ...vectors) {
  const graph = makeGraph(vectors, lineNumber);

  getDFS(1, graph, []);

  return result - 1;
}

function getDFS(v, graph, visited) {
  visited[v] = true;
  result++;
  if (!(v in graph)) return;
  for (const node of graph[v]) {
    if (!visited[node]) {
      getDFS(node, graph, visited);
    }
  }
}

// function getBFS(v, graph, visited) {
//   visited[v] = true;
//   result += v + ' ';
//   if (!(v in graph)) return;

//   const queue = [...graph[v]];
//   while (queue.length) {
//     const node = queue.splice(0, 1);
//     if (!visited[node]) {
//       visited[node] = true;
//       result += node + ' ';
//       queue.push(...graph[node]);
//     }
//   }
// }

function makeGraph(vectors, lineNumber) {
  const graph = {};
  for (let i = 0; i < lineNumber; i++) {
    const [k, v] = vectors[i].split(' ');

    try {
      graph[k].push(v);
    } catch {
      graph[k] = [v];
    }

    try {
      graph[v].push(k);
    } catch {
      graph[v] = [k];
    }
  }
  return graph;
}

console.log(solution(...input));
