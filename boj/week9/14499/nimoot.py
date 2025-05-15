n, m, x, y, k = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

oder = list(map(int, input().split()))

dmap = [[0,2,0],[4,1,3],[0,5,0]]

dice = [0,0,0,0,0,0,0]
idx = 1
for mov in oder:
    if mov == 1 and 0<=y+1<m: #동
        y += 1
        dtmp = [dmap[1][1],dmap[1][2],7-dmap[1][1]]
        dmap[1] = dtmp
        if arr[x][y] == 0:
            arr[x][y] = dice[7-dmap[1][1]]
        else:
            dice[7-dmap[1][1]] = arr[x][y]
            arr[x][y] = 0
        print(dice[dmap[1][1]])
                   
    elif mov == 2 and 0<=y-1<m: #서
        y -= 1
        dtmp = [7-dmap[1][1],dmap[1][0],dmap[1][1]]
        dmap[1] = dtmp
        
        if arr[x][y] == 0:
            arr[x][y] = dice[7-dmap[1][1]]
        else:
            dice[7-dmap[1][1]] = arr[x][y]
            arr[x][y] = 0
        print(dice[dmap[1][1]])
    elif mov == 3 and 0<=x-1<n: #북
        x -= 1
        dtmp = [[0,7-dmap[1][1],0],[dmap[1][0],dmap[0][1],dmap[1][2]],[0,dmap[1][1],0]]
        dmap = dtmp
        if arr[x][y] == 0:
            arr[x][y] = dice[7-dmap[1][1]]
        else:
            dice[7-dmap[1][1]] = arr[x][y]
            arr[x][y] = 0
        print(dice[dmap[1][1]])
    elif mov == 4 and 0<=x+1<n: #남
        x += 1
        dtmp = [[0,dmap[1][1],0],[dmap[1][0],dmap[2][1],dmap[1][2]],[0,7-dmap[1][1],0]]
        dmap = dtmp
        if arr[x][y] == 0:
            arr[x][y] = dice[7-dmap[1][1]]
        else:
            dice[7-dmap[1][1]] = arr[x][y]
            arr[x][y] = 0
        print(dice[dmap[1][1]])
    else:
         continue