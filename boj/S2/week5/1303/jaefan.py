# 전쟁 - 전투 
# https://www.acmicpc.net/problem/1303

import sys 
from collections import deque
inputf = sys.stdin.readline

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def find_group(war_field, N, M, src, team:str, visited:list):
    """src 에서 시작해서 team 과 같은 그룹을 찾는다. """
    queue = deque()
    queue.append(src)
    count = 0  # 그룹 내 병사 수
    visited[src[0]][src[1]] = True

    # BFS 탐색: 기본 BFS 탐색 방식으로 그룹을 찾는다. 
    while queue:
        x, y = queue.popleft()
        count += 1
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            # 기본 BFS 조건 + 현재 위치가 team 과 같은 그룹인지 검사한다. 
            if 0 <= nx < M and 0 <= ny < N and not visited[nx][ny] and war_field[nx][ny] == team:
                queue.append((nx, ny))
                visited[nx][ny] = True

    return count, visited

def get_team_power(war_field, N, M, team:str):
    """team 의 힘을 계산한다. """

    # 팀의 힘 
    power_of_team = 0

    # 방문 배열 
    visited = [[False] * N for _ in range(M)]

    # 전쟁터를 탐색하며 팀의 힘을 계산한다. 
    for i in range(M):
        for j in range(N):
            if war_field[i][j] == team and not visited[i][j]:  # 현재 팀 이면서 방문하지 않은 위치 검색 
                count, new_visited = find_group(war_field, N, M, (i, j), team, visited)  # 현재 위치에서 시작해서 그룹의 힘을 계산한다. 
                power_of_team += count**2  # 그룹의 힘을 팀의 힘에 추가한다. 
                visited = new_visited  # 방문 배열 업데이트 

    return power_of_team


def main():
    N, M = map(int, inputf().split())

    # 전쟁터 
    war_field = [list(inputf().strip()) for _ in range(M)]

    # 팀 별 힘 계산
    white_team_power = get_team_power(war_field, N, M, 'W')
    blue_team_power = get_team_power(war_field, N, M, 'B')

    print(white_team_power, blue_team_power)

    return 

if __name__ == "__main__":
    main()