from collections import deque


def sumbak(num):
    queue = deque([num])
    while queue:
        current = queue.popleft()
        if current == k:
            print(visited[k][0])
            exit()
        for add in [-1,1,current]:
            new = current + add
            if 0 <= new <= 100000 and  sum(visited[new]) >= sum(visited[current]) and visited[new][0] > visited[current][0]:
                queue.append(new)
                if add == current:
                    visited[new] = visited[current]
                    visited[new][1] += 1
                else:
                    visited[new][0] = visited[current][0] +1


n, k = map(int, input().split())

visited = [[float('inf'),0] for _ in range(100001)]
visited[n][0] = 0
sumbak(n)