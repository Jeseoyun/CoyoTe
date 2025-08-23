# 크기가 n x n인 2차원 정수 배열 X가 있다. (n은 홀수)
from copy import deepcopy
class Matrix:
    def __init__(self):
        self.size, degree = map(int, input().split())
        self.rotate_n = (degree + 360) // 45
        self.matrix = [list(map(int, input().split())) for _ in range(self.size)]
        self.mid = self.size // 2

    def rotate_matrix(self):
        """
        주 대각선(\\)   : [i][i]
        가운데 열(|)    : [i][self.mid]
        부 대각선(/)    : [self.size - i][i]
        가운데 행(-)    : [self.mid][i]
        """
        new_matrix = deepcopy(self.matrix)


        for _ in range(self.rotate_n):
            for i in range(self.size):
                # breakpoint()
                # X의 주 대각선을 ((1,1), (2,2), …, (n, n)) 가운데 열 ((n+1)/2 번째 열)로 옮긴다.
                new_matrix[i][self.mid] = self.matrix[i][i]
                # X의 가운데 열을 X의 부 대각선으로 ((n, 1), (n-1, 2), …, (1, n)) 옮긴다.
                new_matrix[self.size - i - 1][i] = self.matrix[self.size - i - 1][self.mid]
                # X의 부 대각선을 X의 가운데 행 ((n+1)/2번째 행)으로 옮긴다.
                new_matrix[self.mid][i] = self.matrix[self.size - i - 1][i]
                # X의 가운데 행을 X의 주 대각선으로 옮긴다.
                new_matrix[i][i] = self.matrix[self.mid][i]
            self.matrix = deepcopy(new_matrix)


        return new_matrix

    def print_matrix(self):
        for row in self.matrix:
            print(*row)
    

if __name__ == "__main__":
    TC = int(input())
    for _ in range(TC):
        matrix = Matrix()
        matrix.rotate_matrix()
        matrix.print_matrix()