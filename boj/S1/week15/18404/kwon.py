from collections import deque

N, M = map(int, input().split())

dxy = ((1, 2), (2, 1), (-1, 2), (2, -1), (1, -2), (-2, 1), (-1, -2), (-2, -1))

x, y = map(int, input().split())

enemy_list = [tuple(map(int, input().split())) for _ in range(M)]
result = [0] * M

q = deque([(x, y, 1)])
find_cnt = 0
visited = set([(x, y)])

while q:
    cur_x, cur_y, t = q.popleft()

    for dx, dy in dxy:
        n_x, n_y = cur_x + dx, cur_y + dy
        if (n_x, n_y) in visited:
            continue
        if (n_x, n_y) in enemy_list:
            enemy_idx = enemy_list.index((n_x, n_y))
            if result[enemy_idx] != 0:
                continue
            result[enemy_idx] = t
            find_cnt += 1
        # print(result)
        # print(find_cnt, M)
        if find_cnt == M:
            break
        q.append((n_x, n_y, t + 1))
        visited.add((n_x, n_y))
    else:
        continue
    break

print(*result)





#####################################################

# from math import ceil

# N, M = map(int, input().split())
# x, y = map(int, input().split())

# enemy_list = tuple(tuple(map(int, input().split())) for _ in range(M))

# def get_move_cnt(x, y, e_x, e_y):
#     # 차이 작은 쪽의 최소 이동 개수
#     diff_x, diff_y = abs(e_x - x), abs(e_y - y)
#     diff_x = diff_x if diff_x != 0 else 4
#     diff_y = diff_y if diff_y != 0 else 4

#     if diff_x <= diff_y:
#         move = ceil(diff_x / 2)
#         one_cnt = diff_x % 2
#         two_cnt = diff_x // 2
#         max_diff = diff_y
#     else:
#         move = ceil(diff_y / 2)
#         one_cnt = diff_y % 2
#         two_cnt = diff_y // 2
#         max_diff = diff_x
#     # print("move1:", move)
#     # 차이 큰 쪽을 작은 쪽에서 이미 결정된 숫자의 짝만큼 진행
#     # print(max_diff)
#     for _ in range(two_cnt):
#         if max_diff >= 0:
#             max_diff -= 1
#         else:
#             max_diff += 1
#     # print(max_diff)
#     if max_diff >= 0:
#         max_diff -= one_cnt * 2
#     else:
#         max_diff += one_cnt * 2

#     # print(max_diff)
#     # 남은 거리 진행
#     move += ceil(abs(max_diff) / 2)
#     return move


# for e_x, e_y in enemy_list:
#     print(get_move_cnt(x, y, e_x, e_y), end=' ')




