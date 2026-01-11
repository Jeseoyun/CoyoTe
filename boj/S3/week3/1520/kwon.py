import sys

sys.setrecursionlimit(10**5)


class PathFinder:
    dxy = ((1, 0), (-1, 0), (0, 1), (0, -1))

    def __init__(self, m, n, grid):
        self.m = m
        self.n = n
        self.grid = grid
        self.memo = [[-1] * n for _ in range(m)]  # 메모이제이션 배열

    def _valid_path(self, x, y, pre_h):
        if not (0 <= x < self.m and 0 <= y < self.n):
            return False
        if self.grid[x][y] >= pre_h:
            return False
        return True

    def find_path(self, x, y):
        # 도착점에 도달하면 1개의 경로
        if x == self.m - 1 and y == self.n - 1:
            return 1

        # 이미 계산된 값이 있으면 반환
        if self.memo[x][y] != -1:
            return self.memo[x][y]

        total = 0
        current_h = self.grid[x][y]

        for dx, dy in PathFinder.dxy:
            nx, ny = x + dx, y + dy
            if self._valid_path(nx, ny, current_h):
                total += self.find_path(nx, ny)

        self.memo[x][y] = total
        return total


if __name__ == "__main__":
    M, N = map(int, input().split())

    grid = [list(map(int, input().split())) for _ in range(M)]
    path_finder = PathFinder(M, N, grid)

    print(path_finder.find_path(0, 0))
