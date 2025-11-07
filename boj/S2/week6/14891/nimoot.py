from collections import deque

# 회전
def rotate(num, direction):
    rot = [0] * 4
    rot[num] = direction

    # 왼쪽
    for i in range(num - 1, -1, -1):
        if wheels[i][2] != wheels[i + 1][6]:
            rot[i] = -rot[i + 1]
        else:
            break

    # 오른쪽
    for i in range(num + 1, 4):
        if wheels[i - 1][2] != wheels[i][6]:
            rot[i] = -rot[i - 1]
        else:
            break

    # 회전
    for i in range(4):
        if rot[i] != 0:
            wheels[i].rotate(rot[i])


wheels = [deque(input().strip()) for _ in range(4)]
k = int(input())


for _ in range(k):
    num, direction = map(int, input().split())
    rotate(num - 1, direction)


ans = 0
for i in range(4):
    if wheels[i][0] == '1':
        ans += pow(2,i)

print(ans)
