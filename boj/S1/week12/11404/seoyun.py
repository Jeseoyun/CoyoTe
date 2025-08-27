import heapq
from collections import defaultdict


def dijkstra(graph, start, n):
    dist = {node: float('inf') for node in range(1, n+1)}
    dist[start] = 0

    heap = [(0, start)]

    while heap:
        curr_dist, curr_node = heapq.heappop(heap)

        if curr_dist > dist[curr_node]:
            continue

        for next_dist, next_node in graph[curr_node]:
            new_dist = curr_dist + next_dist

            if dist[next_node] > new_dist:
                dist[next_node] = new_dist
                heapq.heappush(heap, (new_dist, next_node))

    return dist


def main():
    n = int(input())
    m = int(input())

    bus_info = [list(map(int, input().split())) for _ in range(m)]

    graph = defaultdict(list)
    for start, end, cost in bus_info:
        graph[start].append((cost, end))

    for start in range(1, n+1):
        dist = dijkstra(graph, start, n)
        print(" ".join(str(dist[i]) if dist[i] != float('inf') else "0" for i in range(1, n+1)))


if __name__ == "__main__":
    main()