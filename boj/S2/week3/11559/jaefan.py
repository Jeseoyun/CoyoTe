# Puyo Puyo
# https://www.acmicpc.net/problem/11559 

import sys 
from collections import deque

inputf = sys.stdin.readline

N = 12  # 행 (높이)
M = 6   # 열 (너비)

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 상하좌우

def remove_puyos(board, groups_to_pop):
    """
    연결된 뿌요 그룹들을 제거 ('.'으로 변경)
    """
    for group in groups_to_pop:
        for x, y in group:
            board[x][y] = '.'

def apply_gravity(board):
    """
    중력 적용: 빈 공간을 채우기 위해 위의 뿌요들을 아래로 이동
    """
    for j in range(M):  # 각 열에 대해
        # 아래에서 위로 올라가며 빈 공간 찾기
        empty_positions = []
        for i in range(N-1, -1, -1):
            if board[i][j] == '.':
                empty_positions.append(i)
            elif empty_positions:
                # 빈 공간이 있고 현재 위치에 뿌요가 있으면 이동
                empty_pos = empty_positions.pop(0)
                board[empty_pos][j] = board[i][j]
                board[i][j] = '.'
                empty_positions.append(i)

def find_connected_puyos_bfs(board):
    """
    BFS를 사용하여 4개 이상 연결된 뿌요 그룹들을 찾아서 반환
    """
    visited = [[False] * M for _ in range(N)]
    groups_to_pop = []
    
    for i in range(N):
        for j in range(M):
            if board[i][j] != '.' and not visited[i][j]:
                # BFS로 연결된 뿌요들 찾기
                connected = []
                queue = deque([(i, j)])
                visited[i][j] = True
                
                while queue:
                    x, y = queue.popleft()
                    connected.append((x, y))
                    
                    for dx, dy in DIRECTIONS:
                        nx, ny = x + dx, y + dy
                        if (0 <= nx < N and 0 <= ny < M and 
                            not visited[nx][ny] and 
                            board[nx][ny] == board[x][y]):
                            visited[nx][ny] = True
                            queue.append((nx, ny))
                
                # 4개 이상 연결된 경우 터뜨릴 그룹에 추가
                if len(connected) >= 4:
                    groups_to_pop.append(connected)
    
    return groups_to_pop


def main():
    # 보드 입력: .: empty, R: red, G: green, B: blue, P: purple, Y: yellow
    board = [list(inputf().strip()) for _ in range(N)]
    
    count = 0
    
    while True:
        # 1. 4개 이상 연결된 뿌요 그룹 찾기
        groups_to_pop = find_connected_puyos_bfs(board)
        
        # 더 이상 터질 뿌요가 없으면 종료
        if not groups_to_pop:
            break
        
        # 2. 뿌요 터뜨리기
        remove_puyos(board, groups_to_pop)
        
        # 3. 중력 효과 적용
        apply_gravity(board)
        
        # 4. 연쇄 횟수 증가
        count += 1
    
    print(count)

if __name__ == "__main__":
    main()