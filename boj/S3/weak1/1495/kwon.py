# # 누가 봐도 DP
# from collections import deque

# N, S, M = map(int, input().split())
# V = [-1] + list(map(int, input().split()))

# # i 번째 연주에서 볼륨 j 가 가능한지 여부
# dp = [[False] * (M + 1) for _ in range(N + 1)]
# dp[0][S] = True

# cur = S
# q = deque([(cur, 0)])
# while q:
#     cur, idx = q.popleft()
#     idx += 1
#     if cur + V[idx] <= M and dp[idx][cur + V[idx]] == False:
#         dp[idx][cur + V[idx]] = True
#         if idx < N:
#             q.append((cur + V[idx], idx))
#     if cur - V[idx] >= 0 and dp[idx][cur - V[idx]] == False:
#         dp[idx][cur - V[idx]] = True
#         if idx < N:
#             q.append((cur - V[idx], idx))


# # print(*dp, sep="\n")
# possible_volumes = [i for i, possible in enumerate(dp[N]) if possible]
# print(possible_volumes[-1] if possible_volumes else -1)

# ########

N, S, M = map(int, input().split())
V = list(map(int, input().split()))

# 현재 가능한 볼륨들의 집합 (초기값: 시작 볼륨 S)
volumes = {S}

for v in V:
    next_volumes = set()
    for cur in volumes:
        if cur + v <= M:
            next_volumes.add(cur + v)
        if cur - v >= 0:
            next_volumes.add(cur - v)

    # 더 이상 가능한 볼륨이 없으면 조기 종료 가능
    if not next_volumes:
        print(-1)
        exit()

    volumes = next_volumes

# 마지막 곡까지 연주한 후 가능한 볼륨 중 최댓값
print(max(volumes))
