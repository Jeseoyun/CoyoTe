from collections import deque, defaultdict

N = int(input())
r1, c1, r2, c2 = map(int, input().split())

dxy = ((-2, -1),
        (-2, 1),
        (0, -2),
        (0, 2),
        (2, -1),
        (2, 1))

q = deque([(r1, c1)])
visited = defaultdict(int)

result = -1
while q:
    x, y = q.popleft()

    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if not(0 <= nx < N and 0 <= ny < N):
            continue

        if visited[(nx, ny)] or (nx == r1 and ny == c1):
            continue
        
        if (nx, ny) == (r2, c2):
            result = visited[(x, y)] + 1
            break

        q.append((nx, ny))
        visited[(nx, ny)] = visited[(x, y)] + 1

    else:
        continue
    break
# print(visited)
# print(q)
print(result)