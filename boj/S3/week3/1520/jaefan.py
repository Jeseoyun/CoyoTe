# https://www.acmicpc.net/problem/1520
# 내리막 길 


"""
'등산로' in SWEA 

- 가능한 모든 경로를 구해야 함. -> DFS .. 
- 높은 곳에서 낮은 곳으로만 이동해야 함.
- (0,0) -> (N-1, M-1) 로 이동 
- 상하좌우 4방향 이동 가능 

- 현재 위치에서 목적지 까지 가는 경로의 수를 저장한다. -> dp[r][c] 
- DFS 로 반환하면서 dp[r][c] 에 경로의 수를 저장.
"""

import sys 
sys.setrecursionlimit(250000)  # 재귀 길이 제한.
inputf = sys.stdin.readline

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def main():
    N, M = map(int, inputf().split())
    grid = list()
    for _ in range(N):
        grid.append(list(map(int, inputf().split())))
        
    ways = [[-1] * M for _ in range(N)]
    
    
    def dfs(r, c):
        
        # 목적지 도달 
        if r == N-1 and c == M-1:
            return 1
        
        # 이미 계산한 경우 -> 바로 반환. 
        if ways[r][c] != -1:
            return ways[r][c]
        
        ways[r][c] = 0
        
        # 4방향 탐색 후 이동
        for dr, dc in DIRECTIONS:
            nr, nc = r + dr, c + dc
            # 유효성 검사 
            if 0 <= nr < N and 0 <= nc < M and grid[nr][nc] < grid[r][c]:
                # 경로의 수 업데이트 
                ways[r][c] += dfs(nr, nc)
        
        # 경로의 수 반환
        return ways[r][c]
    
    total_ways = dfs(0, 0)
    print(total_ways)
    return 


if __name__ == "__main__":
    main()