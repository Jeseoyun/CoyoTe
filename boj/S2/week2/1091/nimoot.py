import math

def rot():
    cnt = 0
    arr = [i for i in range(n)] # 카드
    visited = set()
    while True:
        temp = [0 for _ in range(n)] # 카드 섞기
        for i in range(n):
            temp[i] = arr[s[i]]
        print(temp)

        cnt += 1
        
        temp_comp = [tnum%3 for tnum in temp] # 수열 p와 비교하기 위해 3으로 나눈 나머지
        if temp_comp == p: # p랑 같다면
            print(cnt)
            return
        else: # 같지 않으면 섞은 temp를 카드 배열인 arr에 넣기
            arr = temp
        
        if tuple(temp_comp) in visited: # 똑같은 배열이 만들어졌다 -> 루프
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