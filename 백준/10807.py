N = int(input())
r = list(map(int, input().split()))
v = int(input())

sum = 0
for i in range(0, N):
    if v == r[i]:
        sum = sum + 1

print(sum)