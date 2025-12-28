def solve():
    n = int(input())
    meetings = []
    for _ in range(n):
        meetings.append(list(map(int, input().split())))
    
    if n == 1:
        print(meetings[0][2])
        return
    
    # dp[i] : i번째 회의를 선택했을 때 최대 인원
    dp = [0] * n
    dp[0] = meetings[0][2]
    dp[1] = max(meetings[0][2], meetings[1][2])
    
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + meetings[i][2])
        
    print(dp[n-1])

if __name__ == "__main__":
    solve()