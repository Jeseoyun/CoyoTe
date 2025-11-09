# 톱니바퀴 
# https://www.acmicpc.net/problem/14891


import sys 
from collections import deque
inputf = sys.stdin.readline

"""
톱니바퀴 A를 회전할 때, 그 옆에 있는 톱니바퀴 B와 서로 맞닿은 톱니의 극이 다르다면, B는 A가 회전한 방향과 반대방향으로 회전하게 된
"""
N = 4 

def rotate_gear(gear, direction):
    """
    gear: 회전시킬 톱니바퀴 상태
    direction: 회전 방향 (-1: 반시계, 1: 시계)
    """
    gear = deque(gear)
    if direction == 1:  # clockwise
        gear.rotate(1)
    elif direction == -1: # counter-clockwise
        gear.rotate(-1)
    return list(gear)


def rotate(gears, wheel_num, direction):
    """
    gears: 현재 톱니바퀴 상태 
    wheel_num: 회전시킬 톱니바퀴 번호
    direction: 회전 방향 (-1: 반시계, 1: 시계)
    """
    # 먼저 회전할 톱니바퀴들을 결정 (회전 전 상태로 비교해야 함)
    rot = [0] * N
    rot[wheel_num] = direction
    
    # 왼쪽으로 연쇄 회전 확인
    for i in range(wheel_num - 1, -1, -1):
        if gears[i][2] != gears[i + 1][6]:  # 회전 전 상태로 비교
            rot[i] = -rot[i + 1]
        else:
            break  # 극이 같으면 더 이상 전파되지 않음
    
    # 오른쪽으로 연쇄 회전 확인
    for i in range(wheel_num + 1, N):
        if gears[i - 1][2] != gears[i][6]:  # 회전 전 상태로 비교
            rot[i] = -rot[i - 1]
        else:
            break  # 극이 같으면 더 이상 전파되지 않음
    
    # 결정된 회전을 한 번에 수행
    for i in range(N):
        if rot[i] != 0:
            gears[i] = rotate_gear(gears[i], rot[i])
    
    return gears


def calculate_score(gears):
    """
    1번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 1점
    2번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 2점
    3번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 4점
    4번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 8점
    """
    
    score = 0
    for i, gear in enumerate(gears):
        if gear[0] == '1':
            score += 2 ** i
            
    return score

def main():
    gears = []  # N극은 0, S극은 1로 나타나있다.
    for _ in range(N):
        gears.append(list(inputf().strip()))  # 상태는 8개의 정수로 이루어져 있고, 12시방향부터 시계방향 순서대로 주어진다.
        
    K = int(inputf())
    rotate_info = []
    for _ in range(K):
        wheel_num, direction = map(int, inputf().split()) # 톱니바퀴 번호, 회전 방향 (-1: 반시계, 1: 시계)
        rotate_info.append((wheel_num, direction))
        
    for wheel_num, direction in rotate_info:
        gears = rotate(gears, wheel_num - 1, direction)  # 1-based를 0-based로 변환
        
    score = calculate_score(gears)
    print(score)
        
    return 

if __name__ == "__main__":
    main()