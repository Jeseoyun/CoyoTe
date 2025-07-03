# 그냥 BFS로 풀었더니 메모리 초과

# from collections import deque

# dy = [-2, -1, 1, 2, 2, 1, -1, -2]
# dx = [1, 2, 2, 1, -1, -2, -2, -1]

# INF = float('inf')

# def BFS(board, cur_y, cur_x, size_y):

#     q = deque()

#     q.append((cur_y, cur_x, 0))
#     board[cur_y][cur_x] = 0

#     while(q):
#         y, x, dist = q.popleft()

#         for i in range(8):
#             ny = y + dy[i]
#             nx = x + dx[i]

#             if ny < 0 or nx < 0 or ny >= size_y or nx >= size_y:
#                 continue
            
#             if board[ny][nx] < dist + 1:
#                 continue
            
#             board[ny][nx] = dist + 1
#             q.append((ny, nx, dist+1))




# def main():
#     size_y, en_num = map(int, input().split())
#     cur_y, cur_x = map(int, input().split())

#     board = [[INF] * size_y for _ in range(size_y)]

#     BFS(board, cur_y-1, cur_x-1, size_y)

#     for _ in range(en_num):
#         en_y, en_x = map(int, input().split())
#         print(board[en_y-1][en_x-1], end=' ')


# if __name__ == "__main__":
#     main()

# 방문 처리를 2차원 배열로 하는게 아니라 dict 구조로 함.
from collections import deque

dy = [-2, -1, 1, 2, 2, 1, -1, -2]
dx = [1, 2, 2, 1, -1, -2, -2, -1]

def BFS(cur_y, cur_x, size_y):
    visited = {}
    q = deque()
    q.append((cur_y, cur_x, 0))
    visited[(cur_y, cur_x)] = 0

    while q:
        y, x, dist = q.popleft()

        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or nx < 0 or ny >= size_y or nx >= size_y:
                continue

            if (ny, nx) not in visited or visited[(ny, nx)] > dist + 1:
                visited[(ny, nx)] = dist + 1
                q.append((ny, nx, dist + 1))

    return visited

def main():
    size_y, en_num = map(int, input().split())
    cur_y, cur_x = map(int, input().split())

    visited = BFS(cur_y - 1, cur_x - 1, size_y)

    for _ in range(en_num):
        en_y, en_x = map(int, input().split())
        print(visited.get((en_y - 1, en_x - 1), -1), end=' ')

if __name__ == "__main__":
    main()