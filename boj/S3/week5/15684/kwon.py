import sys

input = sys.stdin.readline


def solve():
    n, m, h = map(int, input().split())

    # ladder[r][c] = r행에서 c번 세로선과 c+1번 세로선을 잇는 가로선 존재 여부
    ladder = [[False] * (n + 1) for _ in range(h + 1)]

    for _ in range(m):
        a, b = map(int, input().split())
        ladder[a][b] = True

    # 현재 사다리 상태에서 i -> i 로 끝나는지 확인
    def is_valid():
        for start in range(1, n + 1):
            pos = start
            for row in range(1, h + 1):
                if pos > 1 and ladder[row][pos - 1]:
                    pos -= 1
                elif pos < n and ladder[row][pos]:
                    pos += 1
            if pos != start:
                return False
        return True

    # target 개수만큼 가로선을 추가해서 성립 가능한지 백트래킹
    def backtrack(start_row, start_col, count, target):
        if count == target:
            return is_valid()

        for row in range(start_row, h + 1):
            col_begin = start_col if row == start_row else 1
            for col in range(col_begin, n):
                # 인접 가로선이 있으면 설치 불가
                if ladder[row][col] or ladder[row][col - 1] or ladder[row][col + 1]:
                    continue

                ladder[row][col] = True
                # 같은 행에서는 바로 옆 칸을 건너뛰어 중복 탐색/인접 설치 방지
                next_col = col + 2 if row == start_row else col + 2
                if backtrack(row, next_col, count + 1, target):
                    return True
                ladder[row][col] = False

            start_col = 1

        return False

    for target in range(4):
        if backtrack(1, 1, 0, target):
            print(target)
            return

    print(-1)


if __name__ == "__main__":
    solve()
