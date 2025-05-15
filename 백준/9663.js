const fs = require("fs");
const N = Number(fs.readFileSync("/dev/stdin").toString().trim());

let answer = 0;

// 상태를 저장할 배열
const col = Array(N).fill(false);         // 같은 열
const diag1 = Array(2 * N).fill(false);   // ↘ 방향 대각선 (row + col)
const diag2 = Array(2 * N).fill(false);   // ↙ 방향 대각선 (row - col + N)

function dfs(row) {
  if (row === N) {
    answer++;
    return;
  }

  for (let c = 0; c < N; c++) {
    if (col[c] || diag1[row + c] || diag2[row - c + N]) continue;

    // 퀸 놓기 (상태 저장)
    col[c] = diag1[row + c] = diag2[row - c + N] = true;

    dfs(row + 1);  // 다음 행으로

    // 퀸 빼기 (백트래킹)
    col[c] = diag1[row + c] = diag2[row - c + N] = false;
  }
}

dfs(0);
console.log(answer);
