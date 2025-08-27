# dp[i][j] = i ~ j 까지 합쳤을 때 비용이 가장 작은 경우
#          = min(원래 i ~ j까지의 최소 비용, k를 거쳐 합칠 때 최소 비용(i < k < j))
INF = float("inf")
T = int(input())

for _ in range(T):
    K = int(input())
    files = list(map(int, input().split()))

    dp = [[0] * K for _ in range(K)]

    sum_list = [0] * (K + 1)
    for i in range(K):
        sum_list[i + 1] = sum_list[i] + files[i]

    for i in range(1, K):
        for j in range(i, K):
            dp[j - i][j] = INF
            for k in range(j - i, j):
                dp[j - i][j] = min(dp[j - i][j], dp[j - i][k] + dp[k + 1][j])
            # 누적 합으로 빠르게 구간 합 계산
            dp[j - i][j] += sum_list[j + 1] - sum_list[j - i]

    # print(*dp, sep="\n")
    print(dp[0][K - 1])
