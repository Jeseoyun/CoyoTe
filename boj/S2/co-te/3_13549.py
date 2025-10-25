from collections import deque

def bfs():
    queue = deque()

    queue.append(n)

    while queue:
        cur = queue.popleft()
        print(cur, moving[cur])

        if cur == k:
            return moving[k][0]
        
        for m in [-1,1,cur]:
            new = cur + m

            if 0<=new<=100000  and sum(moving[new]) >= sum(moving[cur]) and moving[new][0]>moving[cur][0]:
                queue.append(new)
                if m != cur:
                    moving[new][0] = moving[cur][0] + 1
                else:
                    moving[new] = moving[cur]
                    moving[new][1] += 1






n,k = map(int, input().split())

moving = list([float('inf'),0] for _ in range(100001))
moving[n][0] = 0
print(bfs())