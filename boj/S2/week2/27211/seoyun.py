from collections import deque


dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def bfs(board, visited, N, M, sx, sy):
    queue = deque([(sx, sy)])

    while queue:
        x, y = queue.popleft()

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            nx %= N
            ny %= M

            if board[nx][ny]:
                continue

            if visited[nx][ny]:
                continue

            queue.append((nx, ny))
            visited[nx][ny] = 1


def main():
    N, M = map(int, input().split())
    planet = [list(map(int, input().split())) for _ in range(N)]

    visited = [[0]*M for _ in range(N)]
    area_cnt = 0
    for i in range(N):
        for j in range(M):
            if planet[i][j]:
                continue
            if visited[i][j]:
                continue
            bfs(planet, visited, N, M, i, j)
            area_cnt += 1

    print(area_cnt)


if __name__ == "__main__":
    main()