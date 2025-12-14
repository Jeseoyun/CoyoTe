def solve():
    N, K = map(int, input().split())

    # 0: 흰색, 1: 빨간색, 2: 파란색
    board = [list(map(int, input().split())) for _ in range(N)]

    curr_board = [[[] for _ in range(N)] for _ in range(N)]

    horses = [list(map(int, input().split())) for _ in range(K)]

    # 0:우, 1:좌, 2:상, 3:하
    dxy = ((0, 1), (0, -1), (-1, 0), (1, 0))

    # 말 정보 관리
    # idx_to_pos: 말 번호 -> [행, 열, 몇 번째로 쌓여 있는지]
    # idx_to_dir: 말 번호 -> 방향 인덱스 (0~3)
    idx_to_pos = {}
    idx_to_dir = {}

    for i in range(K):
        r, c, d = horses[i]
        # 0부터 시작
        r -= 1
        c -= 1
        d -= 1

        idx_to_pos[i] = [r, c, len(curr_board[r][c])]
        idx_to_dir[i] = d
        curr_board[r][c].append(i)

    cnt = 0

    while cnt <= 1000:
        cnt += 1

        for i in range(K):
            r, c, h = idx_to_pos[i]
            d = idx_to_dir[i]

            # 다음 위치 계산
            nr = r + dxy[d][0]
            nc = c + dxy[d][1]

            # 파란색이거나 맵을 벗어나는 경우
            if not (0 <= nr < N and 0 <= nc < N) or board[nr][nc] == 2:
                # 방향 반대로 전환: 0<->1, 2<->3
                if d == 0:
                    nd = 1
                elif d == 1:
                    nd = 0
                elif d == 2:
                    nd = 3
                else:
                    nd = 2

                idx_to_dir[i] = nd

                nr = r + dxy[nd][0]
                nc = c + dxy[nd][1]

                # 반대 방향도 파란색이거나 맵을 벗어나면 제자리 유지
                if not (0 <= nr < N and 0 <= nc < N) or board[nr][nc] == 2:
                    continue

            stack = curr_board[r][c]

            # 움직일 말들
            moving_horses = stack[h:]
            curr_board[r][c] = stack[:h]

            # 빨간색이면 순서 뒤집기
            if board[nr][nc] == 1:
                moving_horses.reverse()

            # 이동할 칸의 현재 쌓인 말 높이
            base_h = len(curr_board[nr][nc])

            # 이동할 칸에 쌓기
            curr_board[nr][nc].extend(moving_horses)

            # 이동한 말들의 위치 및 높이 정보 업데이트
            for k, horse_idx in enumerate(moving_horses):
                idx_to_pos[horse_idx] = [nr, nc, base_h + k]

            # 게임 종료 조건 확인: 말이 4개 이상 쌓이면 종료
            if len(curr_board[nr][nc]) >= 4:
                print(cnt)
                return

    print(-1)


if __name__ == "__main__":
    solve()
