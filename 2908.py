a, b = input().split()

a1 = a[2] + a[1] + a[0]
b1 = b[2] + b[1] + b[0]

if int(a1) < int(b1):
    print(b1)
else:
    print(a1)