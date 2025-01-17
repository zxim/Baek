n = int(input())

a = [list(map(int, input().split())) for _ in range(n)]
cost = []

dp = [[0] * 3 for i in range(n)]
dp[0] = a[0]

for i in range(1, n):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + a[i][0]        #인덱스 0으로 시작했을 시 다음 인덱스부터 최솟값을 누적해서 더함
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + a[i][1]        #인덱스 1으로 시작했을 시 다음 인덱스부터 최솟값을 누적해서 더함
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + a[i][2]        #인덱스 2으로 시작했을 시 다음 인덱스부터 최솟값을 누적해서 더함

print(min(dp[n-1]))         #최종 합 중에서 가장 작은 것 출력