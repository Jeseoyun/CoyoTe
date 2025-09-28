'''
일단 bfs로 4개가 되는지 확인하고 4개가 되면 그 인접한 위치 다 0으로 만들어놓기
그리고 0으로 되었다는건 연쇄를 했다는 뜻이고
연쇄를 한 이후에 아래로 줄 내리는데
이건 열단위로 보고 0이 있는 가장 작은 행(맨 위 인거지) 바로 위가 .이면 다 .으로 채우기
그렇게 계속 반복하면 될 것 같은데...
이건 bfs가 아닌 것 같기도하고...단타로 보면 또 bfs인 것 같기도하고...
'''
from collections import deque
def bfs_inga(): #응 아니야
    global ans
    cnt = 0
    visited = list([0 for _ in range(c)] for _ in range(r))

    queue = deque()
    color_crash = deque()
    for i in range(r):
        for j in range(c):
            if arr[i][j] != '.': #visited[i][j] == 0 추가하면 더 효율적이라고 생각했는데 시간 똑같음
                queue.append((i,j,arr[i][j]))
                color_crash.append((i,j))
                visited[i][j] = 1

            while queue:
                cx,cy,color = queue.popleft()
                for m in dxy:
                    nx,ny = cx+m[0],cy+m[1]

                    if 0<=nx<r and 0<=ny<c and arr[nx][ny] == color and visited[nx][ny] == 0:
                        queue.append((nx,ny,color))
                        color_crash.append((nx,ny))
                        visited[nx][ny] = 1
            
            if len(color_crash) >= 4: # 터트리기
                cnt += 1
                while color_crash:
                    x,y = color_crash.popleft()
                    arr[x][y] = '.'
            else:
                color_crash.clear()

    if cnt == 0:
        return
    else: # 아래로 내리기
        for j in range(c):
            gravity = [arr[i][j] for i in range(r) if arr[i][j] != '.']
            len_g = len(gravity)
            
            if len_g > 0:
                for i in range(r-len_g):
                    arr[i][j] = '.'
                for i in range(r-len_g,r):
                    arr[i][j] = gravity[0]
                    del gravity[0]
        ans += 1
        bfs_inga() #재귀..


r = 12
c = 6

arr = list(list(input()) for _ in range(r))
           
ans = 0

dxy = [[-1,0],[1,0],[0,1],[0,-1]]

bfs_inga()
print(ans)
