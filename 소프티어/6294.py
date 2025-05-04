import sys

def main():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    scores = list(map(int, input().split()))

    prefix_sum = [0]
    for score in scores:
        prefix_sum.append(prefix_sum[-1] + score)

    for _ in range(K):
        A, B = map(int, input().split())
        total = prefix_sum[B] - prefix_sum[A - 1]
        average = total / (B - A + 1)

        print(f"{average:.2f}")

if __name__ == "__main__":
    main()
