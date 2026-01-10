# https://www.acmicpc.net/problem/2156
# 포두주 시식 

"""
DP 인 듯 하다.
조건: 연속된 3잔의 포도주를 마실 수 없다.

상태: dp 리스트에 정의 
- dp[i]: i 번째 포도주까지 마실 수 있는 최대 포도주 양

- dp[i] 에 들어갈 수 있는 경우의 수:
    경우 1. i 번째 잔을 마시지 않는 경우 -> dp[i-1]
    경우 2. i-1 번째 잔을 마시고, i 번째 잔을 마신 경우 -> i-2 번째 잔은 마시지 못함. -> dp[i-3] + dp[i-1] + wine[i]
    경우 3. i-1 번째 잔을 마시지 않고, i 번 째 잔을 마신 경우 -> dp[i-2] + wine[i]


"""

import sys 

inputf = sys.stdin.readline

def main():
    n = int(inputf())
    wine = list()
    dp = [0] * n
    for _ in range(n):
        wine.append(int(inputf()))
        
    # 포도주 잔의 개수가 3개 미만인 경우 처리
    if n == 1:
        print(wine[0])
        return
    elif n == 2:
        print(wine[0] + wine[1])
        return

    # basecase 
    dp[0] = wine[0]  # 첫 잔은 마실 수 있음. 
    dp[1] = wine[0] + wine[1]  # 두 잔은 연속으로 마실 수 있음.
    dp[2] = max(wine[0] + wine[1], wine[0] + wine[2], wine[1] + wine[2])  # 세 잔은 연속으로 마실 수 없음. -> 12, 13, 23 중에 선택

    for i in range(3, n):
        # 경우 1. i 번째 잔을 마시지 않는 경우 -> dp[i-1]
        # 경우 2. i-1 번째 잔을 마시고, i 번째 잔을 마신 경우 -> i-2 번째 잔은 마시지 못함. -> dp[i-3] + dp[i-1] + wine[i]
        # 경우 3. i-1 번째 잔을 마시지 않고, i 번 째 잔을 마신 경우 -> dp[i-2] + wine[i]
        dp[i] = max(dp[i-1], # case 1
                    dp[i-3] + wine[i-1] + wine[i], # case 2 
                    dp[i-2] + wine[i]) # case 3

    print(dp[n-1])
    return 


if __name__ == "__main__":
    main()