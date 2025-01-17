n = int(input())
card_n = list(map(int,input().split()))

m = int(input())
card_m = list(map(int,input().split()))
result = []
for i in range(m):
    for k in range(n):
        if card_m[i] == card_n[k]:
            result[i] = 1
        else:
            result[i] = 0

    if result[i] == 1:
        print("1", end = ' ')
    else:
        print("0", end = ' ')