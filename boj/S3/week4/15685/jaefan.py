# 드래곤 커브 
# https://www.acmicpc.net/problem/15685

"""
x 축: 우
y 축: 하

방향은 0, 1, 2, 3 중 하나이고, 다음을 의미한다.

0: x좌표가 증가하는 방향 (→)
1: y좌표가 감소하는 방향 (↑)
2: x좌표가 감소하는 방향 (←)
3: y좌표가 증가하는 방향 (↓)
"""

"""scratchpad 
'K(K > 1)세대 드래곤 커브는 K-1세대 드래곤 커브를 끝 점을 기준으로 90도 시계 방향 회전 시킨 다음, 그것을 끝 점에 붙인 것이다.'
-> K 세대 드래곤 커브는 K-1 세대 드래곤 커브의 이동 방향을 역(끝 -> 시작)으로 따라가되, 그 방향은 시계 방향으로 90도씩 회전 된 상태이다. 
-> K 세대 드래곤 커브는 1세대부터 시작해서 K 까지 반복해가며 그린다. 

- 1 세대 DC 는 시작 좌표에서 시작 방향으로 한 칸 이동한다. 
- 2 세대 DC 는 1세대 DC 를 90도 눕혀서 이어
"""

import sys 
from typing import *

inputf = sys.stdin.readline

def draw_dragon_curve(grid: List, dragon_curves: List):

    # 시계 방향 90도 회전 매핑
    ROTATE_MAP = {
        0: 1,
        1: 2,
        2: 3, 
        3: 0
    }

    DIRECTIONS = [[1, 0], [0, -1], [-1, 0], [0, 1]]
    # dx = (1, 0, -1, 0)
    # dy = (0, -1, 0, 1)

    for x, y, d, g in dragon_curves:
        directions = [d]
        # 순회 하면서 이전 세대의 이동 방향을 역으로, 그리고 90도 회전 시켜서 directions 에 추가 
        for _ in range(g):
            for direction in reversed(directions):
                directions.append(ROTATE_MAP[direction])

        grid[y][x] = 1
        for direction in directions:
            x += DIRECTIONS[direction][0]
            y += DIRECTIONS[direction][1]
            grid[y][x] = 1

    return grid 


def find_rectangle(grid: List):

    """
    y 축 (row) 를 기준으로 i 번째 row 와 i+1 번째 row 를 가지고 
    x 축 (col) 을 순회하면서 4 모서리 좌표가 동일하다면 num += 1
    """

    number_of_rectangle = 0
    for y in range(100):
        row = grid[y]  # 현재 열 
        row_below = grid[y + 1]  # 다음 열 
        for x in range(100):
            if row[x] and row[x + 1] and row_below[x] and row_below[x + 1]:
                number_of_rectangle += 1

    return number_of_rectangle 

def main():

    N = int(inputf())  # 드래곤 커브 개수 
    grid = [[0 for _ in range(101)] for _ in range(101)]

    dragon_curves = list()
    for _ in range(N):
        # [x: 시작 x 좌표, y: 시작 y 좌표, d: 시작 방향, g: 세대]
        dragon_curves.append(list(map(int, inputf().split())))  

    grid = draw_dragon_curve(grid, dragon_curves)

    number_of_rectangle = find_rectangle(grid)

    print(number_of_rectangle)
    return

if __name__=='__main__':
    main()
