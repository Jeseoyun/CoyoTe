from collections import deque


def bfs(matrix, sx, sy, max_x, max_y):
    if max_x==1 and max_y==1:
        return 'Yes'
    elif matrix[sx+1][sy]==0 and matrix[sx][sy+1]==0:
        return 'No'
    elif matrix[max_x-2][max_y-1]==0 and matrix[max_x-1][max_y-2]==0:
        return 'No'

    queue = deque([(sx, sy)])
    visited = {(sx, sy)}
    dxy = [(0, 1), (1, 0)]  # 오른쪽, 아래쪽

    while queue:
        x, y = queue.popleft()

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            if nx < 0 or nx >= max_x or ny < 0 or ny >= max_y:
                continue

            if (nx, ny) in visited:
                continue

            if not matrix[nx][ny]:
                continue

            if (nx == max_x-1) and (ny == max_y-1):
                return 'Yes'

            queue.append((nx, ny))
            visited.add((nx, ny))

    return 'No'

def main():
    N, M = map(int, input().split())
    city_map = []

    for _ in range(M):
        city_map.append(list(map(int, input().split())))

    result = bfs(city_map, 0, 0, M, N)
    print(result)


if __name__ == "__main__":
    main()