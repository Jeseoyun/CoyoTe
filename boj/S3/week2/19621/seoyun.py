def main():
    N = int(input())
    meeting = [list(map(int, input().split())) for _ in range(N)]
    # print(meeting)

    dp = [[0]*2 for _ in range(N)]
    dp[0][1] = meeting[0][2]

    for i in range(1, N):
        # 선택 안하는 경우
        dp[i][0] = max(dp[i-1][0], dp[i-1][1])  # 이전 값 중 최댓값 가져오기

        # 선택 하는 경우
        dp[i][1] = dp[i-1][0] + meeting[i][2]  # 무조건 이전에 선택 안 한  경우 + 현재 인원

    print(max(dp[N-1]))


if __name__ == "__main__":
    main()