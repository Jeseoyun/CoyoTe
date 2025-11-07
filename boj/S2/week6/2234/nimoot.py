from collections import deque

def bfs(x, y, num):
    queue = deque([(x, y)])
    visited[x][y] = num
    size = 1
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx, ny = cx + dxy[i][0], cy + dxy[i][0]

            if arr[cx][cy] & wall[i]:
                continue

            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                visited[nx][ny] = num
                queue.append((nx, ny))
                size += 1
    return size

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]

dxy = [[-1,0],[1,0],[0,1],[0,-1]]
wall = [1, 2, 4, 8]

visited = [[0]*n for _ in range(m)]
room_size = []
room_num = 0


# 방 나누기
for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            room_num += 1
            room_size.append(bfs(i, j, room_num))
            print(i,j,room_num,room_size)

after_wall = 0

# 벽 제거
for i in range(m):
    for j in range(n):
        for mov in dxy:
            nx, ny = i + mov[0], j + mov[1]
            if 0 <= nx < m and 0 <= ny < n:
                if visited[i][j] != visited[nx][ny]:
                    after_wall = max(after_wall, room_size[visited[i][j]-1] + room_size[visited[nx][ny]-1])


print(room_num)
print(max(room_size))         
print(after_wall)
