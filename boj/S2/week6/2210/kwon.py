# 5×5 크기의 숫자판이 있다. 각각의 칸에는 숫자(digit, 0부터 9까지)가 적혀 있다.
# 이 숫자판의 임의의 위치에서 시작해서, 인접해 있는 네 방향으로 다섯 번 이동하면서, 각 칸에 적혀있는 숫자를 차례로 붙이면 6자리의 수가 된다.
# 이동을 할 때에는 한 번 거쳤던 칸을 다시 거쳐도 되며, 0으로 시작하는 000123과 같은 수로 만들 수 있다.

# 숫자판이 주어졌을 때, 만들 수 있는 서로 다른 여섯 자리의 수들의 개수를 구하는 프로그램을 작성하시오.

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
