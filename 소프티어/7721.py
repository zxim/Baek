from decimal import Decimal, ROUND_HALF_UP
from itertools import product

# 입력
F = list(map(int, input().split()))

# 경기 조합
matches = [(0,1), (0,2), (0,3), (1,2), (1,3), (2,3)]

# 각 경기의 결과별 확률 계산
probabilities = []
for a, b in matches:
    total = Decimal(5 * (F[a] + F[b]))
    win_a = Decimal(4 * F[a]) / total
    draw = Decimal(F[a] + F[b]) / total
    win_b = Decimal(4 * F[b]) / total
    probabilities.append((win_a, draw, win_b))

# 모든 경기 결과 조합 탐색
total_probability = Decimal(0)
for outcomes in product((0,1,2), repeat=6):
    scores = [0, 0, 0, 0]
    prob = Decimal(1)
    for idx, outcome in enumerate(outcomes):
        a, b = matches[idx]
        if outcome == 0:
            scores[a] += 3
            prob *= probabilities[idx][0]
        elif outcome == 1:
            scores[a] += 1
            scores[b] += 1
            prob *= probabilities[idx][1]
        else:
            scores[b] += 3
            prob *= probabilities[idx][2]
    # 순위 결정
    ranking = sorted([(score, -i) for i, score in enumerate(scores)], reverse=True)
    if -ranking[0][1] == 0 or -ranking[1][1] == 0:
        total_probability += prob

# 결과 출력
result = total_probability * Decimal(100)
print(result.quantize(Decimal('0.001'), rounding=ROUND_HALF_UP))
