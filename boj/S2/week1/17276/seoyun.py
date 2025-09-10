import copy


def spin_matrix(matrix, n):
    new_matrix = copy.deepcopy(matrix)

    for i in range(n):
        # 1. 주 대각선을 가운데 열로 이동
        new_matrix[i][n//2] = matrix[i][i]

        # 2. 가운데 열을 부 대각선으로 이동
        new_matrix[i][n-1-i] = matrix[i][n//2]

        # 3. 부 대각선을 가운데 행으로 이동
        new_matrix[n//2][i] = matrix[n-1-i][i]

        # 4. 가운데 행을 주 대각선으로 이동
        new_matrix[i][i] = matrix[n//2][i]

    return new_matrix


def main():
    T = int(input())

    for test_case in range(T):
        n, d = map(int, input().split())
        matrix = [input().split() for _ in range(n)]

        spin_cnt = (d//45)%8

        for _ in range(spin_cnt):
            matrix = spin_matrix(matrix, n)

        for row in matrix:
            print(*row)


if __name__ == "__main__":
    main()