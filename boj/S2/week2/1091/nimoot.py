import math

def rot():
    cnt = 0
    # temp = [0 for _ in range(n)]
    arr = [i for i in range(n)]
    visited = set()
    while True:
        temp = [0 for _ in range(n)]
        for i in range(n):
            temp[i] = arr[s[i]]
        # print(temp)

        cnt += 1
        
        temp_comp = [tnum%3 for tnum in temp]

        if temp_comp == p:
            print(cnt)
            return
        else:
            arr = temp
        
        if tuple(temp_comp) in visited:
            print(-1)
            return
        
        visited.add(tuple(temp_comp))


n = int(input())
p = list(map(int, input().split())) # 2 0 1
s = list(map(int, input().split())) # 1 2 0

arr_comp = [i%3 for i in range(n)]

if arr_comp == p:
    print(0)
else:
    rot()