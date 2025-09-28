from collections import defaultdict, deque

N, M = map(int, input().split())

taller = defaultdict(list)
shorter = defaultdict(list)

for _ in range(M):
    a, b = map(int, input().split())
    taller[a].append(b)
    shorter[b].append(a)

def bfs(graph, start):
    visited = set()
    q = deque([start])
    while q:
        node = q.popleft()
        for n in graph[node]:
            if n not in visited:
                visited.add(n)
                q.append(n)
    return visited

result = 0
for i in range(1, N+1):
    visited_taller = bfs(taller, i)
    visited_shorter = bfs(shorter, i)
    # 앞 뒤의 키를 모두 탐색 가능할 경우
    if len(visited_taller) + len(visited_shorter) == N - 1:
        # print(i, visited_taller, visited_shorter)
        result += 1

print(result)