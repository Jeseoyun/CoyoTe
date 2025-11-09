# https://www.acmicpc.net/problem/2210
# 2210. 숫자판 점프

# 알고리즘 종류 좀 늘려야 할듯


class Jumper:
    dxy = ((1, 0), (-1, 0), (0, 1), (0, -1))

    def __init__(self, matrix):
        self.matrix = matrix
        # self.visited = set()
        self.combinations = set()

    def _dfs(self, x, y, num_str):
        if len(num_str) == 6:
            self.combinations.add(num_str)
            return

        for dx, dy in Jumper.dxy:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < 5 and 0 <= ny < 5):
                continue
            # if (nx, ny, num_str) in self.visited:
            #     continue

            n_num_str = num_str + self.matrix[nx][ny]
            # self.visited.add((nx, ny, n_num_str))
            self._dfs(nx, ny, n_num_str)

    def calculate_combination_cnt(self):
        for x in range(5):
            for y in range(5):
                self._dfs(x, y, self.matrix[x][y])

        return len(self.combinations)


if __name__ == "__main__":
    matrix = [input().split() for _ in range(5)]

    jumper = Jumper(matrix)
    print(jumper.calculate_combination_cnt())
