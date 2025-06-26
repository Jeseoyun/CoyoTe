from collections import deque
N, K = map(int, input().split())
durability = deque(map(int, input().split()))
belt = deque([False] * (N * 2)) # belt 위에 로봇이 있는지 여부
# bot_pos = [] # 들어온 순서대로 위치 확인

PUT_IDX = 0
OUT_IDX = N - 1
round_num = 1
# print("durability:", list(durability))
# print("belt:", list(belt))
# print()

while True:
    # 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
    durability.rotate()
    belt.rotate()

    # 언제든지 로봇이 내리는 위치에 도달하면 그 즉시 내린다.
    belt[OUT_IDX] = False


    # 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
    for i in range(N - 2, -1, -1):
        # 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
        if not belt[i]:
            continue
        n_i = i + 1
        if not belt[n_i] and durability[n_i] >= 1:
            durability[n_i] -= 1
            belt[i] = False
            belt[n_i] = True
    
    # 언제든지 로봇이 내리는 위치에 도달하면 그 즉시 내린다.
    belt[OUT_IDX] = False

    # 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
    if durability[PUT_IDX]:
        durability[PUT_IDX] -= 1
        belt[PUT_IDX] = True
        
    # print("durability:", list(durability))
    # print("belt:", list(belt))
    # print()
    # 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.
    if durability.count(0) >= K:
        break
    round_num += 1

print(round_num)

