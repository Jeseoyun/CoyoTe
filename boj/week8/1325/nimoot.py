from collections import deque

def bfs(start):
    global graph
    visited = [False] * (n + 1)
    queue = deque([start])
    visited[start] = True
    count = 1

    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                count += 1
    return count

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]


for _ in range(m):
    A, B = map(int, input().split())
    graph[B].append(A)

max_count = 0
result = []

for i in range(1, n + 1):
    count = bfs(i)
    if count > max_count:
        max_count = count
        result = [i]
    elif count == max_count:
        result.append(i)

print(*result)
