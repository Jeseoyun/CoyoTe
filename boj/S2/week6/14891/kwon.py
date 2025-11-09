import sys
from collections import deque

input = sys.stdin.readline

gears = []
for _ in range(4):
    gears.append(deque(list(map(int, input().strip()))))

k = int(input())
commands = [list(map(int, input().split())) for _ in range(k)]

for gear_num, direction in commands:

    gear_idx = gear_num - 1

    rotations_to_do = [0] * 4
    rotations_to_do[gear_idx] = direction

    for i in range(gear_idx, 0, -1):
        if gears[i][6] != gears[i - 1][2]:
            rotations_to_do[i - 1] = -rotations_to_do[i]
        else:
            break

    for i in range(gear_idx, 3):
        if gears[i][2] != gears[i + 1][6]:
            rotations_to_do[i + 1] = -rotations_to_do[i]
        else:
            break

    for i in range(4):
        if rotations_to_do[i] != 0:

            gears[i].rotate(rotations_to_do[i])

total_score = 0
if gears[0][0] == 1:
    total_score += 1
if gears[1][0] == 1:
    total_score += 2
if gears[2][0] == 1:
    total_score += 4
if gears[3][0] == 1:
    total_score += 8

print(total_score)
