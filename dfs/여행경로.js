let answer = [];

function solution(tickets) {
  const graph = getMakedGraph(tickets);

  const result = [];
  dfs("ICN", graph, result, tickets.length + 1);
  console.log(answer);
  return answer;
}
function dfs(v, graph, result, targetCnt) {
  console.log(result);
  if (graph[v] === undefined) {
    result.push(v);
    if (result.length === targetCnt) {
      answer = result;
      return true;
    }
    result.pop();
    return false;
  }

  result.push(v);
  beAbleToGoPlace = graph[v]?.filter((el) => !el.visit) ?? [];

  for (const node of beAbleToGoPlace) {
    if (!node.visit) {
      node.visit = true;
      if (dfs(node.place, graph, result, targetCnt)) {
        answer = result;
        return true;
      }
      node.visit = false;
    }
  }

  if (result.length === targetCnt) {
    answer = result;
    return true;
  }

  result.pop();
  return false;
}

function getMakedGraph(tickets) {
  tickets = tickets.reduce((acc, ticket) => {
    if (acc.hasOwnProperty(ticket[0]))
      acc[ticket[0]].push({ place: ticket[1], visit: false });
    else acc[ticket[0]] = [{ place: ticket[1], visit: false }];
    return acc;
  }, {});

  for (const k in tickets) {
    tickets[k].sort((a, b) => {
      if (a.place === b.place) return 0;
      return a.place > b.place ? 1 : -1;
    });
  }
  return tickets;
}

function isSame(a, b) {
  if (a.length !== b.length) return false;
  for (let i = 0; i < a.length; i++) {
    if (a[i] !== b[i]) return false;
  }
  return true;
}

console.log(
  isSame(
    solution([
      ["ICN", "B"],
      ["B", "ICN"],
      ["ICN", "A"],
      ["A", "D"],
      ["D", "A"],
    ]),
    ["ICN", "B", "ICN", "A", "D", "A"]
  )
);
