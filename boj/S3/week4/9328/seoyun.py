from collections import deque, defaultdict

dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]


# def is_enter(cell, keys):
#     if cell == "*": return False
#     if cell == ".": return True
#     if cell == "$": return True
#     if cell.islower():  return True
#     if cell.isupper(): return cell.lower() in keys
#
#     return False


def find_enterance(grid, keys, h, w):
    enterance = []

    for i in range(w):
        # 윗줄
        # if is_enter(grid[0][i], keys):
        enterance.append((0, i))
        # 아랫줄
        # if is_enter(grid[h-1][i], keys):
        enterance.append((h-1, i))

    for j in range(1, h-1):
        # 왼쪽
        # if is_enter(grid[j][0], keys):
        enterance.append((j, 0))
        # 오른쪽
        # if is_enter(grid[j][w-1], keys):
        enterance.append((j, w-1))

    return enterance


def find_docs(grid, keys, h, w, enterance):
    visited = [[False]*w for _ in range(h)]
    queue = deque()
    docs = 0

    wait = defaultdict(list)  # 열쇠 없어서 대기중인 경로

    # 1. 입구들 큐에 넣기
    for sx, sy in enterance:
        if visited[sx][sy]:
            continue

        if grid[sx][sy] == "*":
            continue

        # 잠긴 문이면 wait에만 등록하고 큐엔 안 넣음
        if grid[sx][sy].isupper() and (grid[sx][sy].lower() not in keys):
            wait[grid[sx][sy].lower()].append((sx, sy))
            continue

        visited[sx][sy] = True
        queue.append((sx, sy))

        # 입구 자체가 문서/열쇠일 경우
        if grid[sx][sy] == "$":
            docs += 1
            grid[sx][sy] = "."
        elif grid[sx][sy].islower():
            keys.add(grid[sx][sy])

            # 입구에서 대기중인 애들 열어주기
            for kx, ky in wait[grid[sx][sy]]:
                if not visited[kx][ky]:
                    visited[kx][ky] = True
                    queue.append((kx, ky))
            grid[sx][sy] = "."

    # 2. 탐색
    while queue:
        x, y = queue.popleft()

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            if visited[nx][ny]:
                continue
            if grid[nx][ny] == "*":
                continue

            # 문인데 키 없음 -> 대기
            if grid[nx][ny].isupper() and (grid[nx][ny].lower() not in keys):
                wait[grid[nx][ny].lower()].append((nx, ny))
                continue

            # 문서 획득
            if grid[nx][ny] == "$":
                docs += 1
                grid[nx][ny] = "."

            # 열쇠 획득
            if grid[nx][ny].islower():
                keys.add(grid[nx][ny])

                # 키로 문 열어서 경로 추가
                for kx, ky in wait[grid[nx][ny]]:
                    if visited[kx][ky]:
                        continue
                    visited[kx][ky] = True
                    queue.append((kx, ky))

                grid[nx][ny] = "."

            visited[nx][ny] = True
            queue.append((nx, ny))

    return docs


def main():
    T = int(input())

    for _ in range(T):
        h, w = map(int, input().split())
        grid = [list(input()) for _ in range(h)]
        # keys = set(input())
        k = input()
        keys = set() if k == "0" else set(k)

        # 1. 입구 찾기
        enter = find_enterance(grid, keys, h, w)
        # print(enter)

        # 2. 입구로부터 탐색
        docs = find_docs(grid, keys, h, w, enter)
        print(docs)


if __name__ == "__main__":
    main()