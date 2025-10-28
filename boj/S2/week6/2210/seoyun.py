BOARD_SIZE = 5
DIGITS_SIZE = 6
dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def dfs(grid, x, y, seen, current, numbers):
    # print(current)
    if len(current) >= DIGITS_SIZE:
        numbers.add(current)
        return

    for dx, dy in dxy:
        nx, ny = x + dx, y + dy

        if nx < 0 or nx >= BOARD_SIZE or ny < 0 or ny >= BOARD_SIZE:
            continue

        new_digit = current + grid[nx][ny]

        if new_digit in seen:
            continue

        seen.add(new_digit)
        dfs(grid, nx, ny, seen, new_digit, numbers)
        seen.remove(new_digit)


def main():
    digits = [list(input().split()) for _ in range(BOARD_SIZE)]

    numbers = set()
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            # print(numbers)
            seen = set()
            dfs(digits, i, j, seen, "", numbers)

    print(len(numbers))


if __name__ == "__main__":
    main()