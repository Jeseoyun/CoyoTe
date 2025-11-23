# 데스 나이트 
# https://www.acmicpc.net/problem/16948


"""
fyi. while-else
    Python의 while-else 구문은 다음과 같이 동작한다. 
    else 블록이 실행되는 경우: while 루프가 정상적으로 종료되면 (조건이 False가 되어 종료) else 블록이 실행된다.
    else 블록이 실행되지 않는 경우: while 루프가 break, return 등으로 중간에 빠져나가면 else 블록은 실행되지 않는다.
"""

import sys
from collections import deque

inputf = sys.stdin.readline
# 데스 나이트가 있는 곳이 (r, c)라면, (r-2, c-1), (r-2, c+1), (r, c-2), (r, c+2), (r+2, c-1), (r+2, c+1)로 이동할 수 있다.
DIRECTIONS = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]

def main():
    N = int(inputf())
    # r1, c1 에서 r2, c2 로 이동하는 최소 이동 횟수를 구한다. => BFS 
    r1, c1, r2, c2 = map(int, inputf().split())
    visited = [[-1] * N for _ in range(N)]

    queue = deque([(r1, c1)]) # 첫 좌표부터 시작 
    visited[r1][c1] = 0  # 첫 좌표는 0번 이동 
    while queue:
        x, y = queue.popleft()
        if x == r2 and y == c2:  # 목표 좌표에 도달했다면 종료 
            print(visited[x][y])
            return
        for dx, dy in DIRECTIONS:  # 데스 나이트의 이동 가능한 방향 확인 
            nx, ny = x + dx, y + dy  # 이동 후 좌표 
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1:  # 유효성 검사 및 방문 여부 체크 
                visited[nx][ny] = visited[x][y] + 1  # 이동 횟수 업데이트 
                queue.append((nx, ny))  # 큐에 추가 
    # 목표 좌표에 도달하지 못했다면 -1 출력 
    else: 
        print(-1)

if __name__ == "__main__":
    main()
    return 