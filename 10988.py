a = input()
t = 1

for i in range(len(a)):
    if a[i] != a[len(a)-i-1]:
        print("0")
        t = 0
        break

if t == 1:
    print(t)