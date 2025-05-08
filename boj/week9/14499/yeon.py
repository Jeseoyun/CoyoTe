# 주사위 굴리기

def move_dice(dice, direction):
    """주사위 이동 방향에 따른 주사위의 상태 변화

    Args:
        dice (list): 주사위 상태 (0: 위, 1: 뒤, 2: 오른쪽, 3: 왼쪽, 4: 앞, 5: 바닥)
        direction (int): 이동 방향 (1: 동쪽, 2: 서쪽, 3: 북쪽, 4: 남쪽)

    Returns:
        list: 이동 후 주사위 상태
    """ 
    if direction == 1:  # 동쪽으로 이동
        tmp = dice[0]
        dice[0] = dice[3]
        dice[3] = dice[5]
        dice[5] = dice[2]
        dice[2] = tmp
    elif direction == 2:  # 서쪽으로 이동
        tmp = dice[0]
        dice[0] = dice[2]
        dice[2] = dice[5]
        dice[5] = dice[3]
        dice[3] = tmp
    elif direction == 3:  # 북쪽으로 이동 
        tmp = dice[0]
        dice[0] = dice[1]
        dice[1] = dice[5]
        dice[5] = dice[4]
        dice[4] = tmp
    elif direction == 4:  # 남쪽으로 이동
        tmp = dice[0]
        dice[0] = dice[4]
        dice[4] = dice[5]
        dice[5] = dice[1]
        dice[1] = tmp

    return dice


def main():# 
    N, M, x, y, K = map(int, input().split())
    # N: 세로 크기, M: 가로 크기, (x, y): 주사위 좌표, K: 명령의 개수

    maap = [list(map(int, input().split())) for _ in range(N)]  # 지도
    # print(maap)
    commands = list(map(int, input().split()))  # K개 명령어
    # 주사위의 초기 상태
    dice = [0 for _ in range(6)]  # 주사위의 각 면에 대한 값 (위, 뒤, 오른쪽, 왼쪽, 앞, 바닥)

    # 명령에 따른 주사위 이동 방향 
    command_dict = {
        1: (0, 1),  # 동
        2: (0, -1),  # 서
        3: (-1, 0),  # 북
        4: (1, 0)   # 남
    }

    for cmd in commands:
        dx, dy = command_dict[cmd]
        nx, ny = x + dx, y + dy
        # 이동할 좌표가 지도 범위를 벗어나는 경우
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            # print(-1)  # debugging
            continue
        # 주사위 이동
        dice = move_dice(dice, cmd)
        # 이동한 칸에 쓰여 있는 수가 0인 경우 -> 주사위 바닥면의 수를 칸에 복사 
        if maap[nx][ny] == 0:
            maap[nx][ny] = dice[5]  
        # 이동한 칸에 쓰여 있는 수가 0이 아닌 경우
        else:
            # 칸에 쓰여 있는 수를 주사위 바닥면에 복사
            dice[5] = maap[nx][ny]
            maap[nx][ny] = 0  # 칸의 수를 0으로 초기화
        # 주사위의 위쪽 면에 있는 수 출력
        print(dice[0])
        
        x, y = nx, ny  # 주사위 좌표 업데이트 -> 이거 안해줘서 한참 디버깅함,,, ㄹㅈㄷ

    return

if __name__=='__main__':
    main()