def main():
    N, K = map(int, input().split())
    belt_durability = list(map(int, input().split()))  # 각 칸의 내구도, 길이: 2N
    robot = [0 for _ in range(N)]  # 각 칸 로봇 존재 여부, 0: 없음, 1: 있음

    step = 0
    while belt_durability.count(0) < K:
        # 1. 벨트와 로봇이 함께 한 칸 회전
        belt_durability = [belt_durability[-1]] + belt_durability[:-1]  # 벨트 회전(가장 마지막 놈이 가장 처음에 온다)
        robot = [0] + robot[:-1]  # 로봇 회전(가장 마지막놈은 내리고 처음에 빈 공간 들어온다)

        # 2. 로봇 이동
        for idx in range(N-1, -1, -1):
            if robot[idx] == 0:  # 로봇 없음
                continue

            if idx == N-1:  # 내리는 위치
                robot[idx] = 0
                continue

            # 옮길 위치에 로봇이 없고, 내구도가 1 이상이면 로봇 옮긴다
            if robot[idx+1] == 0 and belt_durability[idx+1] >= 1:
                belt_durability[idx+1] -= 1
                robot[idx], robot[idx+1] = 0, 1

        # 3. 올리는 위치에 내구도가 0이 아니면 로봇 올린다
        if belt_durability[0] > 0:
            belt_durability[0] -= 1
            robot[0] = 1

        step += 1

    print(step)


if __name__ == "__main__":
    main()