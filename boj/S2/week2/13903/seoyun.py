from collections import deque


def bfs(board, R, C, dxy):
    queue = deque()
    visited = [[0]*C for _ in range(R)]

    # 시작 가능한 지점 모두 큐에 삽입
    for sy in range(C):
        if board[0][sy]:
            queue.append((0, sy, 0))
            visited[0][sy] = 1

    if not queue:
        return -1

    while queue:
        x, y, step = queue.popleft()

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            if nx < 0 or nx >= R or ny < 0 or ny >= C:
                continue

            if not board[nx][ny]:
                continue

            if visited[nx][ny]:
                continue

            if nx == R-1:
                return step+1

            queue.append((nx, ny, step+1))
            visited[nx][ny] = 1

    return -1


def main():
    R, C = map(int, input().split())
    blocks = [list(map(int, input().split())) for _ in range(R)]

    N = int(input())  # 규칙 수
    dxy = [tuple(map(int, input().split())) for _ in range(N)]

    step = bfs(blocks, R, C, dxy)
    print(step)


if __name__ == "__main__":
    main()