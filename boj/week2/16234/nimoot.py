from collections import deque

dxy = [[-1, 0], [1, 0], [0, 1], [0, -1]]


def bfs():
    global total
    visited = [[False] * n for _ in range(n)] # 방문 여부
    is_moved = False # 인구 이동 진행 여부
    
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                queue = deque([(i, j)])
                groups = [(i, j)]
                visited[i][j] = True
                hap = arr[i][j] # 연합의 인구 수
                
                while queue:
                    x, y = queue.popleft()
                    
                    for dx, dy in dxy:
                        nx, ny = x + dx, y + dy
                        
                        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and l <= abs(arr[x][y] - arr[nx][ny]) <= r:
                            queue.append((nx, ny))
                            groups.append((nx, ny))
                            visited[nx][ny] = True
                            hap += arr[nx][ny]
            
                if len(groups) > 1:
                    is_moved = True
                    hap //= len(groups)
                    for x, y in groups: # 새로운 인구 수 저장
                        arr[x][y] = hap

    if is_moved: # 인구 이동 진행했으면 일수 +1
        total += 1
    else: # 인구 이동 안했으면 일수 출력하고 종료
        print(total)
        exit()

n, l, r = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

total = 0

while True: # bfs 무한 반복
    bfs()