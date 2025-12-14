# 치즈
# https://www.acmicpc.net/problem/2638

import sys
from collections import deque

inputf = sys.stdin.readline

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def mark_outside_air(grid, N, M):
    """BFS로 외부 공기 영역을 찾아 표시"""
    outside = [[False] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    queue = deque()

    # 가장자리의 모든 공기 영역에서 BFS 시작
    # 첫 번째 행과 마지막 행
    for j in range(M):
        if grid[0][j] == 0 and not visited[0][j]:
            queue.append((0, j))
            visited[0][j] = True
            outside[0][j] = True
        if grid[N - 1][j] == 0 and not visited[N - 1][j]:
            queue.append((N - 1, j))
            visited[N - 1][j] = True
            outside[N - 1][j] = True

    # 첫 번째 열과 마지막 열
    for i in range(N):
        if grid[i][0] == 0 and not visited[i][0]:
            queue.append((i, 0))
            visited[i][0] = True
            outside[i][0] = True
        if grid[i][M - 1] == 0 and not visited[i][M - 1]:
            queue.append((i, M - 1))
            visited[i][M - 1] = True
            outside[i][M - 1] = True

    # BFS로 외부 공기와 연결된 모든 공기 찾기
    while queue:
        x, y = queue.popleft()

        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                visited[nx][ny] = True  # 방문 처리
                if grid[nx][ny] == 0:  # 공기인 경우
                    outside[nx][ny] = True  # 외부 공기 영역 표시
                    queue.append((nx, ny))

    return outside


def find_melting_cheese(grid, outside, N, M):
    """2변 이상 외부 공기와 접촉한 치즈 찾기"""
    melting = []

    for i in range(N):
        for j in range(M):
            if grid[i][j] == 1:  # 치즈인 경우
                contact_count = 0

                # 동서남북 췤
                for dx, dy in DIRECTIONS:
                    ni, nj = i + dx, j + dy

                    # 외부 공기와 닿는 면 확인 후 카운트
                    if 0 <= ni < N and 0 <= nj < M and outside[ni][nj]:
                        contact_count += 1

                # 2변 이상 외부 공기와 접촉하면 녹아내려유
                if contact_count >= 2:
                    melting.append((i, j))

    return melting


def main():
    N, M = map(int, inputf().split())
    grid = [list(map(int, inputf().split())) for _ in range(N)]

    time = 0

    while True:
        # 1. 외부 공기 영역 찾기
        outside = mark_outside_air(grid, N, M)

        # 2. 녹을 치즈 찾기
        melting_cheese = find_melting_cheese(grid, outside, N, M)

        # 3. 더 이상 녹을 치즈가 없으면 종료
        if not melting_cheese:
            break

        # 4. 치즈 녹이기
        for x, y in melting_cheese:
            grid[x][y] = 0

        # 5. 시간 증가
        time += 1

    print(time)
    return


if __name__ == "__main__":
    main()
