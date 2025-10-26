from collections import deque

N, M = map(int, input().split())
grid = [list(input().strip()) for _ in range(M)]
visited = set()

dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(x, y, team):
    q = deque([(x, y)])
    visited.add((x, y))
    count = 1
    
    while q:
        x, y = q.popleft()
        
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            
            if not(0 <= nx < M and 0 <= ny < N):
                continue
            if (nx, ny) in visited:
                continue
            if grid[nx][ny] != team:
                continue
            visited.add((nx, ny))
            q.append((nx, ny))
            count += 1
    return count

white_power = 0
blue_power = 0

for i in range(M):
    for j in range(N):
        if (i, j) in visited:
            continue
        team = grid[i][j]
        count = bfs(i, j, team)
        if team == 'W':
            white_power += count ** 2
        else:
            blue_power += count ** 2

print(white_power, blue_power)