a = int(input())

home, cnt = 1, 1
while a > home:
    home += 6 * cnt
    cnt += 1

print(cnt)