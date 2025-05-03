a, b = map(int, input().split())

result = list(map(int, input().split()))

result.sort()

print(result[a-b])