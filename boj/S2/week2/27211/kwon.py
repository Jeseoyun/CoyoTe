from collections import deque

N, M = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(N)]

dxy = ((0, 1), (0, -1), (1, 0), (-1, 0))


def bfs(x, y):
    q = deque([(x, y)])

    while q:
        x, y = q.popleft()

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            nx %= N
            ny %= M

            if grid[nx][ny] == 1:
                continue

            grid[nx][ny] = 1
            q.append((nx, ny))

    return 1


result = 0

for x in range(N):
    for y in range(M):
        if grid[x][y] == 1:
            continue

        result += bfs(x, y)

print(result)
