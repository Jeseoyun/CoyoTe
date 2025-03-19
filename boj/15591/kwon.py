from collections import deque

# 영상에 대해 유사도가 K 이상인 모든 동영상 추천

N, Q = map(int, input().split())
INF = float('inf')

graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    p, q, r = map(int, input().split())
    graph[p].append((q, r))
    graph[q].append((p, r))

visited = [[False] * (N + 1) for _ in range(N + 1)]

# print(*graph, sep='\n')

def get_relations(graph, start, k):
    q = deque([(start, INF)])
    visited = [False] * (N + 1)
    visited[start] = True
    cnt = 0

    while q:
        node, min_r = q.popleft()

        for n_node, r in graph[node]:
            if visited[n_node]:
                continue
            visited[n_node] = True
            r = min(min_r, r)
            if r >= k:
                cnt += 1
            q.append((n_node, r))
    return cnt
        
        
for _ in range(Q):
    k, v = map(int, input().split())

    print(get_relations(graph, v, k))


###################################################################

import sys
input = sys.stdin.readline

class DSU:
    def __init__(self, n):
        self.parent = list(range(n+1))
        self.size = [1]*(n+1)
    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb: return
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]

N, Q = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(N-1)]
# (u, v, relevance)
queries = []
for i in range(Q):
    k, v = map(int, input().split())
    queries.append((k, v, i))

# Sort edges descending by relevance
edges.sort(key=lambda x: -x[2])
# Sort queries descending by threshold k
queries.sort(key=lambda x: -x[0])

dsu = DSU(N)
ans = [0]*Q
e_idx = 0

for k, v, qi in queries:
    while e_idx < len(edges) and edges[e_idx][2] >= k:
        u1, u2, _ = edges[e_idx]
        dsu.union(u1, u2)
        e_idx += 1
    ans[qi] = dsu.size[dsu.find(v)] - 1

print(*ans, sep="\n")
