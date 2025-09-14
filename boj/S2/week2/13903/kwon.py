from collections import deque

R, C = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(R)]

N = int(input())
dxy = [list(map(int, input().split())) for _ in range(N)]

# visited array to track visited cells
visited = [[False] * C for _ in range(R)]

q = deque()
for i, floor in enumerate(grid[0]):
    if floor == 1:
        q.append([0, i, 0])
        visited[0][i] = True

result = -1
while q:
    x, y, t = q.popleft()
    
    # Check if we reached the last row
    if x == R - 1:
        result = t
        break
    
    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if not(0 <= nx < R and 0 <= ny < C):
            continue
        if grid[nx][ny] == 0 or visited[nx][ny]:
            continue
        
        q.append([nx, ny, t + 1])
        visited[nx][ny] = True

print(result)