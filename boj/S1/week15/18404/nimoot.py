from collections import deque


def solve():
    queue = deque()
    dxy = [[1,2],[1,-2],[-1,2],[-1,-2],[2,1],[2,-1],[-2,1],[-2,-1]]


    queue.append((knight[0]-1,knight[1]-1,0))
    while queue:
        x, y, cnt = queue.popleft()
        
        for m in dxy:
            nx,ny=x+m[0],y+m[1]
            if 0<=nx<n and 0<=ny<n and arr[nx][ny]==-1:
                arr[nx][ny]=cnt+1
                queue.append((nx,ny,arr[nx][ny]))
                mals_set.discard((nx+1,ny+1))

                if len(mals_set) == 0:
                    for mal in mals:
                        ans.append(arr[mal[0]-1][mal[1]-1])
                    print(*ans)
                    return()


n, mal = map(int,input().split())

knight = list(map(int, input().split()))

mals = []
for _ in range(mal):
    mals.append(list(map(int,input().split())))

ans = []

arr = list([-1 for _ in range(n)] for _ in range(n))
arr[knight[0]-1][knight[1]-1] = 0

mals_set = set(tuple(mal) for mal in mals)

solve()