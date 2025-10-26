from collections import deque

dxy = [[0,1],[0,-1],[1,0],[-1,0]]

def bfs(x,y,cnt,color):
    queue = deque()
    queue.append((x,y))
    arr[x][y] = '.'
    
    while queue:
        x, y = queue.popleft()

        for mov in dxy:
            nx,ny = x+mov[0],y+mov[1]

            if 0<=nx<n and 0<=ny<m and arr[nx][ny] == color:
                arr[nx][ny] = '.'
                queue.append((nx,ny))
                cnt += 1

    if color == 'W':
        home.append(cnt*cnt)
    else:
        away.append(cnt*cnt)
                    


m, n = map(int, input().split())
arr = [list(input()) for _ in range(n)]


home = []
away = []


for i in range(n):
    for j in range(m):
        if arr[i][j] != '.':
            bfs(i,j,1,arr[i][j])

print(sum(home),sum(away))

