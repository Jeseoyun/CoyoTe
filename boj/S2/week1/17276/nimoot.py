# 디버깅용
## temp = arr는 안되지만 arr = temp는 되나? 얕복/깊복

T = int(input())
# print(T)

for _ in range(T):
    n, d = map(int,input().split())
    # print(n,d)

    arr = list(list(map(int, input().split())) for _ in range(n))
    # print(*arr)

    if d != 0:
        d//=45
    
    if d < 0:
        d += 8
    
    if d == 8:
        d = 0

    # print('회전 ',d,'번 실행!')
    while d > 0: # 시계방향 회전
        ## temp = arr
        temp = [row[:] for row in arr]

        ju = []
        mid_c = []
        bu = []
        mid_r = []

        for i in range(n):
            ju.append(temp[i][i])
            mid_c.append(temp[i][n//2])
            bu.append(temp[i][n-i-1])
            mid_r.append(temp[n//2][i])

        # print(bu)
        bu.reverse()
        # print(bu)

        for i in range(n):
            temp[i][n//2] = ju[i]
            temp[i][n-i-1] = mid_c[i]
            temp[n//2][i] = bu[i]
            temp[i][i] = mid_r[i]
        
        arr = temp
        ## arr = [row[:] for row in temp]
        d -= 1
    
    for i in range(n):
        print(*arr[i],end=' ')
        print()
    # print()