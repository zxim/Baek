const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const N = Number(input[0]);
const lines = input.slice(1).map(line => line.split(' ').map(Number));

lines.sort((a, b) => a[0] - b[0]);

const bLines = lines.map(line => line[1]);

const dp = Array(N).fill(1);

for (let i = 1; i < N; i++) {
    for (let j = 0; j < i; j++) {
        if (bLines[j] < bLines[i]) {
            dp[i] = Math.max(dp[i], dp[j] + 1);
        }
    }
}

const maxLIS = Math.max(...dp);
console.log(N - maxLIS);
