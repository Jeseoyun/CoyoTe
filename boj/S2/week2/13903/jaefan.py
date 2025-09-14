# 출근 
# https://www.acmicpc.net/problem/13903

# 이따구로 출근할거면 재택되는 회사를 다녀라 준규야

import sys
from collections import deque

inputf = sys.stdin.readline

# 1. 세로 블록만 밟는다. (시작은 첫 번째 row의 세로 블록 중 아무 곳에서나 가능하다.)
# 2. 특정 규칙(예를 들어 상하좌우, 체스의 나이트 이동 규칙 등)으로 이동한다.
# 3. 첫 번째 row에서 출발하여 마지막 row에 도착하면 출근에 성공한 것이다.
# 4. 마지막으로 준규는 걷는 것이 매우 귀찮아서 최소한의 걸음으로 출근을 하고 싶다.

def main():
    R, C = map(int, inputf().split())
    arr = [list(map(int, inputf().split())) for _ in range(R)]  # 가로 0, 세로 1
    
    N = int(inputf())  # 규칙의 개수 
    directions = list(list(map(int, inputf().split())) for _ in range(N))

    # BFS - 모든 시작점을 한 번에 처리
    queue = deque()
    visited = [[-1] * C for _ in range(R)]
    
    # 첫 번째 row의 모든 세로 블록을 시작점으로 추가
    for y in range(C):
        if arr[0][y] == 1:
            queue.append((0, y))
            visited[0][y] = 0
    
    while queue:
        r, c = queue.popleft()
        
        # 마지막 row에 도달했으면 즉시 종료 (BFS이므로 최소값)
        if r == R - 1:
            print(visited[r][c])
            return
            
        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < R and 0 <= nc < C and visited[nr][nc] == -1 and arr[nr][nc] == 1:
                queue.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1

    # 마지막 row에 도달할 수 없는 경우
    print(-1)
    

if __name__ == "__main__":
    main()