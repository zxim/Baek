const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const N = Number(input[0]);
const people = input[1].split(" ").map(Number);
const graph = Array.from({ length: N }, () => []);

for (let i = 0; i < N; i++) {
  const [_, ...neighbors] = input[i + 2].split(" ").map(Number);
  for (let neighbor of neighbors) {
    graph[i].push(neighbor - 1); // 0-indexed로 변환
  }
}

let minDiff = Infinity;

// 부분집합 조합 함수
function getCombinations(arr, r) {
  const results = [];
  if (r === 1) return arr.map((v) => [v]);
  arr.forEach((fixed, idx) => {
    const rest = arr.slice(idx + 1);
    const combis = getCombinations(rest, r - 1);
    const attached = combis.map((combi) => [fixed, ...combi]);
    results.push(...attached);
  });
  return results;
}

// DFS 연결 확인
function isConnected(group) {
  const visited = new Set();
  const stack = [group[0]];
  visited.add(group[0]);

  while (stack.length) {
    const cur = stack.pop();
    for (let next of graph[cur]) {
      if (group.includes(next) && !visited.has(next)) {
        visited.add(next);
        stack.push(next);
      }
    }
  }

  return visited.size === group.length;
}

// 1개~N/2까지 groupA 조합 생성
const nodes = Array.from({ length: N }, (_, i) => i);

for (let r = 1; r <= Math.floor(N / 2); r++) {
  const groupAs = getCombinations(nodes, r);
  for (let groupA of groupAs) {
    const groupB = nodes.filter((n) => !groupA.includes(n));

    if (isConnected(groupA) && isConnected(groupB)) {
      const sumA = groupA.reduce((acc, idx) => acc + people[idx], 0);
      const sumB = groupB.reduce((acc, idx) => acc + people[idx], 0);
      const diff = Math.abs(sumA - sumB);
      minDiff = Math.min(minDiff, diff);
    }
  }
}

console.log(minDiff === Infinity ? -1 : minDiff);
