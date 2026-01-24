dxy = [(1, 0), (0, -1), (-1, 0), (0, 1)]
square = [(1, 0), (0, 1), (1, 1)]


def spin_by_pos(base, target):
    bx, by = base
    tx, ty = target
    dx, dy = tx-bx, ty-by

    return bx-dy, by+dx


def dragon_curve(sx, sy, dir, gen):
    trace = [(sx, sy), (sx+dxy[dir][0], sy+dxy[dir][1])]  # 0세대

    for _ in range(gen):
        # 끝 점 기준 90도 회전
        spined = [spin_by_pos(trace[-1], target) for target in reversed(trace[:-1])]
        trace += spined
        # print(trace)

    return trace


def main():
    N = int(input())

    spots = set()
    # traces = set()

    # 1. 드레곤커브 만들기
    for _ in range(N):
        x, y, d, g = map(int, input().split())  # (x, y), dir, gen
        dc = dragon_curve(x, y, d, g)

        for i in range(len(dc)):
            spots.add(dc[i])
            # traces.add((dc[i], dc[i+1]))
        # spots.add(dc[-1])
    # print(spots)
    # print(traces)

    # 2. 네 꼭지점이 모두 드래곤 커브의 일부인 정사각형 개수 찾기
    square_cnt = 0
    for x, y in spots:
        is_square = True
        for qx, qy in square:
            if (x+qx, y+qy) not in spots:
                is_square = False
                break

        if is_square:
            square_cnt += 1

    print(square_cnt)


if __name__ == "__main__":
    main()
