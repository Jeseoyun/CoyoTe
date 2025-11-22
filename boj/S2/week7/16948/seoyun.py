from collections import deque


dxy = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]


def bfs(sx, sy, ex, ey, N, visited):
    queue = deque([(sx, sy, 0)])
    visited[sx][sy] = True

    while queue:
        x, y, mov_cnt = queue.popleft()

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            if visited[nx][ny]:
                continue

            if (nx, ny) == (ex, ey):
                return mov_cnt + 1

            visited[nx][ny] = True
            queue.append((nx, ny, mov_cnt+1))

    return -1


def main():
    N = int(input())
    r1, c1, r2, c2 = map(int, input().split())

    visited = [[False]*N for _ in range(N)]
    min_mov = bfs(r1, c1, r2, c2, N, visited)

    print(min_mov)


if __name__ == "__main__":
    main()