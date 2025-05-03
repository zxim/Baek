n, m = map(int, input().split())
card = list(map(int, input().split()))
sum = []

for i in range(n):
    for k in range(i+1, n):
        for j in range(k+1, n):
            if card[i] + card[k] + card[j] > m:
                continue
            elif card[i] + card[k] + card[j] <= m:
                sum.append(card[i] + card[k] + card[j])

print(max(sum))