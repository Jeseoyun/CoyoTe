from collections import deque

N, M = map(int, input().split())

space = [list(map(int, input().split())) for _ in range(M)]

dyx = ((1, 0), (0, 1))

q = deque([(0, 0)])
visited = set([(0, 0)])

is_possible = False

if N == 1 and M == 1:
    is_possible = True

while q:
    y, x = q.popleft()
    for dy, dx in dyx:
        ny, nx = y + dy, x + dx
        if not(0 <= ny < M and 0 <= nx < N):
            continue
        if space[ny][nx] == 0:
            continue
        if (ny, nx) in visited:
            continue
        if (ny, nx) == (M - 1, N - 1):
            is_possible = True
            break

        q.append((ny, nx))
        visited.add((ny, nx))
    else:
        continue
    break

# print(visited)
print('Yes' if is_possible else 'No')