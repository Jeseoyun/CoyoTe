# 카드 구매하기 
# https://www.acmicpc.net/problem/11052

import sys 

inputf = sys.stdin.readline

def main():
    N = int(inputf())
    prices = [0]
    prices.extend(list(map(int, inputf().split())))
    # print(prices)  # debug 

    # dp[i] : i 장 을 살 때 얻을 수 있는 최대 가격 
    # 2장을 살 때 얻을 수 있는 최대 가격: max(1장 최대 가격 + 1장 가격, (0장 최대 가격) + 2장 가격)
    # 3장을 살 때 얻을 수 있는 최대 가격: max(1장 최대 가격 + 2장 가격, 2장 최대 가격 + 1장 가격, (0장 최대 가격) + 3장 가격)
    # 4장을 살 때 얻을 수 있는 최대 가격: max(1장 최대 가격 + 3장 가격, 2장 최대 가격 + 2장 가격, 3장 최대 가격 + 1장 가격, (0장 최대 가격) + 4장 가격)
    # i장을 살 때 얻을 수 있는 최대 가격: max(i-j장 최대 가격 + j장 가격 for j in range(1, j+1)) -> 점화식

    # 편의상 N+1 로 초기화 
    dp = [0 for _ in range(N+1)]
    # base case 
    dp[1] = prices[1]
    # start from 2
    for i in range(2, N+1):
        
        dp[i] = max((dp[i-j] + prices[j]) for j in range(1, i+1))

        # print(dp)  # debug
        
    print(dp[N])

    return 

if __name__=='__main__':
    main()