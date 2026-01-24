"""
dp[3]+P[1]  3개를 최대가격으로 사고 1개짜리 한 팩 구매
dp[2]+P[2]  2개를 최대가격으로 사고 2개짜리 한 팩 구매
dp[1]+P[3]
dp[0]+P[4]  4개짜리 한 팩만 구매
"""


def main():
    N = int(input())
    P = list(map(int, input().split()))
    P.insert(0, 0)

    dp = [0]*(N+1)

    for i in range(1, N+1):
        dp[i] = max(dp[i-j]+P[j] for j in range(1, i+1))

    print(dp[N])


    # dp = [0]*(N+1)  # N개 살 때 최댓값
    # dp[0] = P[0]
    # for i in range(1, N+1):
    #     for j in range(i+1):
    #         dp[i] = max(dp[i], dp[i-j]+P[j])
    #         # print(i, j, dp)
    # print(dp[-1])


if __name__ == "__main__":
    main()