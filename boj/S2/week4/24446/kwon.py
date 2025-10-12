# 알고리즘 수업 - 너비 우선 탐색 3

import sys
from collections import deque

input = sys.stdin.readline

N, M, R = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    q = deque([(start, 0)])
    visited = [-1] * (N + 1)
    visited[start] = 0
    
    while q:
        cur_node, d = q.popleft()
        for n_node in graph[cur_node]:
            if visited[n_node] != -1:
                continue
            visited[n_node] = d + 1
            q.append((n_node, d + 1))

    return visited[1:]

print(*bfs(R), sep='\n')