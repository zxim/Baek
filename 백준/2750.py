r = []

a = int(input())
for i in range(a):
    num = int(input())
    r.append(num)

r.sort()
for i in range(a):
    print(r[i])