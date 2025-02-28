N, M = map(int, input().split())

rectangle = [list(input()) for _ in range(N)]

len_limit = min(N - 1 , M - 1)

ans = 0
for k in range(len_limit, -1, -1):
    # print(k)
    for x in range(M - k):
        for y in range(N - k):
            # print(x, y, k)
            if rectangle[y][x] == rectangle[y + k][x] == rectangle[y][x + k] == rectangle[y + k][x + k]:
                ans = k
                break
        else:
            continue
        break
    else:
        continue
    break

print((ans + 1) ** 2)