from collections import deque

def bfs():
    queue = deque()

    queue.append(n)

    while queue:
        loc = queue.popleft()
        print(loc, arr[loc])
        if loc == k:
            return
        
        for move in [-1,1,loc]:
            new = loc+move

            if 0<=new<=100000 and arr[new] ==0:
                arr[new] = arr[loc]+1
                queue.append(new)



n,k = map(int,input().split())
arr = [0]*100001

# print(n,k)

bfs()

print(arr[k])