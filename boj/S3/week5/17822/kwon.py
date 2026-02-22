import sys
from collections import deque

input = sys.stdin.readline


def solve():
    n, m, t = map(int, input().split())
    circles = [deque(map(int, input().split())) for _ in range(n)]

    for _ in range(t):
        x, d, k = map(int, input().split())

        # x의 배수 원판 회전
        for idx in range(x - 1, n, x):
            if d == 0:  # 시계 방향
                circles[idx].rotate(k)
            else:  # 반시계 방향
                circles[idx].rotate(-k)

        to_remove = set()

        # 인접한 같은 수 탐색 (좌우는 원형 연결)
        for i in range(n):
            for j in range(m):
                if circles[i][j] == 0:
                    continue

                nj = (j + 1) % m
                if circles[i][j] == circles[i][nj]:
                    to_remove.add((i, j))
                    to_remove.add((i, nj))

                if i + 1 < n and circles[i][j] == circles[i + 1][j]:
                    to_remove.add((i, j))
                    to_remove.add((i + 1, j))

        # 지울 수가 있으면 제거
        if to_remove:
            for i, j in to_remove:
                circles[i][j] = 0
        else:
            total = 0
            count = 0

            for i in range(n):
                for j in range(m):
                    if circles[i][j] != 0:
                        total += circles[i][j]
                        count += 1

            # 남은 수가 없으면 조정할 필요 없음
            if count == 0:
                continue

            avg = total / count

            # 평균보다 크면 -1, 작으면 +1
            for i in range(n):
                for j in range(m):
                    if circles[i][j] == 0:
                        continue
                    if circles[i][j] > avg:
                        circles[i][j] -= 1
                    elif circles[i][j] < avg:
                        circles[i][j] += 1

    answer = sum(sum(circle) for circle in circles)
    print(answer)


if __name__ == "__main__":
    solve()
