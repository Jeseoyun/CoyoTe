# 1 / 00 사용 가능
# 만들 수 있는 모든 가짓수 세기


'''리스트 사용 -> 메모리 초과'''
# def main():
#     N = int(input())
#     dp = [0] * (N+1)
#
#     dp[1] = 1  # 1
#     dp[2] = 2  # 11/00
#
#     if N >= 3:
#         for i in range(3, N+1):
#             # 마지막이 1로 끝나는 경우: 그 앞은 길이가 n-1이 됨
#             # 2로 끝나는 경우: 그 앞은 길이가 n-2가 됨
#             # 두 경우의 합으로 계싼
#             dp[i] = dp[i-1] + dp[i-2]
#
#     print(dp[N]%15746)


def main():
    N = int(input())

    # 1개 이전 값, 2개 이전 값 기록
    a, b = 1, 2

    for _ in range(3, N+1):
        a, b = b, (a + b) % 15746

    print(b if N > 1 else a)


if __name__ =="__main__":
    main()