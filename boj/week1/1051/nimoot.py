# max_square = min(n, m)
# max_square 크기 기준으로 네 점 찾아서 같은 수 인지 확인.

n, m =map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]

min_square = min(n, m)
if min_square == n: # 행이 작으면
    x_move = 0
    y_move = m-n # 가로로 움직일 수 있음
else: # 열이 작으면
    x_move = n-m # 세로로 움직일 수 있음
    y_move = 0
    
for cal in range(min_square, 1, -1): # 한 변의 길이
    for y in range(y_move+1):
        for x in range(x_move+1):
            if arr[x][y] == arr[x][y+cal-1] == arr[x+cal-1][y] == arr[x+cal-1][y+cal-1]: # 네 점의 값이 같다면
                print(cal*cal)
                exit()
    # cal값 기준으로 충족하는 네 점이 없었으므로 이동범위 늘려서 재탐색 시도
    x_move += 1
    y_move += 1

# for문 돌렸을 때 안되면 기본 정사각형 크기 출력
print(1)