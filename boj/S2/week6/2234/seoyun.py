from collections import deque, defaultdict

dxy = [(0, -1), (-1, 0), (0, 1), (1, 0)]  # 서, 북, 동, 남


def define_room(grid, N, M, sx, sy, room_num, visited):
    visited[sx][sy] = room_num
    queue = deque([(sx, sy)])

    while queue:
        x, y = queue.popleft()

        for i, (dx, dy) in enumerate(dxy):
            nx, ny = x + dx, y + dy

            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue

            is_wall = format(grid[x][y], '04b')[3-i] == '1'
            # print(format(grid[x][y], '04b'), format(grid[x][y], '04b')[3 - i], format(grid[x][y], '04b')[3 - i] == '1')
            if is_wall:  # i번째 자리가 1일 경우 벽으로 막힘
                continue

            if visited[nx][ny] != 0:
                continue

            queue.append((nx, ny))
            visited[nx][ny] = room_num


def make_connection(grid, N, M):
    queue = deque([(0, 0, 1)])
    visited = [[False]*N for _ in range(M)]

    graph = defaultdict(set)
    room_size = defaultdict(int)

    visited[0][0] = True

    while queue:
        x, y, r = queue.popleft()
        room_size[grid[x][y]] += 1

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue

            if visited[nx][ny]:
                continue

            if grid[x][y] != grid[nx][ny]:
                graph[grid[x][y]].add(grid[nx][ny])
                graph[grid[nx][ny]].add(grid[x][y])

            queue.append((nx, ny, r+1))
            visited[nx][ny] = True

    return graph, room_size


def main():
    N, M = map(int, input().split())
    castle_map = [list(map(int, input().split())) for _ in range(M)]

    room_info = [[0]*N for _ in range(M)]
    room_num = 1

    # 1. 방 넘버링 하기
    for i in range(M):
        for j in range(N):
            if room_info[i][j] != 0:
                continue

            define_room(castle_map, N, M, i, j, room_num, room_info)
            room_num += 1

    # 2. 그래프로 인접한 방 연결시키기, 방 크기도 같이 구하기
    graph, room_size = make_connection(room_info, N, M)

    print(len(room_size.keys()))  # 방 개수
    print(max(room_size.values()))  # 가장 넓은 방 크기

    # 3. 벽 하나 뚫는다 == 인접한 방을 연결시킨다
    # 인접한 방 크기 더해서 가장 넓어지는 경우 구하기
    max_connected_room = 0
    for node in graph.keys():
        for adj in graph[node]:
            max_connected_room = max(max_connected_room, room_size[node]+room_size[adj])

    print(max_connected_room)


if __name__ == "__main__":
    main()