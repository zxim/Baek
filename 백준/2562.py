r = []

for i in range(0, 9):
    a = int(input())
    r.append(a)

a = r.index(max(r))
print(max(r))
print(a+1)