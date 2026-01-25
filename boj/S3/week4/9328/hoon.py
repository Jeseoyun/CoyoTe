# 백준: 열쇠
# 저번주랑 비슷한 문제

from collections import deque
import sys
inputf = sys.stdin.readline

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def BFS(board, size_y, size_x, key_list, visited):
    documents = 0
    queue = deque([])
    queue.append((0,0, set(key_list)))
    visited[0][0] = set(key_list)

    while queue:
        y, x, keys = queue.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or nx < 0 or ny >= size_y+2 or nx >= size_x+2:
                continue
            
            # print(keys)
            if  keys <= visited[ny][nx]:
                continue
            
            if board[ny][nx] == '*':
                continue


            new_keys = keys

            if 'A' <= board[ny][nx] <= 'Z':
                # 문을 열 수 있는 열쇠가 없으면 못 지나감
                if board[ny][nx].lower() not in keys:
                    continue
            
            elif 'a' <= board[ny][nx] <= 'z':
                if board[ny][nx] not in keys:
                    # 새로운 set 객체를 만들어야 다른 경로에 영향을 주지 않음
                    new_keys = keys | {board[ny][nx]}
            
            elif board[ny][nx] == '$': # 문서
                documents += 1
                board[ny][nx] = '.'

            visited[ny][nx] = new_keys
            queue.append((ny, nx, new_keys))

    return documents


def print_board(board):
    for li in board:
        for elem in li:
            print(elem, end=" ")
        print()
    print()

# 어디에서든 드갈 수 있네? 크기를 키워서 두르게.
def main():
    test_case = int(inputf())
    # print(test_case)
    for _ in range(test_case):
        size_y, size_x = list(map(int, inputf().strip().split()))
        # print(size_y, size_x)
        board = []
        board.append(['.'] * (size_x + 2))
        
        for _ in range(size_y):
            #strip으로 공백 제거 안 해주면 제대로 안 만들어짐
            board.append(['.'] + list(inputf().strip()) + ['.'])
        board.append(['.'] * (size_x + 2))
        # print_board(board)
        key_temp = inputf()

        key_list = []
        if key_temp != 0:
            key_list = list(key_temp.strip())
        # print(key_list)

        visited = [[set()] * (size_x+2) for _ in range(size_y+2)]
        # print_board(visited)

        print(BFS(board, size_y, size_x, key_list, visited))

    


if __name__ == "__main__":
    main()