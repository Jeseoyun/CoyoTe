# 안전 영역
# https://www.acmicpc.net/problem/2468

"""
풀이 설명: 
    BFS로 풀었슴둥 
    지역 정보 입력 받을 때, 최저 높이(min_height)와 최고 높이(max_height) 구하고, 
    그 사이 모든 높이를 임계값(물에 잠기는 최대 높이)으로 설정하여 bfs() 를 실행 
    bfs는 모든 좌표를 시작점으로 할 수 있음
    따라서, is_safe()라는 함수로 해당 좌표의 유효성, 안정성 및 방문 여부를 검사 
    is_safe() 함수를 통과한 좌표에 한해서 해당 좌표를 시점으로 하는 BFS를 수행 (deque 사용)
    현재 좌표와 인접한 좌표가 is_safe()를 통과한 경우 해당 좌표를 방문처리 하고 deque에 넣어서 너비 우선 탐색이 가능하게 한다.
"""

import sys 
from collections import deque 

inputf = sys.stdin.readline

def bfs(area:list, threshold:int) -> int:
    rows, cols = len(area), len(area[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = set()

    def is_safe(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or area[r][c]<=threshold or (r, c) in visited:
            return False 
        else:
            return True 
    
    num_of_safe_area = 0
    for r in range(rows):
        for c in range(cols):
            if not is_safe(r, c):
                continue 
            
            dq = deque([(r, c)])
            visited.add((r, c))
            while dq:
                curr_r, curr_c = dq.popleft()
                for dr, dc in directions:
                    next_r = curr_r + dr 
                    next_c = curr_c + dc 
                    if not is_safe(next_r, next_c):
                        continue 
                    visited.add((next_r, next_c))
                    dq.append((next_r, next_c))
            num_of_safe_area += 1

    return num_of_safe_area   

def main():

    N = int(inputf().rstrip())
    area = list()
    min_height = 101 
    max_height = 0
    for _ in range(N):
        _input = list(map(int, inputf().rstrip().split()))
        if min_height > min(_input):
            min_height = min(_input)
        if max_height < max(_input):
            max_height = max(_input)
        area.append(_input)

    max_safe_area = 1
    for h in range(min_height, max_height+1):
        safe_area = bfs(area=area, threshold=h)
        if max_safe_area < safe_area:
            max_safe_area = safe_area
    
    print(max_safe_area)

    return

if __name__=='__main__':
    main()