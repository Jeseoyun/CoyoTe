from collections import deque

def main():
    size, zero_num = map(int, input().split())
    belt = deque(list(map(int, input().split())))
    isRobots = deque([False] * size)

    cnt = 0

    while True:
        cnt += 1

        #?
        # belt.append(belt.popleft())
        # isRobots.append(isRobots.popleft())
        belt.rotate(1)
        isRobots.rotate(1)

        isRobots[-1] = False

        # 이동 후, 점수 계산 및 로봇 제거
        # 뒤에서부터 읽으면 됨!!!!!!!
        for idx in range(size - 2, -1, -1):
            # 마지막 제거
            if isRobots[idx] == False or isRobots[idx+1] == True or belt[idx+1] <= 0 :
                continue
            
            isRobots[idx] = False
            isRobots[idx + 1] = True
            belt[idx+1] -= 1
        isRobots[-1] = False
        

        # 로봇 등장
        if belt[0] > 0:
            isRobots[0] = True
            # 올리자마자 빼나?
            belt[0] -= 1

        # 탈출 조건
        cur_zero_num = 0
        for num in belt:
            if num == 0:
                cur_zero_num += 1;
        
        if cur_zero_num >= zero_num:
            break
        
    print(cnt)


if __name__ == "__main__":
    main()