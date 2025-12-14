from collections import defaultdict


dxy = [(0, 1), (0, -1), (-1, 0), (1, 0)]  # 우, 좌, 상, 하
rev_dir = {0: 1, 1: 0, 2: 3, 3: 2}


def main():
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    horse_map = [[[] for __ in range(N)] for _ in range(N)]
    pos = defaultdict(list)
    for horse in range(1, K+1):
        x, y, d = map(int, input().split())
        horse_map[x-1][y-1].append(horse)
        pos[horse] = [x-1, y-1, d-1]

    turn = 1
    while True:
        if turn > 1000:  # 턴 1000번 초과할 경우 종료
            turn = -1
            break

        for horse in range(1, K+1):
            x, y, d = pos[horse]
            nx, ny = x + dxy[d][0], y + dxy[d][1]

            # 현재 칸에서 말의 위치
            idx = horse_map[x][y].index(horse)
            group = horse_map[x][y][idx:]

            # 범위 벗어나거나 파란색
            if nx < 0 or nx >= N or ny < 0 or ny >= N or board[nx][ny] == 2:
                # 이동방향 반대로하고 한 칸 이동
                d = rev_dir[d]
                pos[horse][2] = d
                nx, ny = x + dxy[d][0], y + dxy[d][1]

                # 반대쪽도 이동 불가
                if nx < 0 or nx >= N or ny < 0 or ny >= N or board[nx][ny] == 2:
                    continue

            # 기존 위치에서 말 제거
            horse_map[x][y] = horse_map[x][y][:idx]

            # 빨간색이면 순서 반전
            if board[nx][ny] == 1:
                group = group[::-1]

            # 맵에서 말 이동
            horse_map[nx][ny] += group

            # 말 위치 갱신
            for g in group:
                pos[g][0], pos[g][1] = nx, ny

            # 종료 조건
            if len(horse_map[nx][ny]) >= 4:
                print(turn)
                return

        turn += 1

    print(turn)


if __name__ == "__main__":
    main()