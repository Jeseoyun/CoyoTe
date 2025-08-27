from collections import deque

dxy = [[-1,0],[1,0],[0,1],[0,-1]]
def cal(number): #영역계산
    global ans 
    queue = deque()

    visited = set()
    pre = 0
    
    for i in range(n):
        for j in range(n):
            if arr[i][j] > number and (i,j) not in visited:
                queue.append([i,j])
                while queue:
                    cx,cy = queue.popleft()
                    for move in dxy:
                        nx, ny = cx+move[0],cy+move[1]

                        if 0<=nx<n and 0<=ny<n and arr[nx][ny] > number and (nx,ny) not in visited:
                            queue.append([nx,ny])
                            visited.add((nx,ny))    
                pre += 1
    # print(ans, pre)
    ans = max(ans,pre)



n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

nums = set()
for i in range(n):
    for j in range(n):
        nums.add(arr[i][j])
        
sort_nums = list(nums)
sort_nums.sort()
ans = 1

for i in sort_nums:
    cal(i)

print(ans)