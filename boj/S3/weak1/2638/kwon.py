from collections import deque
from copy import deepcopy

dxy = ((0, 1), (0, -1), (1, 0), (-1, 0))


# 막힌 공간 체크
def check_blocked_space(x, y, matrix):
    new_matrix = deepcopy(matrix)
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < N and 0 <= ny < M):
                continue
            if new_matrix[nx][ny]:
                continue
            if nx == N - 1 or ny == M - 1:
                return matrix
            q.append((nx, ny))
            new_matrix[nx][ny] = 2
    return new_matrix


# 녹이기
def melt_cheese(matrix):
    q = deque([(0, 0)])
    visited = set([(0, 0)])
    while q:
        x, y = q.popleft()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < N and 0 <= ny < M):
                continue
            if (nx, ny) in visited:
                continue
            if matrix[nx][ny] != 0:
                matrix[nx][ny] += 1
                continue
            visited.add((nx, ny))
            q.append((nx, ny))

    for i in range(N):
        for j in range(M):
            if matrix[i][j] > 2:
                matrix[i][j] = 0
            elif matrix[i][j] == 2:
                matrix[i][j] = 1


def restore_matrix(matrix):
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 2:
                matrix[i][j] = 0


N, M = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]

time = 0
while True:
    matrix = check_blocked_space(0, 0, matrix)
    # print(f"time: {time}")
    # print(*matrix, sep="\n")
    # print()
    melt_cheese(matrix)
    # print(*matrix, sep="\n")
    # print()
    restore_matrix(matrix)
    time += 1
    if sum(sum(matrix, [])) == 0:
        break

print(time)
