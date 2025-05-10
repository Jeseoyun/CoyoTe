dxy = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def find_empty_seat_info(seats, n, preference):
    empty_seats = []
    for x in range(n):
        for y in range(n):
            if seats[x][y] != 0:  # 이미 누가 앉아 있음
                continue

            near_empty_cnt = 0
            near_preference = 0

            for dx, dy in dxy:
                nx, ny = x + dx, y + dy

                if nx < 0 or nx >= n or ny < 0 or ny >= n:  # 자리 범위 초과
                    continue

                if seats[nx][ny] == 0:  # 주변의 빈 자리 수 확인용
                    near_empty_cnt += 1

                if seats[nx][ny] in preference:  # 주변에 좋아하는 친구 확인용
                    near_preference += 1

            empty_seats.append((x, y, near_empty_cnt, near_preference))

    return empty_seats


def main():
    N = int(input())
    seats = [[0]*N for _ in range(N)]

    # 1. 자리 배치 하기
    student_preference = dict()
    for _ in range(N**2):
        student, *preference = list(map(int, input().split()))
        student_preference[student] = preference

        # 1) 빈 칸 구하기
        empty_seats = find_empty_seat_info(seats, N, preference)

        # 2) 주변에 좋아하는 친구가 가장 많은 -> 주변에 빈 자리가 가장 많은
        for i in range(3, 1, -1):
            max_val = max(seat[i] for seat in empty_seats)
            empty_seats = [seat for seat in empty_seats if seat[i] == max_val]

            if len(empty_seats) == 1:
                x, y, _, preference = empty_seats[0]

                seats[x][y] = student
                break

        if len(empty_seats) == 1:
            continue

        # 3) 행 번호가 최소, 열 번호 최소
        x, y, _, preference = min(empty_seats, key=lambda seat: (seat[0], seat[1]))

        seats[x][y] = student

    # print(seats)

    # 2. 만족도 구하기
    total_preference = 0
    for x in range(N):
        for y in range(N):
            student = seats[x][y]
            preference = 0

            for dx, dy in dxy:
                nx, ny = x+dx, y+dy

                if nx < 0 or nx >= N or ny < 0 or ny >= N:
                    continue

                if seats[nx][ny] in student_preference[student]:
                    preference += 1

            total_preference += int(10 ** (preference - 1))

    print(total_preference)



if __name__ == "__main__":
    main()