import heapq

dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def main():
    N, M = map(int, input().split())
    heights = [list(map(int, input().split())) for _ in range(N)]

    sx, sy = 0, 0
    heap = [(-heights[sx][sy], sx, sy)]

    visited = [[0]*M for _ in range(N)]
    visited[sx][sy] = 1

    while heap:
        h, x, y = heapq.heappop(heap)

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if heights[nx][ny] >= heights[x][y]:
                continue

            if visited[nx][ny] == 0:
                heapq.heappush(heap, (-heights[nx][ny], nx, ny))

            visited[nx][ny] += visited[x][y]

    print(visited[N-1][M-1])


if __name__ == "__main__":
    main()