from math import sqrt, floor
from collections import deque

def bfs():
    queue = deque()

    visited = [False] * n
    dist = [-1] * n
    
    for twr in last_tower:
        queue.append(twr)
        visited[twr] = True
        dist[twr] = 0
    
    while queue:
        cur = queue.popleft()
        cx, cy = top[cur]

        for next in range(n):
            if not visited[next]:
                nx, ny = top[next]
                if sqrt((cx - nx) ** 2 + (cy - ny) ** 2) <= r:
                    visited[next] = True
                    dist[next] = dist[cur] + 1
                    queue.append(next)
    
    total = 0
    for i in range(n):
        if dist[i] != -1:
            total += d * (0.5 ** dist[i])
    
    return total

n,r,d,x,y = map(int, input().split())
top = [list(map(int, input().split())) for _ in range(n)]


last_tower = []
for i in range(n):
    if sqrt((x - top[i][0])**2 + (y - top[i][1])**2) <= r:
        last_tower.append(i)


if not last_tower:
    print(0)
else:
    print(round(bfs(), 3))
