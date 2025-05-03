def combination(m, n):
    # 조합 계산: C(m, n) = m! / (n! * (m-n)!)
    result = 1
    for i in range(n):
        result *= (m - i)
        result //= (i + 1)
    return result

# 입력 처리
T = int(input())  # 테스트 케이스 수
results = []

for _ in range(T):
    n, m = map(int, input().split())
    results.append(combination(m, n))

# 결과 출력
for res in results:
    print(res)
