# 처음에 나이트를 이동하면 위치가 바뀐다고 착각해서 개고생함

from collections import deque


dxy = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]


def bfs(N, sx, sy):
    dist = [[-1]*N for _ in range(N)]
    dist[sx][sy] = 0

    queue = deque([(sx, sy)])
    while queue:
        x, y = queue.popleft()

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            if dist[nx][ny] != -1:
                continue

            dist[nx][ny] = dist[x][y] + 1
            queue.append((nx, ny))

    return dist


def main():
    N, M = map(int, input().split())

    kx, ky = map(int, input().split())  # knight 위치
    kx, ky = kx - 1, ky - 1  # (0, 0) ~ (N-1, N-1)로 좌표축 이동

    enemy_pos = []
    for _ in range(M):
        ex, ey = map(int, input().split())
        enemy_pos.append((ex-1, ey-1))  # 좌표축 이동

    moved = []  # 상대 말을 몇 번 움직여서 잡았는지 저장
    dist = bfs(N, kx, ky)

    for ex, ey in enemy_pos:
        moved.append(dist[ex][ey])

    print(*moved)


if __name__ == "__main__":
    main()