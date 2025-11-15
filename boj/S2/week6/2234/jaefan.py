# 성곽 
# https://www.acmicpc.net/problem/2234

import sys 
from collections import deque
inputf = sys.stdin.readline

"""
첫째 줄에 두 정수 N, M이 주어진다. 
다음 M개의 줄에는 N개의 정수로 벽에 대한 정보가 주어진다. 
벽에 대한 정보는 한 정수로 주어지는데, 서쪽에 벽이 있을 때는 1을, 북쪽에 벽이 있을 때는 2를, 동쪽에 벽이 있을 때는 4를, 남쪽에 벽이 있을 때는 8을 더한 값이 주어진다. 
참고로 이진수의 각 비트를 생각하면 쉽다. 따라서 이 값은 0부터 15까지의 범위 안에 있다.

1. 성에 있는 방의 개수 
2. 가장 넓은 방의 크기 
3. 하나의 벽을 제거하여 얻을 수 있는 가장 넓은 방의 크기
"""

DIRECTIONS = [(0, -1), (-1, 0), (0, 1), (1, 0)]

def get_direction(wall_info):
    available_directions = []
    
    # 서쪽에 벽이 있음 -> 못감 
    if wall_info & 1:
        pass 
    # 서쪽에 벽이 없음 -> 갈 수 있음 
    else: 
        available_directions.append((0, -1))
    # 북쪽에 벽이 있음 -> 못감 
    if wall_info & 2:
        pass 
    else: 
        available_directions.append((-1, 0))
    # 동쪽에 벽이 있음 -> 못감 
    if wall_info & 4:
        pass 
    else: 
        available_directions.append((0, 1))
    # 남쪽에 벽이 있음 -> 못감 
    if wall_info & 8:
        pass 
    else: 
        available_directions.append((1, 0))
        
    return available_directions


def main():
    
    # NxM 크기의 성곽 
    N, M = map(int, inputf().split())
    grid = []
    for _ in range(M):
        grid.append(list(map(int, inputf().split())))
        
    # bfs 탐색으로 진행, 방문 여부 체크 및 방 번호 할당
    visited = [[-1] * N for _ in range(M)]
    
    # 방 정보
    room_info = dict()
    # 방 번호
    room_num = 0 
    
    # 방 탐색: BFS
    for r in range(M):
        for c in range(N):
            # print(r, c) # DEBUG
            if visited[r][c] != -1:  # 방 번호가 할당된 경우 (이미 방문한 경우)
                continue 
            # 방의 시작점이 된다. -> bfs 탐색 시작 
            # print(f"room_num: {room_num}") # DEBUG
            visited[r][c] = room_num  # 방 번호 할당: 방문 처리 
            room_size = 0  # 방 크기 초기화
            queue = deque([(r, c)])  # bfs 탐색 준비 
            while queue:
                x, y = queue.popleft()
                room_size += 1  # 방 크기 증가
                for dx, dy in get_direction(grid[x][y]):  # 현재 위치에서 이동 가능한 방향 확인 
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < M and 0 <= ny < N and visited[nx][ny] == -1:  # 유효성 검사 및 방문 여부 체크 
                        visited[nx][ny] = room_num  # 방 번호 할당: 방문 처리 
                        queue.append((nx, ny))
            room_info[room_num] = room_size  # 방 크기 저장
            room_num += 1  # 방 번호 증가
            
    # DEBUG
    # for _ in range(len(visited)):
    #     print(visited[_]) # DEBUG
            
    # 1. 방의 개수 
    print(len(room_info))
    
    # 2. 가장 넓은 방의 크기 
    print(max(room_info.values()))
            
    # 3. 하나의 벽을 제거하여 얻을 수 있는 가장 넓은 방의 크기
    max_room_size = 0  # 가장 넓은 방의 크기 초기화
    for r in range(M):
        for c in range(N):
            curr_room_num = visited[r][c]
            for dr, dy in DIRECTIONS:
                nr, nc = r + dr, c + dy
                if 0 <= nr < M and 0 <= nc < N:
                    if visited[nr][nc] != curr_room_num:
                        max_room_size = max(max_room_size, room_info[curr_room_num] + room_info[visited[nr][nc]])
    print(max_room_size)
            
    return 

if __name__ == "__main__":
    main()