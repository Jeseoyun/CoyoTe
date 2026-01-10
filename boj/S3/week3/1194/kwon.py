# BOJ 1194 - 달이 차오른다, 가자
# 빈 칸(.): 언제나 이동 가능
# 벽(#): 이동 불가
# 열쇠(a-f): 이동 가능, 해당 열쇠 획득
# 문(A-F): 대응하는 열쇠가 있을 때만 이동 가능
# 시작(0): 민식이 현재 위치
# 출구(1): 도착지점

from collections import deque

N, M = map(int, input().split())
grid = [input() for _ in range(N)]

# 시작점 찾기
start = next((x, y) for x in range(N) for y in range(M) if grid[x][y] == "0")

dxy = ((1, 0), (0, 1), (-1, 0), (0, -1))

# BFS: (x, y, 보유한 열쇠 비트마스크)
q = deque([(*start, 0, 0)])  # x, y, keys, steps
visited = {(*start, 0)}

while q:
    x, y, keys, steps = q.popleft()

    for dx, dy in dxy:
        nx, ny = x + dx, y + dy

        if not (0 <= nx < N and 0 <= ny < M):
            continue

        cell = grid[nx][ny]

        # 벽은 통과 불가
        if cell == "#":
            continue

        # 문: 해당 열쇠가 없으면 통과 불가
        if "A" <= cell <= "F":
            door_bit = 1 << (ord(cell) - ord("A"))
            if not (keys & door_bit):
                continue

        # 출구 도달 시 종료
        if cell == "1":
            print(steps + 1)
            exit()

        # 열쇠 획득 처리
        new_keys = keys
        if "a" <= cell <= "f":
            new_keys = keys | (1 << (ord(cell) - ord("a")))

        # 방문 체크 (같은 위치 + 같은 열쇠 조합이면 스킵)
        if (nx, ny, new_keys) in visited:
            continue

        visited.add((nx, ny, new_keys))
        q.append((nx, ny, new_keys, steps + 1))

print(-1)
