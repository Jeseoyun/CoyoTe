# 달이 차오른다, 가자.
# https://www.acmicpc.net/problem/1194

"""
- . : 빈칸, 언제나 이동 가능 
- # : 벽, 이동 불가 
- 'a' - 'f': 열쇠, 언제나 이동 가능, 처음 들어가면 열쇠를 집는다.
- 'A' - 'F': 문, 해당 열쇠를 가지고 있어야 이동 가능
- '0' : 민식이의 현재 위치 
- '1': 출구, 도착 시 미로 탈출 

이동 방향: 수직/수평 한 칸

미로를 탈출하는 데 걸리는 이동 횟수의 최솟값 
- 탈출 불가능 -> -1 출력 
"""


"""scratchpad 
- 최단 거리 문제 -> BFS 
- deque 사용 
- 현재 위치에서 이동 가능한 방향을 찾는다.
- escape 함수 작성
    - input: grid, start
    - output: minimum moves 
    - 방문 처리 visited 사용 -> 같은 위치라도 가지고 있는 키 상태가 다르면 다른 방문이다. -> [r][c][keys] 구조의 3차원 배열 사용 
    - [keys]: 가질 수 있는 키의 개수는 6개. -> 소유하고 있는 키를 관리. 'a', 'b', ... 'abcdef' 
        -> 키 관리해주는 함수 필요. -> normalize_keys() -> 중복 제거 + 정렬
    - 2차원 배열로 수정하고, [r][c] 좌표에 (moves, keys) 정보를 튜플로 저장. 
"""

import sys
from typing import List, Tuple
from collections import deque 

inputf = sys.stdin.readline
DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def normalize_keys(keys_str: str) -> str:
    """키 문자열을 정렬하여 정규화 (중복 제거 + 정렬)"""
    return ''.join(sorted(set(keys_str)))

def is_valid(position: Tuple[int, int], grid: List[List[str]], keys: str, visited: set) -> Tuple[bool, str]:
    """
    이동 가능 여부와 새로운 키 상태를 반환
    - return: (valid, new_keys)
      - valid=False면 이동 불가
      - valid=True면 이동 가능, new_keys는 업데이트된 키 상태
    """
    nr, nc = position
    N, M = len(grid), len(grid[0])
    
    # 1. 범위 체크
    if not (0 <= nr < N and 0 <= nc < M):
        return False, keys
    
    cell = grid[nr][nc]
    
    # 2. 벽 체크
    if cell == '#':
        return False, keys
    
    # 3. 문 체크 -> 해당 열쇠가 있어야 통과 가능
    if 'A' <= cell <= 'F':
        required_key = cell.lower()
        if required_key not in keys:  # 해당 키가 없으면 통과 불가
            return False, keys
    
    # 4. 새로운 키 상태 계산 (열쇠를 주우면 키 상태 업데이트)
    new_keys = keys
    if 'a' <= cell <= 'f':
        if cell not in keys:  # 아직 없는 키면 추가
            new_keys = normalize_keys(keys + cell)
    
    # 5. 방문 체크 (같은 위치 + 같은 키 상태면 스킵)
    state = (nr, nc, new_keys)
    if state in visited:
        return False, keys
    
    return True, new_keys

def escape(grid:List[List[str]], start:Tuple[int, int]) -> int:
    N, M = len(grid), len(grid[0])
    
    # visited를 set으로 관리: (r, c, normalized_keys) 튜플 저장
    visited = set()
    
    # queue에 (r, c, keys_str, moves) 저장
    queue = deque([(start[0], start[1], "", 0)])
    visited.add((start[0], start[1], ""))
    
    while queue:
        r, c, keys, moves = queue.popleft()
        
        # 출구 도착 체크
        if grid[r][c] == '1':
            return moves
        
        # 이동 가능한 방향 확인 후 큐에 추가 
        for dr, dc in DIRECTIONS:
            nr, nc = r + dr, c + dc
            
            valid, new_keys = is_valid((nr, nc), grid, keys, visited)
            if not valid:
                continue
            
            visited.add((nr, nc, new_keys))
            queue.append((nr, nc, new_keys, moves + 1))
    
    return -1 


def main():
    
    N, M = map(int, inputf().split())
    grid = []
    start = None 
    for i in range(N):
        row = inputf().strip()
        for j in range(M):
            if row[j] == '0':
                start = (i, j)
                break 
        grid.append(list(row))
    
    minimum_moves = escape(grid, start)
    
    print(minimum_moves)

    return 

if __name__ == "__main__":
    main()
    