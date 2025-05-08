import sys
from collections import deque

input = sys.stdin.readline
# print = sys.stdout.write

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)

def search_hack(start):
    q = deque([start])
    visited = [False] * (N + 1)
    visited[start] = True
    cnt = 0

    while q:
        cur_com = q.popleft()
        cnt += 1
        for n_com in graph[cur_com]:
            if visited[n_com]:
                continue
            q.append(n_com)
            visited[n_com] = True
    
    return cnt

max_com_cnt = 0
result = []
total_visited = set()
for com in range(1, N + 1):
    com_cnt = search_hack(com)
    # print(com_cnt)
    if max_com_cnt < com_cnt:
        max_com_cnt = com_cnt
        result = [com]
    elif max_com_cnt == com_cnt:
        result.append(com)

print(*sorted(result))