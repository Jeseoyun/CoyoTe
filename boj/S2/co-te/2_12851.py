from collections import deque

def bfs():
    queue = deque()

    queue.append(n)
    while queue:
        cur = queue.popleft()

        if cur == k:
            route = 1
            # print(queue)
            while queue:
                if queue.popleft()==k:
                    route += 1
            return route

        for m in [-1,1,cur]:
            new = cur + m

            if 0<=new<=100000 and (visited[new] == 0 or visited[new] == visited[cur]+1):
                queue.append(new)
                visited[new]=visited[cur]+1



n, k = map(int, input().split())
visited = [0]*100001

route = bfs()

print(visited[k])
print(route)