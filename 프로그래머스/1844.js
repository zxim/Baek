function solution(maps) {
    const n = maps.length;           // 행 수
    const m = maps[0].length;        // 열 수

    const visited = Array.from({ length: n }, () => Array(m).fill(false)); // 방문 여부
    const queue = [[0, 0, 1]];       // 시작점과 초기 거리 1
    visited[0][0] = true;            // 시작점 방문 처리

    const dx = [0, 0, 1, -1];        // x 이동: 상하좌우
    const dy = [1, -1, 0, 0];        // y 이동

    while (queue.length > 0) {
        const [x, y, dist] = queue.shift(); // 현재 위치와 거리 추출

        if (x === n - 1 && y === m - 1) {   // 도착점에 도달
            return dist;                   // 현재 거리 반환
        }

        for (let i = 0; i < 4; i++) {
            const nx = x + dx[i];
            const ny = y + dy[i];

            if (
                nx >= 0 && ny >= 0 && nx < n && ny < m && // 맵 범위 내이고
                maps[nx][ny] === 1 &&                    // 벽이 아니며
                !visited[nx][ny]                         // 아직 방문하지 않은 곳
            ) {
                visited[nx][ny] = true;
                queue.push([nx, ny, dist + 1]);          // 거리 +1 해서 큐에 넣기
            }
        }
    }

    return -1; // 도달 불가능한 경우
}
