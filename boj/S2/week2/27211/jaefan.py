# 도넛행성
# https://www.acmicpc.net/problem/27211

import sys 
from collections import deque

inputf = sys.stdin.readline

def main():
    N, M = map(int, inputf().split())
    doughnut_planet = [list(map(int, inputf().split())) for _ in range(N)]

    visited = [[False] * M for _ in range(N)]

    queue = deque()

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    # doughnut_planet 이 0인 곳 찾기 
    for i in range(N):
        for j in range(M):
            if doughnut_planet[i][j] == 0:
                queue.append((i, j))

    # print(queue)
    
    area_cnt = 0    
    while queue:
        x, y = queue.popleft()
        if visited[x][y]:
            continue
        visited[x][y] = True
        tmp_queue = deque([(x, y)])
        while tmp_queue:
            x, y = tmp_queue.popleft()
            # print(x, y)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                # 행성은 연속되어 있음
                if nx < 0 : nx = N - 1
                if nx >= N : nx = 0
                if ny < 0 : ny = M - 1
                if ny >= M : ny = 0

                if not visited[nx][ny] and doughnut_planet[nx][ny] == 0:
                    tmp_queue.append((nx, ny))
                    visited[nx][ny] = True

        area_cnt += 1  # 영역 개수 증가 

    print(area_cnt)

    

if __name__ == "__main__":
    main()
