# 현명한 나이트 
# https://www.acmicpc.net/problem/18404

import sys
from collections import deque

inputf = sys.stdin.readline

DIRECTIONS = [[-2, -1], [-2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2], [2, -1], [2, 1]]


def oneindex2zeroindex(x):
    return int(x) - 1

def is_valid(x, y, N):
    if 0 <= x < N and 0 <= y < N:
        return True
    return False

def calculate_grid(x, y, N):

    grid = [[0 for _ in range(N)] for _ in range(N)]

    que = deque([(x, y)])

    while que:
        cx, cy = que.popleft()
        for dx, dy in DIRECTIONS:
            nx, ny = cx + dx, cy + dy 
            if is_valid(nx, ny, N) and not grid[nx][ny]:
                grid[nx][ny] = grid[cx][cy] + 1
                que.append((nx, ny))
    
    return grid 


def main():

    N, M = map(int, inputf().rstrip().split())  # N: 체스판 크기 (N x N), M: 상대편 말의 수

    X, Y = map(oneindex2zeroindex, inputf().rstrip().split())  # 나이트의 위치 (1-indexed) 

    # Solution 01 (모든 상대 말에 대해서 BFS)
    # # enemies = deque([list(map(oneindex2zeroindex, inputf().rstrip().split())) for _ in range(M)])  # 상대편 말의 위치 (1-indexed)

    # # while enemies:
    # for _ in range(M):

    #     # enemy_x, enemy_y = enemies.popleft()
    #     enemy_x, enemy_y = map(oneindex2zeroindex, inputf().rstrip().split())
    #     visited = [[False for _ in range(N)] for _ in range(N)]
    #     qu = deque([(X, Y, 0)])
    #     visited[X][Y] = True 
    #     while qu:
    #         x, y, dist = qu.popleft()
    #         if (x, y) == (enemy_x, enemy_y):
    #             print(dist, end=' ')
    #             break
    #         for dx, dy in DIRECTIONS:
    #             nx, ny = x + dx, y + dy 
    #             if is_valid(nx, ny, N) and not visited[nx][ny]:
    #                 visited[nx][ny] = True 
    #                 qu.append((nx, ny, dist + 1))
    #             else:
    #                 continue


    # Solution 02 (이동 가능한 위치에 대해서 모두 계산 후 단순 반환)
    calculated_grid = calculate_grid(x=X, y=Y, N=N)

    enemies = deque([list(map(oneindex2zeroindex, inputf().rstrip().split())) for _ in range(M)])  # 상대편 말의 위치 (1-indexed)

    for enemy_x, enemy_y in enemies:
        print(calculated_grid[enemy_x][enemy_y], end=' ')

    return

if __name__=='__main__':
    main()
