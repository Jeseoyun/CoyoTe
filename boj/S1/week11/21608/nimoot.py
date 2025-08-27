n = int(input())

arr = list([0] * n for _ in range(n))
# print(arr)
stu = []
total = list([] for _ in range(n*n))
# print(total)

dxy = [[-1,0],[0,-1],[0,1],[1,0]]


for _ in range(n*n):
    num = list(map(int, input().split()))
    total[num[0]-1]=num[1:]
    k = num[0]
    nums = set(num[1:])
    x, y = -1, -1

    sidx = len(stu)-1
    isidx = False
    fhubo = []
    while sidx >= 0:
        if stu[sidx][0] in nums:
            x, y = stu[sidx][1],stu[sidx][2]

            hubo = []
            for m in dxy:
                nx, ny = x+m[0],y+m[1]

                if 0<=nx<n and 0<=ny<n and arr[nx][ny] == 0:
                    cnt = 0
                    injup = 0
                    for m in dxy:
                        hx,hy = nx+m[0],ny+m[1]
                        if 0<=hx<n and 0<=hy<n:
                            if arr[hx][hy] == 0:
                                cnt += 1
                            elif arr[hx][hy] in nums:
                                injup += 1
                    hubo.append([injup,cnt,nx,ny])
            if len(hubo) > 0:
                # print(hubo)
                hubo.sort(key=lambda x: [-x[0],-x[1]])
                fhubo.append(hubo[0])
        sidx -=1
    if len(fhubo) == 0: ## 인접한 게 아무것도 없다.
        xhubo = []
        for ix in range(n):
            for iy in range(n):
                if arr[ix][iy] == 0:
                    cnt = 0
                    injup = 0
                    for m in dxy:
                        hx,hy = ix+m[0],iy+m[1]
                        if 0<=hx<n and 0<=hy<n:
                            if arr[hx][hy] == 0:
                                cnt += 1
                            elif arr[hx][hy] in nums:
                                injup += 1
                    xhubo.append([injup,cnt,ix,iy])
        xhubo.sort(key=lambda x:[-x[0],-x[1]])
        # print('no injup',xhubo)
        x,y=xhubo[0][2],xhubo[0][3]
        # arr[ix][iy] = k
        arr[x][y] = k
    else:
        fhubo.sort(key=lambda x:[-x[0],-x[1],x[2],x[3]])
        # print('after',fhubo)
        x, y = fhubo[0][2],fhubo[0][3]
        arr[x][y] = k
    
    # print(arr)
    stu.append([k,x,y])

# print(arr)
ans = 0
for i in range(n):
    for j in range(n):
        num = arr[i][j]
        tonum = set(total[num-1])
        like = 0
        for m in dxy:
            ni,nj = i+m[0],j+m[1]
            if 0<=ni<n and 0<=nj<n and arr[ni][nj] in tonum:
                like += 1
        # print(num, like, int(pow(10,like-1)))
        ans += int(pow(10,like-1))

print(ans)

