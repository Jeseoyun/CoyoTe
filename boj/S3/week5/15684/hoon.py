# 백준: 사다리 조작

import sys
inputf = sys.stdin.readline

def dfs(board, cur_cnt, x, y, size_x, size_y, max_cnt):
    if cur_cnt == max_cnt:
        return check(board, size_x, size_y)
    
    for i in range(x, size_y + 1):
        k = 1
        if x == i:
            k = y
        for j in range(k, size_x):
            # 양 옆에 사다리 없어야 함
            if not board[i][j] and not board[i][j - 1] and not board[i][j + 1]:
                board[i][j] = True

                # 선 놓고 탐색하기
                if dfs(board, cur_cnt + 1, i, j + 2, size_x, size_y, max_cnt):
                    return True
                
                # 선 지우기
                board[i][j] = False
    
    return False

# i번 세로줄 타고 내려가면 i번에서 끝나는지 확인
def check(board, size_x, size_y):
    for start in range(1, size_x + 1):
        cur_x = start
        for i in range(1, size_y + 1):
            # 오른쪽 이동 확인
            if board[i][cur_x]:
                cur_x += 1
            # 왼쪽 이동 확인 (1 아니고 사다리 있으면)
            elif cur_x > 1 and board[i][cur_x - 1]:
                cur_x -= 1

        # 하나라도 안 돌아오면 그냥 false 반환
        if cur_x != start:
            return False
    return True

def main():
    # 출발한 그대로 자기 자신으로 내려오려면?
    # 정답이 3이상이면 -1 출력?
    size_x, line_cnt, size_y = map(int, inputf().split())

    board = [[False] * (size_x + 1) for _ in range(size_y + 1)]

    for _ in range(line_cnt):
        #가로선 정보는 (y, x) x+1(생략)으로 표현된다.
        x, y = map(int, inputf().split())
        board[x][y] = True
    
    # dfs 도전
    for max_cnt in range(4):
        if dfs(board, 0, 1, 1, size_x, size_y, max_cnt):
            print(max_cnt)
            return
    
    # 3개 해봤는데 불가능한 경우
    print(-1)


if __name__ == "__main__":
    main()