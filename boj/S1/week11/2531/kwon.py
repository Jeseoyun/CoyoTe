
from collections import defaultdict

N, d, k, c = map(int, input().split())
sushi_list = [int(input()) for _ in range(N)]

counter = defaultdict(int)
kind = 0

for i in range(k):
    if counter[sushi_list[i]] == 0:
        kind += 1
    counter[sushi_list[i]] += 1

# 쿠폰
max_kind = kind + (1 if counter[c] == 0 else 0)

for i in range(1, N):
    remove = sushi_list[i - 1]
    counter[remove] -= 1
    if counter[remove] == 0:  # 더 이상 없으면 종류 수 감소
        kind -= 1

    cur = sushi_list[(i + k - 1) % N]
    if counter[cur] == 0:
        kind += 1
    counter[cur] += 1

    # 쿠폰
    total = kind + (1 if counter[c] == 0 else 0)
    max_kind = max(max_kind, total)  # 최대 종류 수 갱신

print(max_kind)