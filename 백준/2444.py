a = int(input())

for i in range(1, 2*a, 2):
    result = " " * int((2*a-i)/2)  + "*" * i
    print(result)

for i in range(2*(a-1), 1, -2):
    result1 = " " * int((2*a-i)/2) + "*" * (i-1)
    print(result1)