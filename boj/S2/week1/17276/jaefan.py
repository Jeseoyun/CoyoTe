# 배열 돌리기 
# https://www.acmicpc.net/problem/17276

import sys 
import copy

inputf = sys.stdin.readline 


def rotate(array, degree):
    # 0 <= abs(degree) <= 360
    N = len(array)
    
    # 360도 돌리는 경우 원래대로 돌아옴 
    if abs(degree) == 360 or degree == 0:
        return array 
    
    result = copy.deepcopy(array)
    main_diag = [array[i][i] for i in range(N)]
    sub_diag = [array[i][N-1-i] for i in range(N)]
    center_row = [array[N//2][i] for i in range(N)]
    center_col = [array[i][N//2] for i in range(N)]
    
    if degree == 45:    
        for i in range(N):
            for j in range(N):
                if i == j:  # 주 대각선 <- 가운데 행 
                    result[i][j] = center_row[i]
                elif i == N-1-j:  # 부 대각선 <- 가운데 열 
                    result[i][j] = center_col[i]
                elif i == N//2:  # 가운데 행 <- 부 대각선 
                    result[i][j] = sub_diag[N-1-j]
                elif j == N//2:  # 가운데 열 <- 주 대각선 
                    result[i][j] = main_diag[i]
    elif degree == -45:
        for i in range(N):
            for j in range(N):
                if i == j:  # 주 대각선 <- 가운데 열 
                    result[i][j] = center_col[j]
                elif i == N-1-j:  # 부 대각선 <- 가운데 행 
                    result[i][j] = center_row[N-1-i]
                elif i == N//2:  # 가운데 행 <- 주 대각선 
                    result[i][j] = main_diag[j]
                elif j == N//2:  # 가운데 열 <- 부 대각선 
                    result[i][j] = sub_diag[i]
    
    else: 
        if degree > 0:
            while degree != 0:
                result = rotate(result, 45)
                degree -= 45
        else:
            while degree != 0:
                result = rotate(result, -45)
                degree += 45
    return result 
    


def main():
    
    T = int(inputf())
    
    for tc in range(T):
        N, D = map(int, inputf().split())
        array = [list(map(int, inputf().split())) for _ in range(N)]
        
        rotated = rotate(array, D)
        
        for row in rotated:
            print(*row)
    return 


if __name__ == "__main__":
    main()