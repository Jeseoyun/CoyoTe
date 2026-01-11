def max_wine(wine, n):
    if n == 1:
        return wine[0]

    if n == 2:
        return wine[0] + wine[1]

    dp = [0] * n
    dp[0] = wine[0]
    dp[1] = wine[0] + wine[1]
    dp[2] = max(wine[0] + wine[1], wine[0] + wine[2], wine[1] + wine[2])

    for i in range(3, n):
        dp[i] = max(
            dp[i-1],  # i번째 잔 안마심
            dp[i-2] + wine[i],  # 직전 안마시고 i번째 마심
            dp[i-3] + wine[i-1] + wine[i]  # i-1, i 연속으로 마심
        )

    return dp[n-1]


def main():
    n = int(input())
    wine = [int(input()) for _ in range(n)]

    print(max_wine(wine, n))


if __name__ == "__main__":
    main()