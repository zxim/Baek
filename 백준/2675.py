t = int(input())

for i in range(t):
    r, s = map(str, input().split())
    ln = len(s)
    for k in range(ln):
        print(s[k]*int(r), end = "")
    print()