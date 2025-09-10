# 최소니까 bfs
# 그냥 다 돌아
from collections import deque
def bfs():
    global ans
    queue = deque()
    
    for i in range(c):
        if arr[0][i] == 1:
            queue.append([0,i])
            cnt[0][i] = 0

    while queue:
        x, y = queue.popleft()
        if x == r-1: # 이 코드가 없어도 돌아가긴한다,,,
            continue
            
        for m in move:
            nx, ny = x+m[0],y+m[1]

            if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] == 1 and cnt[nx][ny] == -1:
                queue.append((nx,ny))
                cnt[nx][ny] = cnt[x][y] + 1


r, c = map(int, input().split())
arr = list(list(map(int, input().split())) for _ in range(r))
cnt = list([-1] * c for _ in range(r)) # 이동 거리


n = int(input())
move = list(list(map(int, input().split())) for _ in range(n))

bfs()


ans = float('inf')
for num in cnt[-1]:
    if num < ans and num != -1:
        ans = num
if ans == float('inf'):
    ans = -1

# ans = min([d for d in cnt[-1] if d != -1], default=-1)
# 한 줄로 대체 가능..^-^;

print(ans)
