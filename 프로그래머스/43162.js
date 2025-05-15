function solution(n, computers) {
    const visited = Array(n).fill(false); 
    let answer = 0; 

    function dfs(node) {
        visited[node] = true;

        for (let i = 0; i < n; i++) {
            if (computers[node][i] === 1 && !visited[i]) {
                dfs(i);
            }
        }
    }

    for (let i = 0; i < n; i++) {
        if (!visited[i]) {
            dfs(i);     
            answer++;    
        }
    }

    return answer;
}
