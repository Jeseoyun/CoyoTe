import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(m)]

room_map = [[0] * n for _ in range(m)]
room_areas = {}

d_move = [(0, -1), (-1, 0), (0, 1), (1, 0)]
d_bit = [1, 2, 4, 8]


def bfs(start_x, start_y, room_id):
    """
    (start_x, start_y)에서 BFS를 시작하여
    연결된 방을 탐색하고 방의 넓이를 반환합니다.
    """
    q = deque([(start_x, start_y)])
    room_map[start_x][start_y] = room_id
    current_area = 1

    while q:
        x, y = q.popleft()
        wall_info = grid[x][y]

        for i in range(4):

            i_bit = d_bit[i]

            if (wall_info & i_bit) == 0:
                nx = x + d_move[i][0]
                ny = y + d_move[i][1]

                if 0 <= nx < m and 0 <= ny < n and room_map[nx][ny] == 0:
                    room_map[nx][ny] = room_id
                    q.append((nx, ny))
                    current_area += 1

    return current_area


room_id_counter = 0
for i in range(m):
    for j in range(n):
        if room_map[i][j] == 0:
            room_id_counter += 1
            area = bfs(i, j, room_id_counter)
            room_areas[room_id_counter] = area

print(room_id_counter)

if room_areas:
    print(max(room_areas.values()))
else:
    print(0)

max_merged_area = 0
for x in range(m):
    for y in range(n):
        current_room_id = room_map[x][y]

        for dx, dy in [(0, 1), (1, 0)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < m and 0 <= ny < n:
                neighbor_room_id = room_map[nx][ny]

                if current_room_id != neighbor_room_id:
                    merged_area = (
                        room_areas[current_room_id] + room_areas[neighbor_room_id]
                    )
                    max_merged_area = max(max_merged_area, merged_area)

print(max_merged_area)
