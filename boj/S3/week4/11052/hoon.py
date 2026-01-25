# 백준: 카드 구매하기
# 문제 자체는 일부러 비효율적으로 구매해야하는 거지만
# 지불하는 비용이 가치라고 생각하면 사실 배낭이랑 똑같은 구조임.

import sys
inputf = sys.stdin.readline

def main():
    num = int(inputf())
    num_arr = list(map(int, inputf().split()))
    # print(num)
    # print(num_arr)

    # dp 0은 아무것도 고르지 않았을 때가 됨
    dp = [0] * (num + 1)

    for i in range(1, num+1):
        for j in range(0, i):
            dp[i] = max(dp[i], dp[i-(j+1)] + num_arr[j])

    print(dp[-1])


if __name__ == "__main__":
    main()