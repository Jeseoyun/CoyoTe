from collections import deque

dxy = [[-1,0],[0,1],[1,0],[0,-1]]

def bfs(cx,cy,cnt):
    queue = deque()
    queue.append((cx,cy))

    while queue:
        x, y = queue.popleft()
        
        for move in dxy:
            nx = (x+move[0]) % n
            ny = (y+move[1]) % m

            if arr[nx][ny] == 0:
                arr[nx][ny] = cnt
                queue.append((nx,ny))

    # print()
    # print(cx,cy)
    # for row in arr:
    #     print(*row)

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

ans = 2

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            bfs(i,j,ans)    
            ans += 1

print(ans-2)