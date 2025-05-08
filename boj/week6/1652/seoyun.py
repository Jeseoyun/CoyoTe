# def transpose(matrix):
#     return [list(arr) for arr in zip(*matrix)]
#
#
# def get_X_index(arr):
#     return [idx for idx, val in enumerate(arr) if val=='X']
#
#
# def get_row_space_num(idx_arr):
#     space_num = 0
#     for i, idx in enumerate(idx_arr):
#         # 첫 번째 나온 X 위치면서 인덱스 값이 2보다 크면 왼쪽에 공간 있음
#         if i == 0:
#             if idx >= MIN_SIZE:
#                 space_num += 1
#             else:
#                 continue
#
#         # 마지막 X 위치면서 인덱스 값이 (N-1)-MIN_SIZE보다 작으면 오른쪽에 공간 있음
#         elif (i == len(idx_arr)-1) and (idx <= N-1-MIN_SIZE):
#             space_num += 1
#
#         # 사이값 계산 (첫 번째 인덱스의 경우는 가장 첫 if 문에서 예외처리 완료)
#         else:
#             if idx_arr[i]-idx_arr[i-1] > 2:
#                 space_num += 1
#
#     return space_num
#
#
# def get_all_row_space_num(matrix):
#     all_space_num = 0
#
#     for y in range(N):
#         # 1. X 위치 구하기
#         X_idx = get_X_index(matrix[y])
#
#         # 2. 구간 나누고 사이값 MIN_SIZE(2) 이상이면 더해주기
#         if not X_idx:  # X가 없음
#             all_space_num += 1
#         elif len(X_idx) == N:  # 모두 X
#             continue
#         elif len(X_idx) == 1:  # X가 1개 있음
#             left_space = X_idx[0] >= MIN_SIZE
#             right_space = X_idx[0] <= N - 1 - MIN_SIZE
#             if left_space and right_space:
#                 all_space_num += 2
#             elif left_space or right_space:
#                 all_space_num += 1
#             # 양쪽 모두 공간이 없으면 아무 일도 안 함
#         else:  # 여백마다 공간 있는지 계산
#             all_space_num += get_row_space_num(X_idx)
#
#     return all_space_num
#
#
# MIN_SIZE = 2
#
# N = int(input())
# room = []
#
# for _ in range(N):
#     room.append([_ for _ in input()])
#
# col = get_all_row_space_num(room)
# row = get_all_row_space_num(transpose(room))
#
# print(col, row, sep=" ")


def space_counter(matrix, min_size):
    result = 0
    for arr in matrix:
        # print(arr)
        if 'X' not in arr:
            if len(arr) >= min_size:
                result += 1
            continue
        elif '.' not in arr:
            continue

        cnt = 0
        for elem in arr:
            if elem == 'X':
                if  cnt >= min_size:
                    result += 1
                cnt = 0
            elif elem == '.':
                cnt += 1
            # print(elem, cnt, result)
        if cnt >= min_size:
            result += 1
    return result


def main():
    N = int(input())
    room = []

    MIN_SIZE = 2

    for _ in range(N):
        room.append([_ for _ in input()])

    row = space_counter(room, MIN_SIZE)
    col = space_counter(list(zip(*room)), MIN_SIZE)

    print(row, col)


if __name__ == "__main__":
    main()
