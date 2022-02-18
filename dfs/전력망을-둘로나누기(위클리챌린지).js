function solution(n, wires) {
    const graph = [];
    let visit = [];
    let cnt = 0;
    
    // 연결된 간선의 배열 초기화
    wires.forEach(([v1, v2]) => {
        graph[v1] = graph[v1] ? [ ...graph[v1], v2 ] : [v2];
        graph[v2] = graph[v2] ? [ ...graph[v2], v1 ] : [v1];
    });
    
    
    return wires.reduce((c, [v1, v2]) => {
        // 간선 삭제
        graph[v1].shift(0)
        graph[v2].shift(0)
        
        // 현재 연결된 간선의 개수 세기
        cnt = dfs(1, 0, graph, visit);
        visit = [];
        
        // 삭제된 노드 재연결
        graph[v1].push(v2);
        graph[v2].push(v1);
        
        return Math.min(c, Math.abs((n - cnt) - cnt));
    }, n);
}

function dfs(node, cnt, graph, visit) {
    visit[node] = true;
    cnt++;
    
    for (const v of graph[node]) {
        if (!visit[v]) cnt = dfs(v, cnt, graph, visit);
    }
    return cnt;
}
