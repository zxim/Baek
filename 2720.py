t = int(input())

for i in range(t):
    sum = int(input())
    print(f"{sum//25} {(sum%25)//10} {((sum%25)%10)//5} {(((sum%25)%10)%5)//1}")