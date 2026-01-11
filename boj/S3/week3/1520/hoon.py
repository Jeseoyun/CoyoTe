# 백준: 내리막 길
# dfs로 경로들을 뒤져야 함. 최대 높이가 10000 이니까 10000 이하로 경로의 길이가 생기긴 함. 뎁스가 10000
# python 재귀 한계를 건드리면 되지만... 실전에서 쓸 수 있을지 모르니 그냥 stack으로 dfs 구현하자

# 시간 초과 남.
# 500 x 500 너무 큰가.
# sys 금지된 코테는 어떡함?

# from collections import deque
# import sys
# inputf = sys.stdin.readline

# dy = [-1, 0, 1, 0]
# dx = [0, 1, 0, -1]

# goal_cnt = 0

# def print_board(board):
#     for li in board:
#         for elem in li:
#             print(elem, end=" ")
#         print()
#     print()

# def DFS(board, size_y, size_x):
#     goal_y = size_y - 1
#     goal_x = size_x - 1

#     # 방문처리할 배열
#     visited = [[False]*size_x for _ in range(size_y)]

#     stack = deque()

#     visited[0][0] = True
#     stack.append((board[0][0], 0, 0, visited))

#     #visited를 통으로 보내야되겠는데

#     while stack:
#         cur_h, y, x, cur_visited = stack.pop()
#         global goal_cnt

#         if y == goal_y and x == goal_x:
#             goal_cnt += 1
#             continue

#         for i in range(4):
#             ny = y + dy[i]
#             nx = x + dx[i]
#             if ny < 0 or ny >= size_y or nx < 0 or nx >= size_x:
#                 continue
#             if cur_visited[ny][nx] == True:
#                 continue
#             if board[ny][nx] >= cur_h:
#                 continue
            
#             cur_visited[ny][nx] = True
#             stack.append((board[ny][nx], ny, nx, cur_visited))
#             cur_visited[ny][nx] = False
            
        

# def main():
#     size_y, size_x = map(int, inputf().split())

#     board = [list(map(int, inputf().split())) for _ in range(size_y)]

#     # print_board(board)

#     DFS(board, size_y, size_x)

#     print(goal_cnt)


# if __name__ == "__main__":
#     main()


# DP를 적용할 때, 출발지부터 해당 도착지까지의 경로를 정하는 게 아니라,
# 해당 도착지부터 목적지까지의 경로를 DP로 저장하는 것임.
# 따라서 아무리 출발지부터 해당 지점까지의 경로 숫자가 늘어나도, DP에 더할 갯수는 안 늘어남.
# 이 발상이 도저히 안 떠올라서 선생님과 대화를 좀 했음.

import sys

sys.setrecursionlimit(10001)
inputf = sys.stdin.readline

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def print_board(board):
    for li in board:
        for elem in li:
            print(elem, end=" ")
        print()
    print()

def DFS(board, size_y, size_x, dp, y, x):
    # 목적지에 도착시 경로를 1개 찾은 것임!!!
    if y == size_y - 1 and x == size_x - 1:
        return 1
    
    # 이미 방문한 적 있다는 건, 해당 지점으로부터 도착지까지 경로의 갯수가 정해졌다는 것
    if dp[y][x] != -1:
        return dp[y][x]

    dp[y][x] = 0
    
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if ny < 0 or ny >= size_y or nx < 0 or nx >= size_x:
            continue
        if board[ny][nx] >= board[y][x]:
            continue
        
        dp[y][x] += DFS(board, size_y, size_x, dp, ny, nx)
    
    return dp[y][x]
            
def main():
    size_y, size_x = map(int, inputf().split())

    board = [list(map(int, inputf().split())) for _ in range(size_y)]

    # print_board(board)
    dp = [[-1] * size_x for _ in range(size_y)]

    goal_cnt = DFS(board, size_y, size_x, dp, 0, 0)

    print(goal_cnt)


if __name__ == "__main__":
    main()