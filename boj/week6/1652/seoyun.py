# 1. X의 인덱스 구한다
# 2. 각 X인덱스 이전에 점이 몇 개 있는지 구하고, 점 개수가 2개가 넘으면 col++
# 3. transpose해서 또 점 2개 넘으면 row++


def transpose(matrix):
    return [list(arr) for arr in zip(*matrix)]


def get_X_index(arr):
    return [idx for idx, val in enumerate(arr) if val=='X']


def get_row_space_num(idx_arr):
    space_num = 0
    for i, idx in enumerate(idx_arr):
        # 첫 번째 나온 X 위치면서 인덱스 값이 2보다 크면 왼쪽에 공간 있음
        if i == 0:
            if idx >= MIN_SIZE:
                space_num += 1
            else:
                continue

        # 마지막 X 위치면서 인덱스 값이 (N-1)-MIN_SIZE보다 작으면 오른쪽에 공간 있음
        elif (i == len(idx_arr)-1) and (idx <= N-1-MIN_SIZE):
            space_num += 1

        # 사이값 계산 (첫 번째 인덱스의 경우는 가장 첫 if 문에서 예외처리 완료)
        else:
            if idx_arr[i]-idx_arr[i-1] > 2:
                space_num += 1

    return space_num


def get_all_row_space_num(matrix):
    all_space_num = 0

    for y in range(N):
        # 1. X 위치 구하기
        X_idx = get_X_index(matrix[y])

        # 2. 구간 나누고 사이값 MIN_SIZE(2) 이상이면 더해주기
        if not X_idx:  # X가 없음
            all_space_num += 1
        elif len(X_idx) == N:  # 모두 X
            continue
        elif len(X_idx) == 1:  # X가 1개 있음(공간 2개로 나뉨)
            # X가 한 개 있는데 한 쪽 여백에는 누울 수 있는 공간이 없음
            if X_idx[0] < MIN_SIZE or X_idx[0] > N-MIN_SIZE:
                all_space_num += 1
            # X의 양 옆으로 공간 있음
            else:
                all_space_num += 2
        else:  # 여백마다 공간 있는지 계산
            all_space_num += get_row_space_num(X_idx)

    return all_space_num


MIN_SIZE = 2

N = int(input())
room = []

for _ in range(N):
    room.append([_ for _ in input()])

col = get_all_row_space_num(room)
row = get_all_row_space_num(transpose(room))

print(col, row, sep=" ")