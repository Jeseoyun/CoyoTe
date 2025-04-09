from typing import List, Tuple, Set
from collections import deque

dyx = ((1, 0), (0, 1), (-1, 0), (0, -1))


def search_area(
    area_map: List[List[int]],
    n: int,
    water_h: int,
    start: Tuple[int, int],
    visited: Set[Tuple[int, int]],
) -> int:
    q = deque([start])
    visited.add(start)

    while q:
        y, x = q.popleft()
        for dy, dx in dyx:
            ny, nx = y + dy, x + dx

            if not (0 <= ny < n and 0 <= nx < n):
                continue
            if (ny, nx) in visited:
                continue
            # 물에 잠겼을 때
            if area_map[ny][nx] - water_h <= 0:
                continue

            q.append((ny, nx))
            visited.add((ny, nx))
    return 1


def main():
    N = int(input())
    area_map = []
    max_h = 0
    for _ in range(N):
        row = list(map(int, input().split()))
        max_h = max(max_h, max(row))
        area_map.append(row)

    max_area_cnt = 0
    for water_h in range(0, max_h + 1):
        visited = set()
        area_cnt = 0
        for y in range(N):
            for x in range(N):
                if (y, x) in visited:
                    continue
                if area_map[y][x] - water_h <= 0:
                    continue
                area_cnt += search_area(area_map, N, water_h, (y, x), visited)

        max_area_cnt = max(area_cnt, max_area_cnt)

    print(max_area_cnt)


if __name__ == "__main__":
    main()
