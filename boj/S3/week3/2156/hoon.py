# 백준: 포도주 시식
# 특정 부분을 선택했을 때, 이후 선택에 영향을 주는 문제 구조이기 때문에 일단 DP를 고려함.
import sys
inputf = sys.stdin.readline

def main():
    num = int(inputf())

    wine = []
    for _ in range(num):
        wine.append(int(inputf()))
    
    dp = [0] * 10001

    # num이 1일 때, 2일 때 처리
    dp[1] = wine[0]

    if num >= 2:
        dp[2] = wine[0] + wine[1] #그냥 연달아 마시면 됨
    
    if num >= 3:
        # 2보다 크면 세가지 경우 중 하나 골라야 함.
        dp[3] = max(dp[2], wine[0] + wine[2], wine[1] + wine[2])

    # 두번 연속 마시는 경우, 한번째 마시는 경우(이전에는 안 마셨을 때 중에 최대), 이번에 거르는 경우로 나눠서 max
    for i in range(4, num+1):
        # dp는 1부터 시작하고 wine은 0부터 시작하는 실수.
        # dp[i] = max(dp[i-3] + wine[i-1] + wine[i], dp[i-2] + wine[i], dp[i-1])
        dp[i] = max(dp[i-3] + wine[i-2] + wine[i-1], dp[i-2] + wine[i-1], dp[i-1])


    print(dp[num])

if __name__ == "__main__":
    main()