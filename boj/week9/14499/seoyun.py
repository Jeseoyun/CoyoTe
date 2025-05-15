from copy import deepcopy


dxy = [(0, 1), (0, -1), (-1, 0), (1, 0)]  # 동, 서, 북, 남


def roll_dice(dice, direction):
    d = deepcopy(dice)

    if direction == 1:  # 동쪽
        # 천장 -> 오 -> 바닥 -> 왼 -> 천장 으로 이동해야하니까
        # 오 -> 천장 / 바닥 -> 오 / 왼 -> 바닥 / 천장 -> 왼
        dice["천장"], dice["오른쪽"], dice["바닥"], dice["왼쪽"] = \
            d["왼쪽"], d["천장"], d["오른쪽"], d["바닥"]
    elif direction == 2:  # 서쪽
        # 천장 -> 왼 -> 바닥 -> 오 -> 천장 으로 이동해야하니까
        # 왼 -> 천장 / 바닥 -> 왼 / 오 -> 바닥 / 천장 -> 오
        dice["천장"], dice["왼쪽"], dice["바닥"], dice["오른쪽"] = \
            d["오른쪽"], d["천장"], d["왼쪽"], d["바닥"]
    elif direction == 3:  # 북쪽
        # 천장 -> 앞 -> 바닥 -> 뒤 -> 천장 으로 이동해야하니까
        # 앞 -> 천장 / 바닥 -> 앞 / 뒤 -> 바닥 / 천장 -> 뒤
        dice["천장"], dice["뒤"], dice["바닥"], dice["앞"] = \
            d["앞"], d["천장"], d["뒤"], d["바닥"]
    elif direction == 4:  # 남쪽
        # 천장 -> 뒤 -> 바닥 -> 앞 -> 천장 으로 이동해야하니까
        # 뒤 -> 천장 / 바닥 -> 뒤 / 앞 -> 바닥 / 천장 -> 앞
        dice["천장"], dice["앞"], dice["바닥"], dice["뒤"] = \
            d["뒤"], d["천장"], d["앞"], d["바닥"]

    return dice


def main():
    N, M, x, y, K = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    commands = list(map(int, input().split()))

    dice = {"천장": 1, "바닥": 6, "오른쪽": 3, "왼쪽": 4, "뒤": 2, "앞": 5}
    dice_number = {i: 0 for i in range(1, 7)}

    curr_x, curr_y = x, y

    for comm in commands:
        nx = curr_x + dxy[comm-1][0]
        ny = curr_y + dxy[comm-1][1]

        # 지도 바깥으로 이동 불가
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue

        # 주사위 굴리기
        dice = roll_dice(dice, comm)

        # 숫자 바꾸기
        bottom = dice["바닥"]
        if grid[nx][ny] == 0:  # 칸이 0이면 주사위 바닥면 수 복사
            grid[nx][ny] = dice_number[bottom]
        else:  # 아니면 칸 수가 주사위 바닥에 복사, 칸 수는 0
            dice_number[bottom] = grid[nx][ny]
            grid[nx][ny] = 0

        top = dice["천장"]
        print(dice_number[top])

        curr_x, curr_y = nx, ny


if __name__ == "__main__":
    main()