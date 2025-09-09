def spin_matrix(matrix, spin_cnt, N, M):
    new_matrix = [[0]*M for _ in range(N)]

    for s in range(spin_cnt):
        # 1. 윗줄: 왼쪽으로 한 칸 이동
        for i in range(s, M-1-s):
            new_matrix[s][i] = matrix[s][i+1]

        # 2. 오른쪽 줄: 위로 한 칸 이동
        for i in range(s, N-1-s):
            new_matrix[i][M-1-s] = matrix[i+1][M-1-s]

        # 3. 아래쪽: 오른쪽으로 한 칸 이동
        for i in range(M-1-s, s, -1):
            new_matrix[N-1-s][i] = matrix[N-1-s][i-1]

        # 4. 왼쪽 줄: 아래로 한 칸씩 이동
        for i in range(N-1-s, s, -1):
            new_matrix[i][s] = matrix[i-1][s]

    return new_matrix


def main():
    N, M, R = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]

    spin_cnt = min(N, M) // 2

    for r in range(R):
        A = spin_matrix(A, spin_cnt, N, M)

        for row in A:
            print(*row)


if __name__ == "__main__":
    main()