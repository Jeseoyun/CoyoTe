def get_area_cnt(room, N):
    row_cnt = 0

    for y in range(N):
        cnt = 0
        for x in range(N):
            # print(room[y][x], end=" ")
            if room[y][x] == "X":
                if cnt >= 2:
                    row_cnt += 1
                cnt = 0
                continue
            cnt += 1
        if cnt >= 2:
            row_cnt += 1
    return row_cnt


def main():
    N = int(input())

    room = [input() for _ in range(N)]
    print(get_area_cnt(room, N), end=" ")

    room = list(zip(*room))
    print(get_area_cnt(room, N))


if __name__ == "__main__":
    main()
