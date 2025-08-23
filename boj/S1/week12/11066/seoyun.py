INF = float('inf')


def main():
    T = int(input())

    for _ in range(T):
        K = int(input())
        files = list(map(int, input().split()))

        # prefix_sum[i] = files[0]부터 files[i-1] 까지의 합
        prefix_sum = [0] * (K+1)
        for i in range(K):
            prefix_sum[i+1] = prefix_sum[i] + files[i]

        dp = [[0]*K for _ in range(K)]
        for length in range(2, K+1):  # 2~K개까지 구간
            for start in range(K-length+1):
                end = start + length - 1
                dp[start][end] = INF

                for mid in range(start, end):
                    merge_cost = prefix_sum[end+1] - prefix_sum[start]
                    cost = dp[start][mid] + dp[mid+1][end] + merge_cost

                    dp[start][end] = min(dp[start][end], cost)
                    # print(start, end, mid)
                    # print(dp)

        print(dp[0][K-1])


if __name__ == "__main__":
    main()



if __name__ == "__main__":
    main()


###################################################################

# 츄라이 1) Greedy적 접근. 파일 크기가 가장 작은 두 놈 뽑아서 계속 합친다 => 틀림
# 이유: 소설 내용이 아무거나 2개 뽑아셔 합쳐지면 섞여버림. 무조건 연속된 두 놈을 뽑아서 합쳐야 한다.
# 문제 조건 똑바로 안읽어서 틀림 이슈

# import heapq
#
#
# def main():
#     T = int(input())
#
#     for _ in range(T):
#         K = int(input())
#         files = list(map(int, input().split()))
#
#         cost = 0
#
#         while len(files) != 1:
#             heapq.heapify(files)
#             print(files)
#
#             min_size_a = heapq.heappop(files)
#             min_size_b = heapq.heappop(files)
#
#             tmp_file = min_size_a + min_size_b
#
#             heapq.heappush(files, tmp_file)
#             cost += tmp_file
#
#         print(cost)
#
#
# if __name__ == "__main__":
#     main()