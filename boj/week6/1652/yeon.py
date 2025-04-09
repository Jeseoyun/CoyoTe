# 누울 자리를 찾아라 
# https://www.acmicpc.net/problem/1652

"""
풀이 설명: 
    무지성 완전 탐색 
    가로(row) 방향으로 누울 수 있는 경우의 수와 
    세로(col) 방향으로 누울 수 잇는 경우의 수를 각각 구해줌.

    23 ~ 28 라인 -> 가로 방향으로 누울 수 있는 경우의 수를 구하는 코드 
        - 가로 방향으로 누울 수 있는 경우니까 모든 row 에 대해서 탐색 
        - col을 표현하는 c는 k개씩 증가가 가능해야하기 때문에, for 문 보다는 일반 정수형 변수로 관리 
        (k는 c + k <= N을 만족하는 0 이상 N 이하의 임의의 정수, 코드에서는 안쓰임)
        - 1번째 while 문: c가 N 보다 작을때까지 반복 (하나의 행에 대해서 끝까지 반복)
        - 2번째 while 문: c가 N 보다 작고, 현재 좌표의 값이 'X'인 동안 c값을 +1, 조건을 만족하지 않는다면 아래 if 문으로 전환
        - if 문: 다음 좌표가 방의 내부(c+1 < N)이며, 다음 좌표가 비어 있는 경우에 가로 방향으로 누울 수 있는 경우의 수에 1을 더해줌
        - 3번째 while 문: 누울 수 있는 최대 길이까지 반복하며 c값을 늘려준다. 

    39 ~ 45 라인 -> 세로 방향으로 누울 수 있는 경우의 수를 구하는 코드 
        - r과 c 만 바뀌고, 로직은 동일

"""
import sys 

inputf = sys.stdin.readline 
def main():
    N = int(inputf().rstrip())
    room = list()
    for _ in range(N):
        room.append(list(inputf().rstrip()))

    row_count = 0
    for r in range(N):
        c = 0
        while c < N:
            while c < N and room[r][c] == 'X': c += 1
            if c + 1 < N and room[r][c+1] == '.': row_count += 1
            while c < N and room[r][c] == '.': c += 1
    
    col_count = 0
    for c in range(N):
        r = 0
        while r < N:
            while r < N and room[r][c] == 'X': r += 1
            if r + 1 < N and room[r+1][c] == '.': col_count += 1
            while r < N and room[r][c] == '.': r += 1
    
    print(row_count, col_count)

if __name__=='__main__':
    main()