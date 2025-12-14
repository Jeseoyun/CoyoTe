from collections import deque


dxy = [(-1, 0), (0, 1), (0, -1), (1, 0)]


def print_board(board):
    for arr in board:
        for elem in arr:
            print(elem, end=" ")
        print()
    print()


def find_start_pos(grid, N, M):
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 0:
               return i, j
    return 0, 0


def check_boundary(grid, N, M):
    sx, sy = find_start_pos(grid, N, M)
    queue = deque([(sx, sy)])
    visited = [[False]*M for _ in range(N)]
    visited[sx][sy] = True

    while queue:
        x, y = queue.popleft()

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if visited[nx][ny]:
                continue

            if grid[x][y] == 0 and grid[nx][ny] == 1:
                grid[x][y] = '-'

            if grid[nx][ny] == 1:
                continue

            queue.append((nx, ny))
            visited[nx][ny] = True


def find_melting_cheeze(grid, N, M):
    cheeze = []
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1:
                cheeze.append((i, j))

    melting_cheeze = []
    for x, y in cheeze:
        contact_side = 0
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if grid[nx][ny] == "-":
                contact_side += 1

        if contact_side >= 2:
            melting_cheeze.append((x, y))

    return melting_cheeze


def main():
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    melting_time = 0
    while True:
        # 1. 치즈 경계 찾기 (바깥 놈들 다 -로 바꾸기)
        check_boundary(grid, N, M)
        # print_board(grid)

        # 2. -와 2개 이상 인접해있는 놈들 찾기
        melting_pos = find_melting_cheeze(grid, N, M)

        if not melting_pos:
            break

        # 3. 삭제
        for x, y in melting_pos:
            grid[x][y] = 0

        melting_time += 1

    print(melting_time)


if __name__ == "__main__":
    main()