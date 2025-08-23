INF = float('inf')

n = int(input())

total_sum = 0
select_idx = []
for _ in range(n):
    L = int(input())
    jewels = list(map(int, input().split()))

    cum_sum = [0] * (L + 1)
    for i in range(1, L + 1):
        cum_sum[i] += cum_sum[i - 1] + jewels[i - 1]
    
    # print(cum_sum)
    
    max_sum = -INF
    max_start = 1
    max_end = L

    for k in range(L, 0, -1):
        # print("len:", k)
        is_max = False
        for i in range(0, L - k + 1):
            # print(i, k + i)
            part_sum = cum_sum[k + i] - cum_sum[i]
            # print(part_sum)
            if max_sum > part_sum:
                continue
            # 최대값과 같고 이미 앞에서 그 값이 나온 경우
            elif max_sum == part_sum and is_max:
                continue

            max_sum = part_sum
            max_start = i + 1
            max_end = k + i
            is_max = True
    # print("max_sum:", max_sum)
    total_sum += max_sum
    # print(max_start, max_end)
    select_idx.append((max_start, max_end))


print(total_sum)
for result in select_idx:
    print(*result)