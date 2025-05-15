const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

// 입력 파싱
const N = +input[0];
const K = +input[1];
const apples = new Set();
for (let i = 2; i < 2 + K; i++) {
  const [r, c] = input[i].split(' ').map(Number);
  apples.add(`${r - 1},${c - 1}`); // 0-indexed
}

const L = +input[2 + K];
const turnInfo = new Map();
for (let i = 3 + K; i < 3 + K + L; i++) {
  const [X, C] = input[i].split(' ');
  turnInfo.set(+X, C);
}

// 방향: 오른, 아래, 왼, 위
const dx = [0, 1, 0, -1];
const dy = [1, 0, -1, 0];

let direction = 0;
let time = 0;
let snake = [[0, 0]]; // 뱀의 좌표 배열, 맨 앞이 머리
const snakeSet = new Set(['0,0']);

while (true) {
  time++;

  // 머리 위치 이동
  const [hx, hy] = snake[0];
  const nx = hx + dx[direction];
  const ny = hy + dy[direction];

  const key = `${nx},${ny}`;

  // 벽 또는 자기 몸에 부딪히면 종료
  if (nx < 0 || ny < 0 || nx >= N || ny >= N || snakeSet.has(key)) {
    console.log(time);
    break;
  }

  // 머리 추가
  snake.unshift([nx, ny]);
  snakeSet.add(key);

  // 사과가 없다면 꼬리 제거
  if (!apples.has(key)) {
    const [tx, ty] = snake.pop();
    snakeSet.delete(`${tx},${ty}`);
  } else {
    apples.delete(key); // 사과 먹기
  }

  // 방향 전환
  if (turnInfo.has(time)) {
    const turn = turnInfo.get(time);
    if (turn === 'D') {
      direction = (direction + 1) % 4;
    } else {
      direction = (direction + 3) % 4; // 왼쪽 회전
    }
  }
}
