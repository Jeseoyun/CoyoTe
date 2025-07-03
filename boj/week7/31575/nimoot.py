from collections import deque

dxy = [[1,0],[0,1]]

def bfs():
    global n,m
    queue = deque()
    queue.append([0,0])
    visited = set()
    visited.add((0,0))
    while queue:
        cx,cy = queue.popleft()

        if cx == m-1 and cy == n-1:
            print("Yes")
            exit()

        for new in dxy:
            nx,ny = cx+new[0],cy+new[1]

            if 0<=nx<m and 0<=ny<n and arr[nx][ny] == 1 and (nx,ny) not in visited:
                queue.append((nx,ny))
                visited.add((nx,ny))

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(m)]

bfs()

print("No")g