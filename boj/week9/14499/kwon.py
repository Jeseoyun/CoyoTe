n, m, x, y, k = map(int, input().split())

maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))

com = list(map(int, input().split()))

dice = [[0],
        [0, 0, 0],
        [0],
        [0]]

move_x = [0, 0, -1, 1]
move_y = [1, -1, 0, 0]

def move(d):
    global x, y
    tmp_x = x + move_x[d-1]
    tmp_y = y + move_y[d-1]
    
    if tmp_x < 0 or tmp_y < 0 or tmp_x >= n or tmp_y >= m:
        return False
    else:
        if d == 1:
            tmp = dice[1][2]
            dice[1][2] = dice[1][1]
            dice[1][1] = dice[1][0]
            dice[1][0] = dice[3][0]
            dice[3][0] = tmp
        elif d == 2:
            tmp = dice[1][0]
            dice[1][0] = dice[1][1]
            dice[1][1] = dice[1][2]
            dice[1][2] = dice[3][0]
            dice[3][0] = tmp
        elif d == 3:
            tmp = dice[3][0]
            dice[3][0] = dice[2][0]
            dice[2][0] = dice[1][1]
            dice[1][1] = dice[0][0]
            dice[0][0] = tmp
        else:
            tmp = dice[0][0]
            dice[0][0] = dice[1][1]
            dice[1][1] = dice[2][0]
            dice[2][0] = dice[3][0]
            dice[3][0] = tmp
        
        x, y = tmp_x, tmp_y
        return True

def change_num():
    if maps[x][y] == 0:
        maps[x][y] = dice[1][1]
    else:
        dice[1][1] = maps[x][y]
        maps[x][y] = 0

def print_num():
    print(dice[3][0])

for d in com:
    if move(d):
        change_num()
        print_num()