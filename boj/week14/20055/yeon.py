# 컨베이어 벨트 위의 로봇
# https://www.acmicpc.net/problem/20055

import sys
from collections import deque 

inputf = sys.stdin.readline 


def main():

    N, K = map(int, inputf().rstrip().split())  # N: 벨트 길이, K: 내구도 0인 칸의 개수 
    belt = deque(list(map(int, inputf().rstrip().split())))  # 벨트의 내구도 리스트

    robots = deque([0] * N)  # 로봇의 위치를 나타내는 리스트 (0: 로봇 없음, 1: 로봇 있음)
    step = 0  # 단계 수

    # print(belt)  # debug: 초기 벨트 상태 출력
    while True:
        step += 1

        # 1. 벨트가 각 칸에 있는 로봇과 함께 한 칸 회전한다.
        belt.rotate(1)
        # 로봇 함께 회전 
        robots.rotate(1)
        robots[0] = 0 
        robots[-1] = 0  # 벨트의 끝에 있는 로봇은 제거 (벨트가 회전하면서 로봇이 벨트 끝에 도달하면 내린다)

        

        # 2. 로봇 이동 
        # 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다.
        # 만약 이동할 수 없다면 가만히 있는다.
        # 로봇을 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1이상 남아있어야 한다. 
        # 언제든지 로봇이 내리는 위치에 도달하면 그 즉시 내린다. -> 
        for i in range(N-1, -1, -1):  # 로봇을 뒤에서부터 이동 
            if robots[i] == 1:  # 현재 칸에 로봇이 있는 경우 
                next_index = i + 1
                if next_index < N and robots[next_index] == 0 and belt[next_index] > 0:
                    robots[i] = 0  # 현재 칸의 로봇을 제거 
                    robots[next_index] = 1  # 다음 칸에 로봇 추가 
                    belt[next_index] -= 1  # 벨트 내구도 감소 
                elif next_index == N-1:  # 로봇이 벨트 끝에 도달한 경우
                    robots[next_index] = 0  # 현재 칸에서 로봇 제거 
                    # 내리는 칸에 도달하면 그 즉시 내린다. 라는 조건이 있으므로 굳이 올리지 않음 

        # 3. 올리는 위치에 있는 칸의 내구도가 0이 아니라면 올리는 위치에 로봇을 올린다.
        if belt[0] > 0 and robots[0] == 0:  # 올리는 위치에 로봇이 없고, 내구도가 0이 아닌 경우
            robots[0] = 1  # 올리는 위치에 로봇을 올림
            belt[0] -= 1  # 벨트의 내구도 감소 -> 이 조건을 못봐서 개고생함.... 

        # print(belt)  # debug: 회전 후 벨트 상태 출력
        # print(robots)

        # 4. 내구도가 0인 칸의 개수가 K 개 이상이라면 과정을 종료한다.
        is_finished = False 
        count_zero = 0
        for durability in belt:
            if durability == 0:
                count_zero += 1
            if count_zero == K:
                print(step)
                is_finished = True
                break
        if is_finished:
            break

        
    return

if __name__=='__main__':
    main()