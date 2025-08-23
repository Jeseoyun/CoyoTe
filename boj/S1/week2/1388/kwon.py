from collections import deque

N, M = map(int, input().split())

floor = [list(input()) for _ in range(N)]

def search_tiles(start, visited, tile_shape):
    # 타일 모양에 따라 탐색 방향 설정
    if tile_shape == '-':
        dy, dx = 0, 1
    else:
        dy, dx = 1, 0

    q = deque([start])
    while q:
        y, x = q.popleft()

        ny, nx = y + dy, x + dx

        # 범위 벗어났을 경우
        if not (0 <= ny < N) or not (0 <= nx < M):
            return 1
        # 이미 방문했을 경우
        if visited[ny][nx]:
            return 1
        # 타일 모양이 다를 경우
        if floor[ny][nx] != tile_shape:
            return 1

        q.append((ny, nx))
        visited[ny][nx] = True

visited = [[False] * M for _ in range(N)]
tile_cnt = 0

for y in range(N):
    for x in range(M):
        if visited[y][x]:
            continue
        tile_cnt += search_tiles((y, x), visited, floor[y][x])

print(tile_cnt)






# 그냥 for 문 돌려버리는게 더 빠를듯