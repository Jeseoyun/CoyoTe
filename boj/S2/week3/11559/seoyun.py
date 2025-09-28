from collections import deque


N, M = 12, 6
dxy = [(1, 0), (-1, 0), (0, -1), (1, 0)]


def bfs(board, sx, sy):
    queue = deque([(sx, sy, board[sx][sy])])
    visited = set()
    visited.add((sx,sy))

    while queue:
        x, y, color = queue.popleft()

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if (nx, ny) in visited:
                continue

            if board[nx][ny] != color:
                continue

            queue.append((nx, ny, color))
            visited.add((nx, ny))

    if len(visited) >= 4:
        return visited
    else:
        return None


def rearrange(board, bombed_pos):
    for x, y in bombed_pos:
        board[x][y] = 0

    for j in range(M):
        # 1. 0 빼고 행 추출
        column = [board[i][j] for i in range(N) if board[i][j]]

        # 2. 빠진놈들 개수만큼 앞에 . 으로 채워넣기
        while len(column) != N:
            column.insert(0, ".")

        # 3. 다시 복귀시키기
        for i in range(N):
            board[i][j] = column[i]


def main():
    puyo = [list(input()) for _ in range(N)]
    combo = 0

    while True:
        # 1. 4개 이상 연결된 뿌요들 좌표 찾기
        bombed_pos = set()
        for i in range(N):
            for j in range(M):
                if puyo[i][j] == ".":
                    continue

                if (i, j) in bombed_pos:
                    continue

                connected = bfs(puyo, i, j)

                if connected:
                    for x, y in connected:
                        bombed_pos.add((x, y))
        # print(bombed_pos)

        if not bombed_pos:
            break
        else:
            combo += 1

        # 2. 터진 뿌요들 없애고 아래로 떨어뜨리기
        rearrange(puyo, bombed_pos)
        # print(puyo)

    print(combo)


if __name__ == "__main__":
    main()