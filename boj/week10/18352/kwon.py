import heapq
from collections import defaultdict

INF = float("inf")

N, M, K, X = map(int, input().split())

graph = defaultdict(list)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)


def dijkstra(start):
    dist_list = [INF] * (N + 1)
    dist_list[start] = 0
    # for node in graph[start]:
    #     dist_list[node] = 1
    q = [(0, start)]

    while q:
        dist, cur_node = heapq.heappop(q)
        if dist_list[cur_node] < dist:
            continue

        for n_node in graph[cur_node]:
            if dist + 1 < dist_list[n_node]:
                dist_list[n_node] = dist + 1
                heapq.heappush(q, (dist + 1, n_node))

    return dist_list


inf_cnt = 0
for node, dist in enumerate(dijkstra(X)[1:], start=1):
    if dist == K:
        print(node)
    else:
        inf_cnt += 1

if inf_cnt == N:
    print(-1)
