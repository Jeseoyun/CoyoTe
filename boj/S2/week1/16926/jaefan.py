# 배열돌리기 1
# https://www.acmicpc.net/problem/16926

import sys

inputf = sys.stdin.readline

def rotate(arr, N, M):

    result = [[0] * M for _ in range(N)]

    # TODO: rotate the array 
    # 가장 바깥쪽 테두리부터 시작해서 안 쪽 테두리까지 순서대로 돌리기 
    for i in range(min(N, M) // 2):
        # 위쪽 테두리 
        for j in range(i, M - i - 1):
            result[i][j] = arr[i][j + 1]
        # 오른쪽 테두리
        for j in range(i, N - i - 1):
            result[j][M - i - 1] = arr[j + 1][M - i - 1]
        # 아래쪽 테두리
        for j in range(M - i - 1, i, -1):
            result[N - i - 1][j] = arr[N - i - 1][j - 1]
        # 왼쪽 테두리
        for j in range(N - i - 1, i, -1):
            result[j][i] = arr[j - 1][i]


    return result 

def main():
    N, M, R = map(int, inputf().split())
    arr = [list(map(int, inputf().split())) for _ in range(N)]

    for _ in range(R):
        arr = rotate(arr, N, M)

    for row in arr:
        print(*row)
    

if __name__ == "__main__":
    main()