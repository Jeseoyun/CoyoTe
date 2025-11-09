# 숫자판 점프 
# https://www.acmicpc.net/problem/2210


import sys 
inputf = sys.stdin.readline

N = 5 
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

"""
인접해 있는 4 방향으로 5번 이동하면서 6자리 숫자를 만든다. 
재방문도 가능하며, 0으로 시작하는 숫자도 만들 수 있다. (문자열로 관리해야함)
숫자판이 주어질 때, 만들 수 있는 서로 다른 6자리 숫자의 개수를 출력한다.
-> DFS ?
"""


def main():
    
    grid = []
    for _ in range(N):
        grid.append(list(map(int, inputf().split())))
    
    # 중복 방지를 위한 set
    result_set = set()
    
    def dfs(r, c, num_str, depth):
        # 깊이 6에 도달하면 더 이상 탐색하지 않음
        if depth == 6:
            result_set.add(num_str)
            return  
        
        # 4 방향으로 이동하면서 숫자를 만든다.
        for dr, dc in DIRECTIONS:
            nr, nc = r + dr, c + dc
            # 유효성 검사 
            if 0 <= nr < N and 0 <= nc < N:
                # 숫자를 만들고 다음 깊이로 이동
                dfs(nr, nc, num_str + str(grid[nr][nc]), depth + 1)

    # 모든 시작점에서 탐색 시작
    for i in range(N):
        for j in range(N):
            dfs(i, j, str(grid[i][j]), 1)

    # 결과 출력
    print(len(result_set))

if __name__ == "__main__":
    main()