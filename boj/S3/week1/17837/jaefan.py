# 새로운 게임 2 
# https://www.acmicpc.net/problem/17837

import sys 

inputf = sys.stdin.readline

# 방향: 1=오른쪽, 2=왼쪽, 3=위, 4=아래 (1-index)
DIRECTIONS = [None, (0, 1), (0, -1), (-1, 0), (1, 0)]
# 반대 방향
OPPOSITE = [None, 2, 1, 4, 3]

def main():
    N, K = map(int, inputf().split())
    grid = [list(map(int, inputf().split())) for _ in range(N)]  # 0: white, 1: red, 2: blue
    
    # 말 정보: [r, c, d] (0-index 좌표)
    horses = []
    for i in range(K):
        r, c, d = map(int, inputf().split())
        horses.append([r-1, c-1, d])  # 0-index로 변환
    
    # 각 칸에 쌓인 말들 (아래에서 위로 저장)
    board = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(K):
        r, c, _ = horses[i]
        board[r][c].append(i)
    
    for turn in range(1, 1001):
        for i in range(K):
            r, c, d = horses[i]
            dr, dc = DIRECTIONS[d]
            nr, nc = r + dr, c + dc
            
            # 파란색이거나 체스판 밖인 경우
            if nr < 0 or nr >= N or nc < 0 or nc >= N or grid[nr][nc] == 2:
                # 방향 반대로 변경
                d = OPPOSITE[d]
                horses[i][2] = d
                dr, dc = DIRECTIONS[d]
                nr, nc = r + dr, c + dc
                
                # 반대 방향도 파란색이거나 체스판 밖이면 이동 안 함
                if nr < 0 or nr >= N or nc < 0 or nc >= N or grid[nr][nc] == 2:
                    continue
            
            # 현재 칸에서 말 i와 그 위의 말들을 찾음
            idx = board[r][c].index(i)
            moving = board[r][c][idx:]  # 말 i와 그 위의 말들
            board[r][c] = board[r][c][:idx]  # 원래 칸에는 그 아래 말들만 남김
            
            # 이동할 칸의 색에 따라 처리
            if grid[nr][nc] == 0:  # 흰색
                board[nr][nc].extend(moving)
            elif grid[nr][nc] == 1:  # 빨간색
                board[nr][nc].extend(reversed(moving))
            
            # 이동한 말들의 위치 업데이트
            for horse_idx in moving:
                horses[horse_idx][0] = nr
                horses[horse_idx][1] = nc
            
            # 4개 이상 쌓이면 종료
            if len(board[nr][nc]) >= 4:
                print(turn)
                return
    
    print(-1)

if __name__ == "__main__":
    main()