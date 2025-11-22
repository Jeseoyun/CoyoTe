from collections import deque

def bfs():
    queue = deque()

    queue.append([r1,c1,0])
    while queue:
        x,y,cnt = queue.popleft()

        if x == r2 and y == c2:
            return cnt


        for mov in dxy:
            nx,ny = x+mov[0],y+mov[1]

            if 0<=nx<n and 0<=ny<n and visited[nx][ny] == False:
                visited[nx][ny] = True
                queue.append((nx,ny,cnt+1))
        



n = int(input())

r1,c1,r2,c2 = map(int, input().split())

visited = [[False]*n for _ in range(n)]
visited[r1][c1] = True

dxy = [[-2,-1],[-2,1],[0,-2],[0,2],[2,-1],[2,1]]

ans = bfs()

if ans == None:
    print(-1)
else:
    print(ans)