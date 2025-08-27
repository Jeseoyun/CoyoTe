import heapq
from collections import deque


def bfs(graph, start):
    queue = deque([start])
    dist = {node: float('inf') for node in graph.keys()}
    dist[start] = 0

    while queue:
        curr = queue.popleft()
        # print(curr, dist)

        for neighbor in graph[curr]:
            if dist[neighbor] > dist[curr] + 1:
                dist[neighbor] = dist[curr] + 1
                queue.append(neighbor)

    return dist


def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph.keys()}
    dist[start] = 0
    heap = [(0, start)]

    while heap:
        curr_dist, curr_node = heapq.heappop(heap)
        # print(curr_node, curr_dist, dist)
        for neighbor in graph[curr_node]:
            if dist[neighbor] > curr_dist + 1:
                dist[neighbor] = curr_dist + 1
                heapq.heappush(heap, (curr_dist+1, neighbor))

    return dist


def main():
    N, M, K, X = map(int, input().split())  # 도시 개수, 도로 개수, 거리 정보, 출발 도시 번호
    graph = {node: [] for node in range(1, N+1)}

    for _ in range(M):
        start, end = map(int, input().split())
        graph[start].append(end)

    # dist = bfs(graph, X)
    dist = dijkstra(graph, X)

    FLAG = False
    for node in dist.keys():
        if dist[node] == K:
            FLAG = True
            print(node)

    if not FLAG:
        print(-1)


if __name__ == "__main__":
    main()