import sys

input = sys.stdin.readline


def solve():
    n = int(input())
    mod = 15746

    if n == 1:
        print(1)
        return
    if n == 2:
        print(2)
        return

    # dp[i] = dp[i-1] + dp[i-2]
    prev2 = 1  # dp[1]
    prev1 = 2  # dp[2]

    for _ in range(3, n + 1):
        curr = (prev1 + prev2) % mod
        prev2, prev1 = prev1, curr

    print(prev1)


if __name__ == "__main__":
    solve()
