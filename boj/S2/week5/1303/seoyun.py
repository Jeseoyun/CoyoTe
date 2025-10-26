from collections import deque, defaultdict

dxy = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def scouter(sx, sy, target, war_map, visited, N, M):
    cnt = 1
    queue = deque([(sx, sy)])
    visited[sx][sy] = True

    while queue:
        x, y = queue.popleft()

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue

            if visited[nx][ny]:
                continue

            if war_map[nx][ny] == target:
                # print(nx, ny)
                visited[nx][ny] = True
                queue.append((nx, ny))
                cnt += 1

    return cnt**2


def main():
    N, M = map(int, input().split())
    war_map = [list(input()) for _ in range(M)]

    visited = [[False]*N for _ in range(M)]
    power_dict = defaultdict(int)

    for i in range(M):
        for j in range(N):
            if visited[i][j]:
                continue
            target = war_map[i][j]
            p = scouter(i, j, target, war_map, visited, N, M)
            power_dict[target] += p

    print(power_dict['W'], power_dict['B'])


if __name__ == "__main__":
    main()